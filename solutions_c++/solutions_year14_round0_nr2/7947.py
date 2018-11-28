#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int T;
    fin >> T;

    for (int k=0; k<T; k++) // TEST CASES
    {


       double C, F, X;
       fin >> C >> F >> X;

       double time = 0;
       double cps = 2;

       while( time + X/cps > time + C/cps + X/(cps + F))
       {
           time = time + C/cps;
           cps = cps + F;
       }

       time = time + X/cps;

       fout << "Case #" << k+1 << ": " << std::setprecision(7) << fixed << time << endl;

    }

    return 0;
}
