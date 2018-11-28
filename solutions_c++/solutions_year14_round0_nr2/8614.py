#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

const double START_COEF = 2.0;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("testOut.txt");

    int T;
    fin >> T;
    for(int testCount = 1; testCount <= T; testCount++)
    {
        double C, F, X;
        fin >> C >> F >> X;

        double cur_time = C / START_COEF, prev_time = 0;
        double curF = START_COEF + F, prevF = START_COEF;
        while(cur_time + X/curF < prev_time + X/prevF)
        {
            prev_time = cur_time;
            prevF = curF;
            curF += F;
            cur_time += C / prevF;
        } 

        fout << "Case #" << testCount << ": ";
        fout << fixed << setprecision(7) << prev_time + X/prevF << endl;
    }

    fin.close();
    fout.close();
    system("pause");
    return 0;
}
