#include <iostream>
#include <ios>
#include <iomanip>
using namespace std;

double get_time(int num_farms, double C, double F, double X, double P = 2.0)
{
    double production = P;
    double time = 0;

    for (int i = 0; i < num_farms; ++i) {
        time += C / production;
        production += F;
    }

    time += X / production;

    return time;
}

int main(int argc, char **argv)
{
    int ncases;
    cin >> ncases;

    for (int i = 0; i < ncases; ++i) {
        cout << "Case #" << (i+1) << ": ";

        double C, F, X;
        cin >> C >> F >> X;

        int num = 0;
        int iter = 0, total = 100000000;

        double time = get_time(num, C, F, X);
        double t;
        while ((t = get_time(++num, C, F, X)) < time) {
            time = t;
            if (++iter > total) {
                cout << "CRASH!";
                exit(1);
            }
        }

        cout << fixed << setprecision(7) << showpoint << time;

        cout << endl;
    }
}