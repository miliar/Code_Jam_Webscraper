#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    string str;    // string from file
    ifstream fin;  // input file
    ofstream fout; // output file
    int T;         // number of test cases
    double time, time1 = 0.0, time2 = 0.0;  // time spent
    const double base = 2;
    double C, F, X;
    double rate;

    fin.open("B-large.in");
    fout.open("B-large.out");

    fin >> T;

    for (int t = 0; t < T; t++)
    {
        fin >> C >> F >> X;
        rate = base;
        time = 0.0;
        for(int farms = 0; ; farms++)
        {
            time1 = C / rate + X / (rate + F);
            time2 = X / rate;
            if (time2 < time1)
            {
                time += time2;
                break;
            }
            else
            {
                time += C / rate;
                rate += F;
            }
        }
        fout << "Case #" << t+1 << ": ";
        fout << setiosflags(ios::fixed) << setiosflags(ios::right) << setprecision(7);
        fout << time << endl;
    }

    fin.close();

    return 0;
}
