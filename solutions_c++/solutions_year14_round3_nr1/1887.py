#include <cstdio>

using namespace std;

typedef long long ll;

ll gcd(ll a, ll b) {
    return b == 0 ? a : gcd(b, a % b);
}

int minGens(ll p, ll q) {
    if (p == q || p == 0) {
        return 0;
    }

    ll g = gcd(p, q);
    p /= g;
    q /= g;

    if (__builtin_popcount(q) != 1) {
        return -1;
    }

    int gen = 1;
    while (p < q / 2) {
        p *= 2;
        gen++;
    }

    int g2 = minGens(p - q/2, q);
    if (g2 == -1 || g2 + gen > 40) {
        return -1;
    }

    return gen;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        ll p, q, g;
        scanf("%lld/%lld", &p, &q);
        printf("Case #%d: ", t);

        int gen = minGens(p, q);
        if (gen == -1) {
            printf("impossible\n");
        } else {
            printf("%d\n", gen);
        }
    }

    return 0;
}
