#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

long long myPow(long long x, int p) {
  if (p == 0) return 1;
  if (p == 1) return x;
  return x * myPow(x, p-1);
}

long long convertWithBase(string number, int base)
{
    long long result = 0;

    int length = number.size();
    for(int i=0; i<length; i++)
    {
        if(number[i] == '1')
        {
            result += myPow(base, length - i - 1);
        }
    }

    return result;
}

long long findDivisor(long long num)
{
    long long divisor;
    for(divisor=2; divisor <= sqrt(num); divisor++)
    {
        if(num % divisor == 0)
        {
            return divisor;
        }
    }

    return 0;
}

void generateJamcoin(vector<string> &jamcoins, int n)
{
    if(jamcoins[0].length() == n)
    {
        return;
    }

    vector<string> copyOfJamcoin;
    for(int i=0; i<jamcoins.size(); i++)
    {
        copyOfJamcoin.push_back(jamcoins[i]);
    }

    jamcoins.clear();
    for(int i=0; i<copyOfJamcoin.size(); i++)
    {
        jamcoins.push_back(copyOfJamcoin[i] + "0");
        jamcoins.push_back(copyOfJamcoin[i] + "1");
    }

    generateJamcoin(jamcoins, n);
}

int main()
{
    ifstream infile;
    infile.open("A-small-practice.in");

    int numberOfInputs;
    infile >> numberOfInputs;

    for(int i=0; i<numberOfInputs; i++)
    {
        int n, numberOfJamcoinsNeeded;
        infile >> n >> numberOfJamcoinsNeeded;

        cout << "Case #" << i+1 << ":" << endl;

        vector<string> possibleJamcoins;
        possibleJamcoins.push_back("0");
        possibleJamcoins.push_back("1");
        generateJamcoin(possibleJamcoins, n - 2);

        for(int j=0; j<possibleJamcoins.size(); j++)
        {
            possibleJamcoins[j] = "1" + possibleJamcoins[j] + "1";
        }

        for(int j=0; j<possibleJamcoins.size() && numberOfJamcoinsNeeded; j++)
        {
            vector<long long> proof;
            for(int k=2; k<11; k++)
            {
                long long trueValue = convertWithBase(possibleJamcoins[j], k);
                long long divisor = findDivisor(trueValue);
                if(divisor != 0)
                {
                    proof.push_back(divisor);
                }
                else
                {
                    break;
                }
            }

            if(proof.size() == 9)
            {
                cout << possibleJamcoins[j];

                for(int r=0; r<proof.size(); r++)
                {
                    cout << " " << proof[r];
                }

                cout << endl;

                numberOfJamcoinsNeeded--;
            }
        }
    }

    infile.close();

    return 0;
}
