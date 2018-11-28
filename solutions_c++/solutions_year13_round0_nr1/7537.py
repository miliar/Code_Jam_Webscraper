#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

bool completed;

int ch (char a)
{
    if (a == 'O')
        return 1;
    if (a == 'X')
        return -1;
    return 0;
}

int test (char a, char b, char c, char d)
{
    if (a == '.' || b == '.' || c == '.' || d == '.') {
        completed = false;
        return 0;
    }
    
    return  ch(a) + ch(b) + ch(c) + ch(d);    
}

int main (void)
{
    fstream inputfile("G:\\ain.txt", ios::in);
    fstream outfile("G:\\aout.txt", ios::out);
    
    int tests;
    int total_tests;
    char field[4][5];

    int high;
    int low;
    int temp;

    inputfile >> total_tests;

    for (tests = 1; tests <= total_tests; tests++)
    {
        for (int i=0; i<4; i++)
            inputfile >> field[i];

        completed = true;
        high = low = 0;

        for (int i=0; i<4; i++) {
            temp = test (field[i][0], field[i][1], field[i][2], field[i][3]);
            high = max (high, temp);
            low  = min (low , temp);
        }

        for (int i=0; i<4; i++) {
            temp = test (field[0][i], field[1][i], field[2][i], field[3][i]);
            high = max (high, temp);
            low  = min (low , temp);
        }

        temp = test (field[0][0], field[1][1], field[2][2], field[3][3]);
        high = max (high, temp);
        low  = min (low , temp);

        temp = test (field[3][0], field[2][1], field[1][2], field[0][3]);
        high = max (high, temp);
        low  = min (low , temp);

        outfile << "Case #" << tests;
        
        if (high >= 3)
            outfile << ": O won" << endl;
        else if (low <= -3)
            outfile << ": X won" << endl;
        else if (completed)
            outfile << ": Draw" << endl;
        else 
            outfile << ": Game has not completed" << endl;
    }

    inputfile.close();
    outfile.close();


}

