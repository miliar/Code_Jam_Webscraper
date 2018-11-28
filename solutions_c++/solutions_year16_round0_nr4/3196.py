#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

long long xpow(long long x, long long y) {
    long long sol = 1;
    for (int i = 0; i < y; i++)
        sol *= x;
    return sol;
}

int main() {
    int t;
    long long k, c, s;
    scanf("%d", &t);

    for (int tc = 1; tc <= t; tc++) {
        printf("Case #%d:", tc);
        scanf("%lld %lld %lld", &k, &c, &s);

        long long x = pow(k, c-1);

        for (int i = 0; i < k; i++) {
            long long y = i;
            printf(" %lld", y*x + 1);
        }
        printf("\n");
    }
    return 0;
}
