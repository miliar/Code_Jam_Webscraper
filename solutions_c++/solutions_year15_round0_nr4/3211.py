/*
ID: 
PROG: 
LANG: C++
*/

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

#define INF ~(1 << 31)

using namespace std;

string x_2 [] = {"RGRG", "GGGG", "RGRG", "GGGG"};
string x_3 [] = {"RRRR", "RRGR", "RGGG", "RRGR"};
string x_4 [] = {"RRRR", "RRRR", "RRRG", "RRGG"};


int main(int argc, char *argv[]) {
    
    ifstream fin("d.in");
    ofstream fout("d.out");
    
    int C; fin >> C;
    for (int c = 1; c <= C; c++)
    {
        int X, R, C; fin >> X >> R >> C;
        fout << "Case #" << c << ": ";
        switch (X) {
            case 1:
                fout << "GABRIEL\n";
                break;
            case 2:
                fout << ((x_2[R-1][C-1] == 'R') ? "RICHARD\n" : "GABRIEL\n");
                break;
            case 3:
                fout << ((x_3[R-1][C-1] == 'R') ? "RICHARD\n" : "GABRIEL\n");
                break;
            case 4:
                fout << ((x_4[R-1][C-1] == 'R') ? "RICHARD\n" : "GABRIEL\n");
            default:
                break;
        }
    }
    
    fin.close();
    fout.close();
    return 0;
}