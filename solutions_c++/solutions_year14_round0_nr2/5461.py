#include <iostream>
#include <iomanip>

using namespace std;

void print(int c, long double ans) {
    cout << fixed << "Case #" << c << ": " << setprecision(7) << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;
    for (int cn = 1; cn <= t; cn++) {
        long double C, F, X;
        cin >> C >> F >> X;

        if (X <= C) {
            print(cn, X / 2);
            continue;
        }

        long double r, t, c;
        r = 2;
        t = C / 2;
        c = C;

        while (c < X) {
            long double tc, tb;

            tc = (X - C) / r;
            tb = X / (r + F);

            if (tc <= tb) {
                t += tc;
                break;
            }
            else {
                c = 0;
                r += F;
                t += (C / r);
            }
        }
        print(cn, t);
    }
    return 0;
}

