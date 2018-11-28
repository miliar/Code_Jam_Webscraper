#include <fstream>
#include <math.h>
#include <vector>
#include <sstream>
#include <stdlib.h>

using namespace std;

#define PRIME_TARGET pow(2,20)

struct CoinJam
{
    int digitCount;
    int coinCount;

    CoinJam()
    :digitCount(0)
    ,coinCount(0)
	{

	}
};

vector<int64_t> primeNumbers;

void ProducePrimeList();
bool IsDivisble(int64_t, int64_t&);
void ProduceNumber(CoinJam);
void LoadInputs(ifstream&, int&, vector<CoinJam>&);
void DumpInput(const vector<CoinJam>&, int);

int main(int argc, char *argv[])
{
    vector<CoinJam> inputs;
    int inputCount;
    bool debug;

    if(argc < 2)
    {
	fprintf(stderr, "Provide file name\n");
	return 1;
    }
    if(argc > 2)
	debug = true;

    ifstream inputFile(argv[1]);
    if(!inputFile.is_open())
    {
	fprintf(stderr, "Could not open %s\n", argv[1]);
	return 2;
    }

    ProducePrimeList();
    LoadInputs(inputFile, inputCount, inputs);
    if(inputs.empty() || (inputCount == -1) || (inputCount != (int)inputs.size()))
    {
	fprintf(stderr, "Load error\n");
	if(debug)
	    DumpInput(inputs, inputCount);
	return 3;
    }

    if(debug)
	DumpInput(inputs, inputCount);

    for(size_t i=0; i<inputs.size(); i++)
    {
	printf("Case #%d:\n", (int)i+1);
	ProduceNumber(inputs[i]);
    }


    return 0;
}

void LoadInputs(ifstream &file, int &caseCount, vector<CoinJam> &values)
{
    CoinJam value;
 
    values.clear();
    file >> caseCount;
    while(file >> value.digitCount && file >> value.coinCount)
	values.push_back(value);
}

void DumpInput(const vector<CoinJam> &vec, int count)
{
    printf("Case Count: %d\nInputs:\n", count);
    for(size_t i=0; i<vec.size(); i++)
	printf("\t%u: %d %d\n", (unsigned int)i, vec[i].digitCount, vec[i].coinCount);
}

string HexToBinary(char value)
{
    switch(value)
    {
	case '0': return "0000";
	case '1': return "0001";
	case '2': return "0010";
	case '3': return "0011";
	case '4': return "0100";
	case '5': return "0101";
	case '6': return "0110";
	case '7': return "0111";
	case '8': return "1000";
	case '9': return "1001";
	case 'A': return "1010";
	case 'B': return "1011";
	case 'C': return "1100";
	case 'D': return "1101";
	case 'E': return "1110";
	case 'F': return "1111";
    };
    return "0000";
}

void ConvertToBinary(int64_t value, int width, string &result)
{
    char buffer[256];
    memset(buffer, 0, 256);
    snprintf(buffer, 255, "%X", (unsigned int)value);

    result = "";
    for(size_t i=0; i<strlen(buffer); i++)
	result += HexToBinary(buffer[i]);

    int length = result.length();

    if(width > length)
    {
	for(int i=0; i<(width - length); i++)
	    result = "0" + result;
    }
    else if(length > width)
    {
	result = result.substr(length - width, width);
    }
}

void ProduceNumber(CoinJam data)
{
    string workingValue;
    string fill;
    stringstream sstream;

    if(data.digitCount <= 2)
    {
	printf("oops\n");
	return;
    }

    int64_t stop = (data.digitCount - 2) * 10;
    vector<int64_t> divisor(9,0);
    bool rc;
    int successCount = 0;

    while(successCount < data.coinCount)
    {
	for(int i=0; i<stop; i++)
	{
	    ConvertToBinary(i, data.digitCount - 2, workingValue);
	    workingValue = "1" + workingValue + "1";
    
	    rc = IsDivisble(stoll(workingValue, NULL, 2), divisor[0]) &&
		IsDivisble(stoll(workingValue, NULL, 3), divisor[1]) &&
		IsDivisble(stoll(workingValue, NULL, 4), divisor[2]) &&
		IsDivisble(stoll(workingValue, NULL, 5), divisor[3]) &&
		IsDivisble(stoll(workingValue, NULL, 6), divisor[4]) &&
		IsDivisble(stoll(workingValue, NULL, 7), divisor[5]) &&
		IsDivisble(stoll(workingValue, NULL, 8), divisor[6]) &&
		IsDivisble(stoll(workingValue, NULL, 9), divisor[7]) &&
		IsDivisble(stoll(workingValue, NULL, 10), divisor[8]);

	    if(rc)
	    {
		printf("%s ", workingValue.c_str());
		for(int i=0; i<9; i++)
		    printf("%lld ", divisor[i]);
		printf("\n");
		successCount++;
	    }

	    if(successCount >= data.coinCount)
		return;
	}
    }
}

bool IsDivisble(int64_t number, int64_t &divisor)
{
    divisor = 0;
    for(size_t i=0; i<primeNumbers.size(); i++)
    {
	if(number == primeNumbers[i])
	    continue;
	if((number % primeNumbers[i]) == 0)
	{
	    divisor = primeNumbers[i];
	    return true;
	}
    }
    return false;
}

void ProducePrimeList()
{
    int divisible;
    double root;

    divisible = false;

    for(int64_t i=2; i<PRIME_TARGET; i++)
    {
	root = pow(i, 0.5);
	divisible = false;
	for(size_t d = 0; d < primeNumbers.size(); d++)
	{
	    if(primeNumbers[d] > root)
		break;
	    if((i % primeNumbers[d]) == 0)
	    {
		divisible = true;
		break;
	    }
	}

	if(!divisible)
	    primeNumbers.push_back(i);
    }
}


