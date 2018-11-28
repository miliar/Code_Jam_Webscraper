#include <iostream>
#include <cstdio>
#include <cstring>

#define INF 1e16

using namespace std;

double solve(double c, double f, double x) {
    int i;
    double t = 0, v = 2.0, ret = INF;

    for (i = 0; ; ++i) {
        ret = min(ret, t + x / v);
        t += c / v; v += f;
        if (t >= ret) break;
    }

    return ret;
}

int main() {
    double c, f, x;
    int t, ct = 0;

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%lf%lf%lf", &c, &f, &x);
        printf("Case #%d: %.7f\n", ++ct, solve(c, f, x));
    }

    return 0;
}
