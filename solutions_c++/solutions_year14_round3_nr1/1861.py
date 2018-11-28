#include <stdio.h>

using namespace std;

typedef long long ll;

ll euclide(ll a, ll b) {
    while (a && b) {
        if (a > b) a %= b;
        else b %= a;
    }
    return a + b;
}

ll log2(ll i) {
    ll r = 0;
    for (; i >>= 1; r += 1);
    return r;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int T;
    scanf("%d", &T);
    ll P, Q;

    for (int t = 1;t <= T;t++) {
        scanf("%lld/%lld", &P, &Q);
        printf("Case #%d: ", t);
        P *= (1ll << 40);

        ll DBD = euclide(P, Q);

        P /= DBD;
        Q /= DBD;

        if (Q > 1ll) {
            printf("impossible\n");
            continue;
        }

        ll pow = log2(P);

        printf("%lld\n", 40 - pow);
    }

    return 0;
}

