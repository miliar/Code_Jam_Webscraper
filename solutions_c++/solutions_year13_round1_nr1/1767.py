#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll r;

ll a(ll n) {
    return 1 + (n-1) * 4;
}

ll foo(ll n) {
    return 2*n*r + ((1 + a(n)) * n) / 2;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int nt;
    scanf("%d", &nt);
    for (int _ = 1; nt--; ++_) {
        double ans = 0, rr, t;
        scanf("%lf %lf", &rr, &t);
        r = (ll) rr;
        ans = (-(2*rr-1) + sqrt((2*rr-1)*(2*rr-1) + 8*t))/4;
        ll p = (ll) floor(ans);
        while (foo(p) > t) p--;
        printf("Case #%d: %lld\n", _, p);
    }
    return 0;
}
