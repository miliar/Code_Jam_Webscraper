#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream input;
    ofstream output;

    input.open("A-large.in");
    output.open("output.out");

    int cases;
    input >> cases;

    for(int i = 0; i < cases; i++)
    {
        string shyness;
        int smax;
        input >> smax;
        input >> shyness;

        int people = 0, friends = 0;
        for(int j = 0; j < (smax + 1); j++)
        {
            if(people < j)
            {
                friends += j - people;
                people += j - people;
            }

            people += (shyness[j] - '0');
        }

        output << "Case #" << (i + 1) << ": " << friends << endl;
    }

    input.close();
    output.close();
    system("pause");
    return 0;
}
