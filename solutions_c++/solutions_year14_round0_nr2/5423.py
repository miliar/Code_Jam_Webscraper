#include <cstdio>

double g[100000];
double h[100000];

int main() {
    int T;
    scanf("%d", &T);
    for (int kase = 0; kase < T; ++ kase) {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        double ans = 1E100, tim = 0;
        for (int t = 0; ; ++ t) {
            double tmp = tim + x / (2 + t * f);
            if (tmp < ans) ans = tmp;
            else break;
            tim += c / (2 + t * f);
        }
        printf("Case #%d: %.8lf\n", kase + 1, ans);
    }
    return 0;
}
