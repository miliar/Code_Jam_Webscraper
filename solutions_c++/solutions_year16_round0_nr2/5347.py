#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int switchIndex(string str)
{
    int i;
    for(i=str.length() - 1; i>=0; i--)
    {
        if(str[i] == '-')
        {
            break;
        }
    }

    return i;
}

int main()
{
    ifstream infile;
    infile.open("B-large.in");

    int numberOfInputs;
    infile >> numberOfInputs;

    for(int i=0; i<numberOfInputs; i++)
    {
        string str;
        infile >> str;

        long long index;
        long long numberOfActions = 0;

        while((index = switchIndex(str)) != -1)
        {
            for(long long j=0; j<=index; j++)
            {
                if(str[j] == '-')
                {
                    str[j] = '+';
                }
                else
                {
                    str[j] = '-';
                }
            }

            numberOfActions++;
        }

        cout << "Case #" << i+1 << ": " << numberOfActions << endl;
    }

    infile.close();

    return 0;
}
