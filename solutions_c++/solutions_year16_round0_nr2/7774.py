#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream input;
    ofstream output;

    input.open("input.in");
    output.open("output.txt");

    int t;
    input >> t;
    input.ignore(37627, '\n');

    for (int i = 1; i <= t; i++)
    {
        string line;
        getline(input, line);

        int sub_intervals = 1;
        int a = line.length();

        for (int i = 1; i < a; i++)
        {
            if (line[i] != line[i-1])
                sub_intervals++;
        }

        output << "Case #" << i << ": ";
        if (line[line.length()-1] == '+')
            output << sub_intervals - 1;
        else
            output << sub_intervals;
        output << endl;
    }

    input.close();
    output.close();

    return 0;
}
