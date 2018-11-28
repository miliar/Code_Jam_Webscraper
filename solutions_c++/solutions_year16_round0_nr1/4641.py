#include <fstream>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

#define LOOP_LIMIT 200

map<char, bool> foundValues;
int loopCount;

void LoadInputs(ifstream&, int&, std::vector<int>&);
void DumpInput(const std::vector<int>&, int);
void RunTests(const std::vector<int>&, std::vector<int>&);
void EvaluateNumber(int, int&);

int main(int argc, char *argv[])
{
    bool debug = false;

    if(argc < 2)
    {
	fprintf(stderr, "Specify file\n");
	return 1;
    }
    if(argc == 3)
	debug = true;

    ifstream inputFile(argv[1]);
    if(!inputFile.is_open())
    {
	fprintf(stderr, "Could not open: %s\n", argv[1]);
	return 2;
    }

    std::vector<int> testValues, outputs;
    int caseCount = 0;

    LoadInputs(inputFile, caseCount, testValues);
    if(testValues.empty() || (caseCount == -1) || (caseCount != (int)testValues.size()))
    {
	fprintf(stderr, "Load error\n");
	if(debug)
	    DumpInput(testValues, caseCount);
	return 3;
    }

    if(debug)
	DumpInput(testValues, caseCount);
    else
	RunTests(testValues, outputs);

    for(size_t i=0; i<outputs.size(); i++)
    {
	if(outputs[i] == -1)
	    printf("Case #%d: INSOMNIA\n", (int)i+1);
	else
	    printf("Case #%d: %d\n", (int)i+1, outputs[i]);
    }

    inputFile.close();
    return 0;
}

void EvaluateNumber(int input, int &output)
{
    if(loopCount >= LOOP_LIMIT)
	return;

    int value = input * (loopCount + 1);
    string sValue;
    stringstream sstream;
    
    sstream << value;
    sValue = sstream.str();

    for(size_t i=0; i<sValue.length(); i++)
    {
	foundValues[sValue[i]] = true;
    }

    bool rc = true;
    for(int i=0; i<10; i++)
	rc &= foundValues[i + 48];

    if(rc)
	output = value;
    else
    {
	loopCount++;
	EvaluateNumber(input, output);
    }
}

void RunTests(const vector<int> &inputs, vector<int> &outputs)
{
    outputs = vector<int>(inputs.size(), -1);
    for(size_t i=0; i<inputs.size(); i++)
    {
	loopCount = 0;
	foundValues.clear();
	for(int i=0; i<10; i++)
	    foundValues[i + 48] = false;
	
	if(inputs[i] == 0)
	{
	    outputs[i] = -1;
	    continue;
	}
	EvaluateNumber(inputs[i], outputs[i]);
    }
}

void LoadInputs(ifstream &file, int &caseCount, std::vector<int> &values)
{
    int value = 0;
 
    values.clear();
    file >> caseCount;
    while(file >> value)
	values.push_back(value);
}

void DumpInput(const std::vector<int> &vec, int count)
{
    printf("Case Count: %d\nInputs:", count);
    for(size_t i=0; i<vec.size(); i++)
	printf("\t%u: %d\n", (unsigned int)i, vec[i]);
}
