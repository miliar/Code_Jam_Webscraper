#include <cstdio>
#include <cmath>
using namespace std;

int main() {
    int T;
    long long r, t;

    scanf("%d", &T);
    for (int c = 1; c <= T; c++) {
        scanf("%lld %lld", &r, &t);
        long long a0 = 2*r + 1;
        long long lo = 1, hi = 1000000000;
        while (lo < hi) {
            long long mid = (lo + hi + 1) >> 1;
            if (log10(mid) + log10(a0) >= 18) {
                hi = mid-1;
                continue;
            }
            long long sum = mid*(a0 + 2*(mid-1));
            if (sum > t)
                hi = mid-1;
            else
                lo = mid;
        }
        printf("Case #%d: %lld\n", c, lo);
    }
}
