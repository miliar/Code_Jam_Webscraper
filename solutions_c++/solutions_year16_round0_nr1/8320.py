#include <bits/stdc++.h>
using namespace std;


int n_test;
long long n;

int mask(long long n) {
    int res = 0;
    while (n > 0) {
        res |= 1 << (n % 10);
        n /= 10;
    }
    return res;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &n_test);
    for (int test = 1; test <= n_test; ++test) {
        scanf("%lld", &n);
        printf("Case #%d: ", test);
        if (n == 0) printf("INSOMNIA\n");
        else {
            long long m = 0;
            int state = 0;
            do {
                m += n;
                state |= mask(m);
            } while (state != 0x3ff);
            printf("%lld\n", m);
        }
    }

    return 0;
}