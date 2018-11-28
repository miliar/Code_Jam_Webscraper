#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int t, q = 1;
    double C, F, X, a, b, s, tf, minN;
    cin >> t;
    while(t--) {
        cin >> C >> F >> X;

        tf = 2.0;
        minN = X / tf;
        s = 0.0;
        while(true) {
            a = C / tf;
            b = X / (tf + F);

            if (s+a +b< minN) {
                minN = s + a + b;
            } else {
                printf("Case #%d: %.7lf\n", q++, minN);
                break;
            }

            s += a;
            tf += F;
        }
    }
    return 0;
}
