#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ofstream output;
    ifstream input;
    input.open("A-large.in");
    output.open("output.txt");

    int t;
    input >> t;

    for (int k = 1; k <= t; k++)
    {
        int digits[10] = {0};
        string s;
        string original = "";
        input >> s;

        while (s.find("Z") != string::npos)
        {
            digits[0]++;
            s.erase(s.find("Z"), 1);
            s.erase(s.find("E"), 1);
            s.erase(s.find("R"), 1);
            s.erase(s.find("O"), 1);
        }

        while (s.find("W") != string::npos)
        {
            digits[2]++;
            s.erase(s.find("T"), 1);
            s.erase(s.find("W"), 1);
            s.erase(s.find("O"), 1);
        }

        while (s.find("U") != string::npos)
        {
            digits[4]++;
            s.erase(s.find("F"), 1);
            s.erase(s.find("O"), 1);
            s.erase(s.find("U"), 1);
            s.erase(s.find("R"), 1);
        }

        while (s.find("X") != string::npos)
        {
            digits[6]++;
            s.erase(s.find("S"), 1);
            s.erase(s.find("I"), 1);
            s.erase(s.find("X"), 1);
        }

        while (s.find("G") != string::npos)
        {
            digits[8]++;
            s.erase(s.find("E"), 1);
            s.erase(s.find("I"), 1);
            s.erase(s.find("G"), 1);
            s.erase(s.find("H"), 1);
            s.erase(s.find("T"), 1);
        }

        while (s.find("O") != string::npos &&
               s.find("N") != string::npos &&
               s.find("E") != string::npos)
        {
            digits[1]++;
            s.erase(s.find("O"), 1);
            s.erase(s.find("N"), 1);
            s.erase(s.find("E"), 1);
        }

        while (s.find("T") != string::npos &&
               s.find("H") != string::npos &&
               s.find("R") != string::npos &&
               s.find("E") != string::npos &&
               s.find("E") != string::npos)
        {
            digits[3]++;
            s.erase(s.find("T"), 1);
            s.erase(s.find("H"), 1);
            s.erase(s.find("R"), 1);
            s.erase(s.find("E"), 1);
            s.erase(s.find("E"), 1);
        }

        while (s.find("F") != string::npos &&
               s.find("I") != string::npos &&
               s.find("V") != string::npos &&
               s.find("E") != string::npos)
        {
            digits[5]++;
            s.erase(s.find("F"), 1);
            s.erase(s.find("I"), 1);
            s.erase(s.find("V"), 1);
            s.erase(s.find("E"), 1);
        }

        while (s.find("S") != string::npos &&
               s.find("E") != string::npos &&
               s.find("V") != string::npos &&
               s.find("E") != string::npos &&
               s.find("N") != string::npos)
        {
            digits[7]++;
            s.erase(s.find("S"), 1);
            s.erase(s.find("E"), 1);
            s.erase(s.find("V"), 1);
            s.erase(s.find("E"), 1);
            s.erase(s.find("N"), 1);
        }

        while (s.find("N") != string::npos &&
               s.find("I") != string::npos &&
               s.find("N") != string::npos &&
               s.find("E") != string::npos)
        {
            digits[9]++;
            s.erase(s.find("N"), 1);
            s.erase(s.find("I"), 1);
            s.erase(s.find("N"), 1);
            s.erase(s.find("E"), 1);
        }

        output << "Case #" << k << ": ";

        for (int i = 0; i <= 9; i++)
        {
            for (int j = 1; j <= digits[i]; j++)
                output << i;
        }

        output << endl;
    }

    input.close();
    output.close();

    return 0;
}
