#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);

    for (int i = 1; i <= T; ++i) {
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);

        double rate = 2.0;
        double time = 0.0;

        bool found = false;
        while (!found) {
            double winTime = X/rate;
            double farmTime = C/rate;
            double nextWinTime = X/(rate+F);

            if (farmTime + nextWinTime < winTime) {
                rate += F;
                time += farmTime;
            } else {
                time += winTime;
                found = true;
            }
        }

        printf("Case #%d: %.7lf\n", i, time);
    }

    return 0;
}