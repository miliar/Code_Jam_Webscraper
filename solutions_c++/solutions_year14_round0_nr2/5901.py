#include <cstdio>

int cmp_double(double a, double b, double eps=1e-8) {
    return a + eps > b ? b + eps > a ? 0 : 1 : -1;
}

int main() {
    int T;
    double c, f, x;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%lf %lf %lf", &c, &f, &x);
        double r = 2, tm = 0;
        while (1) {
            double cur = tm + x / r;
            double buy = tm + c / r + x / (r + f);
            if (cur <= buy) {
                tm += x / r;
                break;
            }
            tm += c / r;
            r += f;
        }
        printf("Case #%d: %.7lf\n", t, tm);
    }
}
