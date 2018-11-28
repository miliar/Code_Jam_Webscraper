#include <iostream>
#include <algorithm>
#include <fstream>
#include <iomanip>

using namespace std;

ifstream fin ("B.in");
ofstream fout ("B.out");

double C, F, X;

int main()
{
    fout << fixed << setprecision (8);
    
    int ntest; fin >> ntest;
    for (int test = 0; test < ntest; test++)
    {
    
    fin >> C >> F >> X;
    
    double best = 1e9;
    double ctime = 0.0, cspeed = 2.0;
    for (int i = 0; i < 5000; i++)
    {
        best = min (best, ctime + X / cspeed);
        ctime += C / cspeed;
        cspeed += F;
    }
    
    
    fout << "Case #" << test + 1 << ": " << best << "\n";
    
    }
    
    //system ("Pause");
    return 0;
}
