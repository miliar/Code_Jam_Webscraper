#include <algorithm>
#include <bitset>
#include <fstream>
#include <iostream>
#include <iterator>
#include <cmath>
#include <sstream>
#include <vector>
using namespace std;

int main(int argc, char** argv)
{
    if (argc != 3)
    {
        cerr << "Invalid commandline parameters" << endl;
        return -1;
    }

    fstream input(argv[1], fstream::in);
    fstream output(argv[2], fstream::out | fstream::trunc);

    int numTestCases;
    input >> numTestCases;

    for (int i = 0; i < numTestCases; i++)
    {
        int max;
        char digit;
        int *shyness;
        int friends = 0;
        int total = 0;

        input >> max;
        shyness = new int[max + 1];

        for (int j = 0; j < (max + 1); j++)
        {
            input >> digit;
            shyness[j] = digit - '0';
        }

        total = shyness[0];

        for (int j = 1; j < (max + 1); j++)
        {
            if (total < j) {
                friends += (j - total);
                total += (j - total);
            }
            total += shyness[j];
        }

        output << "Case #" << (i + 1) << ": " << friends << endl;

        delete [] shyness;
    }
}