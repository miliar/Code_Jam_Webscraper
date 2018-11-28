#include <cstdio>
#include <algorithm>

int T;
double c, f, x;

double solve() {
    double ans = 1e5, v = 2, t = 0;
    for(int i = 0; i <= (int) (1e5); ++i) {
        ans = std::min(ans, x / v + t);
        t += c / v, v += f;
    }
    return ans;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for(int test = 1; test <= T; ++test) {
        scanf("%lf %lf %lf", &c, &f, &x);
        printf("Case #%d: %.7lf\n", test, solve());
    }
    return 0;
}
