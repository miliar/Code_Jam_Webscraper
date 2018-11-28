#include <iostream>
#include <fstream>
#include <cstring>
#include <iomanip>

using namespace std;

int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int T;
    fin >> T;
    for (int t = 1; t <= T; t++) {
        double C, F, X;
        fin >> C >> F >> X;
        double breakPt = X*F/C - F;
        double time = 0, R;
        for (R = 2.0; R < breakPt; R += F) time += C/R;
        time += X/R;
        fout << "Case #" << t << ": " << setprecision(7) << fixed << time << "\n";
    }
}