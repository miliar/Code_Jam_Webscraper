/*******************************************\
*                                           *
*   Cookie Clicker                          *
*   CodeJam 2014                            *
*   Rafael Medina (MedinaSoft)              *
*                                           *
\*******************************************/

#include <iostream>
#include <fstream>
using namespace std;

int main () {
    int LINE = 1, TOT, N;
    double C, F, X;
    for (scanf ("%d", &TOT); LINE <= TOT; LINE++)  {
        scanf("%lf %lf %lf", &C, &F, &X);
        double best = 0.0, calc = 0.0, prevtime = 0.0, cps = 2.0;

        do {
            best = calc;
            calc = prevtime + X / cps;
            prevtime += (C / cps);
            cps += F;
        } while (calc < best || best == 0.0);

        printf("Case #%i: %.7lf\n", LINE, best);
    }
    return 0;
}
