#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

const double EPS = 1e-5;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        double C, F, X;
        scanf("%lf%lf%lf", &C, &F, &X);

        double ans = 0.0;
        double cookies = 0.0;
        double rate = 2.0;

        while (X - cookies > EPS) {
            ans += C / rate;
            cookies = C;
            if ((X - cookies) / rate < X / (rate + F)) {
                ans += (X - cookies) / rate;
                break;
            } else {
                cookies = 0;
                rate += F;
            }
        }
        printf("Case #%d: %.7lf\n", t, ans);
    }
    return 0;
}
