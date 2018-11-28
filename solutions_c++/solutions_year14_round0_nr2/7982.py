#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

double solve() {
    double C, F, X, Fc, Fp, Fo = 2;
    cin >> C >> F >> X;
    double nb, y, tb, t = 0; // nobuy, time
    Fp = Fo;
    double nbt, bt;

    do { // buy house until
        nb = X/Fp; // time to not buy
        tb = C/Fp; // time to buy
        y = tb / (1/Fp - 1/(F+Fp)); // find where nb/(tb+wait) lines meet

        nbt = y/Fp;
        bt = C/Fp + y/(Fp+F);
        t += (y >= X) ? nb : C/Fp; // add min time
        Fp += F; // bought house, add more cookies
    } while (y < X);

    return t;
}

int main()
{
    int T, prob = 1;
    for(cin >> T; T--;)
    {
        printf("Case #%d: %.7lf\n", prob++, solve());
    }
    return 0;
}

