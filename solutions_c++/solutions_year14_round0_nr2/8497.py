#include <cmath>
#include <iostream>
#include <iomanip>

using namespace std;

int fcmp(double a, double b) {
    double diff = a - b;

    if (abs(diff) < 1e-9) {
        return 0;
    } else if (diff > 0) {
        return 1;
    } else {
        return -1;
    }
}

int main(){
    int T;
    double C, F, X, fn, cn, tn, fp, cp, tp, tmin;

    cin >> T;

    for (int t = 0; t < T; t ++ ) {
        cin >> C >> F >> X;

        fn = 2.0;
        cn = C / fn;
        tn = X / fn;
        tmin = tn;

        while (true) {
            cp = cn;
            fp = fn;
            tp = tn;

            fn += F;
            cn += C / fn;
            tn = X / fn + cp;

            if (fcmp(tn, tp) == 1) {
                break;
            }

            if (fcmp(tn, tmin) == -1) {
                tmin = tn;
            }

        }

        cout << "Case #" << t + 1 << ": " << fixed << setprecision(7) << tmin << endl;
    }

    return 0;
}
