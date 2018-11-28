#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

ifstream fin("in.in");
ofstream fout("out.out");


bool doCase()
{
    int x, r, c;
    fin >> x >> r >> c;

    if((r*c) % x != 0) return true;
    if((x > r) && (x > c)) return true;
    if(((r == 2) || (c == 2)) && ((x == 4) || (x == 5))) return true;
    if(((r == 1) || (c == 1)) && x > 2) return true;
    if(x >= 7) return true;

    return false;
}



int main()
{
    int t;
    fin >> t;
    for(int i = 1 ; i <= t; i++)
    {
    fout << "Case #" << i << ": ";
    if(doCase()) fout << "RICHARD";
    else fout << "GABRIEL";
    fout << endl;
    }
    return 0;
}
