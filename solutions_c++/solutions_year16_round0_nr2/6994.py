
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>      // file I/O
#include <cstdlib>      // for exit (1)

using namespace std;

int main ()
{
    ifstream fin;
    ofstream fout;
    fin.open("input2.txt");
    fout.open("output2.txt");
    int64_t t;
    fin >> t;
    string stack;
    int64_t length;
    int64_t moves = 0;
    for (int64_t k = 1; k <= t; k++)
    {
        moves = 0;
        fin >> stack;
        length = stack.length();
        for (int64_t j = 0; j < length - 1; j++)
        {
            if(stack[j] != stack[j+1])
                moves++;
        }
        if (stack[length - 1] == '-')
            moves++;
        fout <<"Case #" << k << ": " << moves << endl;
    }
    
    fin.close();
    fout.close();
}