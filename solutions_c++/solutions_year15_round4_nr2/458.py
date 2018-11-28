#include <bits/stdc++.h>

using namespace std;

const int MAXN = 101;
const double GG = -1;
const double eps = 1e-6;

double jizz() {
    int n; scanf("%d", &n);
    double V, X;
    scanf("%lf%lf", &V, &X);

    double rs[MAXN], cs[MAXN];

    for (int i = 0; i < n; ++i)
        scanf("%lf%lf", &rs[i], &cs[i]);

    if (n == 2 and abs(cs[0] - cs[1]) < eps)
        n = 1, rs[0] = rs[0] + rs[1];

    if (n == 1) {
        if (abs(X - cs[0]) > eps)
            return GG;

        return V / rs[0];
    }

    if (n == 2) {
        if (cs[0] > cs[1]) {
            swap(rs[0], rs[1]);
            swap(cs[0], cs[1]);
        }

        if (not (cs[0] <= X and X <= cs[1]))
            return GG;

        double VC = V * X;
        double t0 = (V*cs[1] - VC) / (cs[1] - cs[0]) / rs[0];
        double t1 = (VC - V*cs[0]) / (cs[1] - cs[0]) / rs[1];

        return max(t0, t1);
    }

    assert (false);
    return GG;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        double ans = jizz();
        if (ans < -0.5)
            puts("IMPOSSIBLE");
        else
            printf("%.8f\n", ans);
    }

    return 0;
}
