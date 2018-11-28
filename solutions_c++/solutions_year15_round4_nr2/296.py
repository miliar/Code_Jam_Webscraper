#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int n;
double x, c;
double v[128], r[128];

void read() {
    scanf("%d%lf%lf", &n, &x, &c);
    for (int i = 0; i < n; i++) {
        scanf("%lf%lf", &v[i], &r[i]);
    }
}

void solve() {
    double ans = 1e100;

    for (int i = 0; i < n; i++) {
        if (fabs(r[i] - c) < 1e-9) {
            ans = min(ans, x / v[i]);
        }
    }

    if (n == 2) {
        if (fabs(r[0] - r[1]) < 1e-9 && fabs(r[0] - c) < 1e-9) {
            ans = min(ans, x / (v[0] + v[1]));
        }

        if (fabs(r[0] - r[1]) > 1e-9) {
            double t1 = x * (c - r[1]) / (v[0] * (r[0] - r[1]));
            double t2 = x * (c - r[0]) / (v[1] * (r[1] - r[0]));

            if (t1 < 1e-9 && t2 < 1e-9) {
                ans = min(ans, max(-t1, -t2));
            }
            if (t1 > -1e-9 && t2 > -1e-9) {
                ans = min(ans, max(t1, t2));
            }
        }
    }

    if (ans < 1e10) {
        printf ("%.9lf\n", ans);
    } else {
        printf ("IMPOSSIBLE\n");
    }
}

int main() {
    int i, cases;
    
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
