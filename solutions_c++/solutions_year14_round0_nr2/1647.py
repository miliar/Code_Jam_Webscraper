#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        double c, f, x;
        scanf("%lf%lf%lf", &c, &f, &x);
        double Up = x / c - 2.0 / f - 1;
        int n;
        double per = 2.0, ans = 0.0;
        for (n = 0; n < Up; n++) {
            ans += c / per;
            per += f;
        }
        ans += x / per;
        printf("Case #%d: %.7f\n", cas, ans);
    }
    return 0;
}
