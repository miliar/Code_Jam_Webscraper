#include <bits/stdc++.h>
using namespace std;

const double eps = 1e-10;
const double eps2 = 1e-5;
double cmp(double a, double b) {
    return fabs(a - b) < eps ? 0 : a - b;
}

int T, n;
double v, x, r[105], c[105];

int main() {
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d%lf%lf", &n, &v, &x);
        for (int i = 0; i < n; ++i) scanf("%lf%lf", r + i, c + i);
        if (cas == 50) {
            fprintf(stderr, "%d %.4f %.4f\n", n, v, x);
            for (int i = 0; i < n; ++i) fprintf(stderr, "%.4f %.4f\n", r[i], c[i]);
        }
        printf("Case #%d: ", cas);
        if (n == 1) {
            if (fabs(c[0] - x) > eps2) puts("IMPOSSIBLE");
            else {
                double t = v / r[0];
                printf("%.10f\n", t);
            }
        } else if (fabs(c[0] - c[1]) < eps2) {
            if (fabs(c[0] - x) > eps2) puts("IMPOSSIBLE");
            else {
                double t = v / (r[0] + r[1]);
                printf("%.10f\n", t);
            }
            
            if (cas == 50) fprintf(stderr, "case 2\n");
        } else {
            if (cas == 50) fprintf(stderr, "case 3\n");
            double A = r[0], B = r[1];
            double C = r[0] * c[0], D = r[1] * c[1];
            double delta = A * D - B * C;
            double t0 = (D - B * x) * v / delta;
            double t1 = (-C + A * x) * v / delta;
            if (cmp(min(t0, t1), 0) < 0) puts("IMPOSSIBLE");
            else {
                double t = max(t0, t1);
                printf("%.10f\n", t);
            }
        }
    }
}
