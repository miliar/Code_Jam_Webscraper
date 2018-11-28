#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void getEachDigit(unsigned long long x, vector<int> &digitsInNumber)
{
    digitsInNumber.push_back(x % 10);

    if(x >= 10)
    {
        getEachDigit(x / 10, digitsInNumber);
    }
}

bool fallAsleep(vector<int> &digits)
{
    for(short i=0; i<10; i++)
    {
        if(digits[i] == 0)
        {
            return false;
        }
    }

    return true;
}

int main()
{
    ifstream infile;
    infile.open("A-large.in");

    int numberOfInputs;
    unsigned long long n;
    infile >> numberOfInputs;

    for(int i=0; i<numberOfInputs; i++)
    {
        infile >> n;

        if(n == 0)
        {
            cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
        }
        else
        {
            vector<int> digits;

            for(int j=0; j<10; j++)
            {
                digits.push_back(0);
            }

            int j;
            for(j=1; !fallAsleep(digits); j++)
            {
                vector<int> digitsInNumber;
                getEachDigit(j * n, digitsInNumber);

                for(int k=0; k<digitsInNumber.size(); k++)
                {
                    digits[digitsInNumber[k]] = 1;
                }
            }

            cout << "Case #" << i+1 << ": " << (j - 1) * n << endl;
        }
    }

    infile.close();

    return 0;
}
