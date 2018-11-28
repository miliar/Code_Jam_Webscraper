#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ifstream infile("B-large.in");
    ofstream outfile("B-large.out");

    int T;
    infile >> T;

    double C, F, X;
    for(int t=0; t<T; t++)
    {
        infile >> C >> F >> X;

        double maxRate = (X-C)*F/C;

        double time=0;
        double rate=2;
        while(rate<maxRate)
        {
            time += C/rate;
            rate = rate+F;
        }
        time += X/rate;
        outfile << setprecision(7) << fixed << showpoint << "Case #" << t+1 << ": " << time << endl;
    }

    infile.close();
    outfile.close();
    return 0;
}
