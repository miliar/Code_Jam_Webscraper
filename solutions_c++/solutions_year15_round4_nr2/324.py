#include <bits/stdc++.h>
using namespace std;
const double EPS = 1e-10;

int N;
double V, X;
double a, b, c, d, e, f, g, h;
double r[1000], x[1000];

inline int dblcmp(double x) {
    if (fabs(x) < EPS) {
        return 0;
    }
    return x < 0 ? -1 : 1;
}

inline int dblcmp(double x, double y) {
    return dblcmp(x - y);
}

bool judge(double t) {
    double a = V - g * t, b = X;
    if (dblcmp(a) < 0) {
        return false;
    }
    double cc = c * t, dd = d * t;
    double dc = 0;
    if (dblcmp(cc) > 0) {
        dc = dd / cc;
    }
    return false;

}

int main() {
    int T;
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &N);
        scanf("%lf%lf", &V, &X);
        for (int i = 0; i < N; ++i) {
            scanf("%lf%lf",&r[i],&x[i]);
        }
        a = V;
        b = X;
        for (int i=0; i < N; ++i) {
            auto tt = r[i] * x[i];
            if (dblcmp(x[i], X) > 0) {
                f += tt;
                e += r[i];
            } else if (dblcmp(x[i], X) < 0) {
                d += tt;
                c += r[i];
            } else {
                h += tt;
                g += r[i];
            }
        }
        double l = 0.0, r = 1e16;
        while (dblcmp(l, r) < 0) {
            double mid = (l + r) * 0.5;
            if (judge(mid)) {
                r = mid;
            } else {
                l = mid;
            }
        }
        double ans = (l + r) * 0.5;
        printf("Case #%d: ", t);
        if (ans < 1e8) {
            printf("%.7f\n", ans);
        } else {
            puts("IMPOSSIBLE\n");
        }
    }
    return 0;
}
