#include <cstdio>
#include <algorithm>
using namespace std;

long long p, q;

long long gcd(long long a, long long b) {
    return b == 0 ? a : gcd(b, a%b);
}

int solve(long long p, long long q) {
    if (p == q)
        return 0;
    long long d = gcd(p, q);
    p /= d;
    q /= d;
    return solve(min(p, q/2), q/2) + 1;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        scanf("%lld/%lld", &p, &q);
        long long d = gcd(p, q);
        p /= d;
        q /= d;
        long long b = 1;
        while (b < q)
            b <<= 1;
        if (b != q) {
            puts("impossible");
            continue;
        }
        printf("%d\n", solve(p, q));
    }
}
