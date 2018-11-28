#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int flipcount(char*str, int len, char flipper);

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int T;
    fin >> T;
    for (auto t = 0; t < T; t++)
    {
        char stack[110];
        int result = 0;
        fin >> stack;

        result = flipcount(stack, strlen(stack), '+');

        fout << "Case #" << (t+1) << ": " << (result-1) << endl;
    }

    return 0;
}

char flip(char flipper)
{
    return flipper == '+' ? '-' : '+';
}

int flipcount(char*str, int len, char flipper)
{
    if (len == 0)
        return 0;
    while (str[len-1] == flipper) len--;

    flipper = flip(flipper);
    return 1 + flipcount(str, len, flipper);
}