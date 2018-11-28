#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <bitset>
#include <math.h>

using std::cout;
using std::endl;
using std::string;


bool IsPrimeNumber(long long number, long long* divisor)
{
    if(number < 2)
        return false;
    else if(number == 2 || number == 3)
        return true;

    long double limit = sqrt(static_cast<long double>(number));

    for(long long i = 2; i < (limit + 1.0); i++)
    {
        if(number % i == 0)
        {
            *divisor = i;
            return false;
        }
    }

    return true;
}

long long ConvertBase(const string& input, int base)
{
    long long result = 0;

    for (size_t i = 0; i < input.length(); i++)
    {
        if(input[i] == '1')
        {
            result += powl(base, input.length() - i - 1);
        }
    }

    return result;
}

bool Legitimate(std::vector<long long>& divisors, const string& input)
{
    bool result = true;

    for (int i = 2; i < 11; i++)
    {
        long long base = ConvertBase(input, i);
        long long divisor;

        if(!IsPrimeNumber(base, &divisor))
        {
            divisors.push_back(divisor);
        }
        else
        {
            result = false;
            break;
        }
    }

    return result;
}



int main()
{
    cout << "Working..." << endl;

    std::ifstream input("input.txt" );
    std::ofstream output("output.txt");
    string line;
    std::getline(input, line);
    std::istringstream ss(line);

    long long MIN = 33; // For N=6
    long long MAX = 36; // For N=6
    int caseCount = 0;
    ss >> caseCount;

    int N, J;
    std::getline(input, line);
    ss.clear();
    ss.str(line);
    ss >> N;
    ss >> J;

    if(N == 16)
    {
        MIN = 32769;
        MAX = 65535;
    }
    else if(N == 32)
    {
        MIN = 2147483649;
        MAX = 4294967295;
    }

    int distinct = 0;
    long long number = MIN;

    output << "Case #1:" << endl;

    while(distinct < J)
    {
        std::vector<long long> divisors;
        string binary = std::bitset<64>(number).to_string(); //to binary
        string newStr = binary.substr(64 - N, N);
        bool valid    = (newStr[0] == '1' && newStr[newStr.length() - 1] == '1');
            
        if(valid && Legitimate(divisors, newStr))
        {
            output << newStr;

            for (size_t i = 0; i < divisors.size(); i++)
            {
                output << " " << divisors[i];
            }

            output << endl;
            distinct++;
        }

        number++;
    }

    input.close();
    output.close();

    cout << "Done!" << endl;

    return 0;
}
