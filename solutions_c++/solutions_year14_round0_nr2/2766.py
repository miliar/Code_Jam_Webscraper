#include <cstdio>
using namespace std;

int main() {
    int T;
    double C, F, X;

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%lf %lf %lf", &C, &F, &X);
        double ans = 0, rate = 2;
        while (1) {
            if (X/rate <= C/rate + X/(rate+F)) {
                ans += X/rate;
                break;
            } else {
                ans += C/rate;
                rate += F;
            }
        }
        printf("Case #%d: %.7lf\n", t, ans);
    }
}
