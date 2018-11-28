
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>      // file I/O
#include <cstdlib>      // for exit (1)
#include <inttypes.h>

using namespace std;

bool check(int dig[], int dig2[])
{
    
    for (int i = 0; i < 10; i++)
    {
        if (dig[i] != dig2[i])
            return false;
    }
    return true;
}
int main ()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    int digitsCheck[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int digits[10];
    int64_t t, n, temp;
    fin >> t;
    int64_t initialValue;
    for (int64_t i = 1; i <= t; i++)
    {
        fout << "Case #" << i << ": ";
        for (int i = 0; i < 10; i++)
        {
            digits[i] = -1;
        }
        fin >> n;
        initialValue = n;
        if (n == 0)
        {
            fout << "INSOMNIA" << endl;
            continue;
        }
        while (true)
        {
            temp = n;
            while(temp > 0)
            {
                digits[(temp % 10)] = temp % 10;
                temp = temp / 10;
            }
            
            if (check(digits, digitsCheck) == true)
            {
                fout << n << endl;
                break;
            }
            n = n + initialValue;
        }
    }
    fin.close();
    fout.close();
}

