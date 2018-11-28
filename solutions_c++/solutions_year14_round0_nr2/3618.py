#include <cstdio>

double solve(double c, double f, double x) {
    double ans = 1e10, tot = 0, v = 2;
    for (; ans > tot; v += f) {
        double now = tot + x / v;
        if (now < ans) ans = now;
        tot += c / v;
    }
    return ans;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int i = 1; i <= cas; ++i) {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        printf("Case #%d: %.7f\n", i, solve(c, f, x));
    }
    return 0;
}
