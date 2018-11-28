#include <stdio.h>
#include <string.h>
#include <stdlib.h>
const double eps = 1e-6;
void solve() {
    double C, F, X;
    scanf("%lf%lf%lf", &C, &F, &X);
    double ans = 1e100, t = 0;
    for (int i = 0; i * C < X + eps; ++i) {
        double tmp = t + X / (2 + F * i);
        if (tmp < ans) ans = tmp;
        t += C / (2 + F * i);
    }
    printf("%.10f\n", ans);
    return;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        printf("Case #%d: ", t + 1);
        solve();
    }
}
