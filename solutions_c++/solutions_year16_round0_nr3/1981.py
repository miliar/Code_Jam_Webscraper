#include <cmath>
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char * argv[])
{
    int cases = 0;

    ifstream fin("C-large.in");
    ofstream fout("write4a.txt");

    int n = 0,
        j = 0;

    bool * digits = NULL;

    bool prime = true;
    int divisor[9] = {};

    unsigned int largest = 1;

    int digitrem = 1;
    int remainder = 1;

    int ones = 2;
    bool carry = false;

    int jamcoins = 0;

    if(fin.is_open())
    {
        //cout << "File opened." << endl;

        fin >> cases;

        for(int test = 1; test <= cases; test++)
        {
            fout << "Case #" << test << ":" << endl;

            fin >> n;
            fin >> j;

            digits = new bool[n];

            digits[0] = true;
            for(int i = 1; i < n - 1; i++)
            {
                digits[i] = false;
            }
            digits[n - 1] = true;

            while(ones < n && jamcoins < j)
            {
                prime = false;
                for(int base = 2; base <= 10 && !prime; base++)
                {
                    prime = true;
                    largest = 1;
                    for(int power = 0; power < n; power++)
                    {
                        largest *= base;
                    }
                    largest = largest - 1;
                    largest = sqrt(largest);

                    //cout << "largest : " << largest << endl;

                    //cout << "For base " << base << " : " << endl;

                    for(int factor = 2; factor < largest && prime; factor++)
                    {
                        if(factor % base != 0)
                        {
                            digitrem = 1;
                            remainder = 1;
                            for(int p = n - 2; p >= 0; p--)
                            {
                                digitrem = (digitrem * base) % factor;
                                remainder = (remainder + (digits[p] * digitrem) ) % factor;
                            }
                            if(remainder == 0)
                            {
                                prime = false;
                                divisor[base - 2] = factor;
                            }
                        }

                    }
                }

                if(!prime)
                {
                    jamcoins++;
                    for(int out = 0; out < n; out++)
                    {
                        if(digits[out])
                        {
                            fout << "1";
                        }
                        else
                        {
                            fout << "0";
                        }
                    }

                    for(int d = 0; d < 9; d++)
                    {
                        fout << " " << divisor[d];
                    }

                    fout << endl;
                }

                carry = true;

                for(int last = n - 2; carry; last--)
                {
                    carry = digits[last];
                    digits[last] = !digits[last];
                }

                if(digits[ones-1])
                {
                    ones++;
                }
            }

        }

        fin.close();
        fout.close();
    }
    else
    {
        cout << "Could not open file." << endl;
    }

    return 0;
}
