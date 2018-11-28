#include <cstdio>
#include <algorithm>
using namespace std;

long long gcd(long long a, long long b) {
    return b == 0 ? a : gcd(b, a%b);
}

int main() {
    int T;
    long long P, Q;

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%lld/%lld", &P, &Q);
        long long mdc = gcd(P, Q);
        P /= mdc, Q /= mdc;
        printf("Case #%d: ", t);
        if (__builtin_popcount(Q) != 1) {
            printf("impossible\n");
            continue;
        }
        int cnt = 0;
        while (P < Q) {
            P <<= 1;
            cnt++;
        }
        printf("%d\n", cnt);
    }
}
