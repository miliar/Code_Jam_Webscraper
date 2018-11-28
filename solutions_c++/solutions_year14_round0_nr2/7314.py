#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <sstream>
#include <string>
#include <cmath>
#include <map>
#include <gmpxx.h>

using namespace std;

/* Compile with the gmpxx library */

double cookie(double C, double F, double X)
{
    double elapsed = 0.0;

    double rate = 2.0;

    bool running = true;

    while (running) {
        double t_fin = X / rate;
        double t_up = C / rate + X / (rate + F);

        if (t_fin < t_up) {
            elapsed += t_fin;
            running = false;
        } else {
            elapsed += C / rate;
            rate += F;
        }
    }

    return elapsed;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        exit(1);
    }

    ifstream ifs(argv[1]);

    int T;
    ifs >> T;

    double C, F, X;
    for (int i = 0; i < T; ++i)
    {
        ifs >> C >> F >> X;

        double time = cookie(C, F, X);

        cout << "Case #" << (i+1) << ": ";
        cout << setprecision(7) << time << endl;
    }

    return 0;
}
