#include <stdio.h>

using namespace std;

typedef long long LL;

LL gcd(LL a, LL b) {
    //printf("%lld%lld\n", a, b);
    if (a == 0)
        return b;
    if (b == 0)
        return a;
    if (a >= b)
        return gcd(a - b, b);
    else
        return gcd(b - a, a);
}

void calc(LL p, LL q) {
    //printf("a1\n");
    LL w = gcd(p, q);
    p /= w;
    q /= w;

    //printf("%lld\n", w);

    for (LL qq = q; qq != 1; qq >>= 1) {
        if (qq & 1) {
            printf("impossible\n");
            return;
        }
    }
    //printf("qqq\n");

    int ans = 1;
    while (p * 2 < q) {
        p *= 2;
        ans++;
    }
    printf("%d\n", ans);
    return;
}

int t;

int main() {
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        LL p, q;
        scanf("%lld/%lld", &p, &q);
        //printf("qq\n");
        printf("Case #%d: ", i + 1);
        calc(p, q);
    }


    return 0;
}
