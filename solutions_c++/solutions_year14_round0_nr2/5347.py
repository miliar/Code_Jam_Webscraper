#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;

int T;
double c, f, x;

inline int sgn(double x) {
    if (fabs(x) < 1e-10) return 0;
    return x>0?1:-1;
}

double solve(double c, double f, double x) {
    double ans = 0;
    double pro = 2;
    while (1) {
        double t1 = x/pro;
        double t2 = c/pro+x/(pro+f);
        if (t1 <= t2) {
            return ans+t1;
        } else {
            ans += c/pro;
            pro += f;
        }
    }
    return -1;
}

int main() {
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        scanf("%lf%lf%lf", &c, &f, &x);
        printf("Case #%d: ", t);
        double ans = solve(c, f, x);
        assert(ans>0);
        printf("%7f\n", ans);
    }
    return 0;
}
