#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

const double eps = 1e-8;

double c, f, x;

bool can(double t) {
    double rate = 2., need = 0.;

    bool ok = false;
    while (need < t) {
        double left = t - need;
        if (rate*left >= x) { ok = true; break; }
        need += c / rate;
        rate += f;
    }

    return ok;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("sol.txt", "w", stdout);

    int test;
    scanf("%d", &test);

    for (int t = 1; t <= test; ++t) {
        scanf("%lf%lf%lf", &c, &f, &x);

        double lo = 0., hi = x/2, sol = 0.;

        while (hi - lo > eps) {
            double mid = (lo + hi) / 2;
            if (can(mid)) hi = mid - eps;
            else { sol = mid; lo = mid + eps; }
        }

        printf("Case #%d: %.7lf\n", t, sol);
    }

    return 0;
}
