#include<bits/stdc++.h>

using namespace std;

int f(long long n) {
    long long d = n;
    n = 0;
    int mask = (1 << 10) - 1;
    while (mask) {
        long long temp = n + d;
        while (temp) {
            int t = (1 << (temp % 10));
            if (mask & t) mask ^= t;
            temp /= 10;
        }
        n += d;
    }

    return n;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    long long n;
    cin >> t;
    for (int i=1; i<=t; i++) {
        scanf("%lld", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", i);
        } else {
            printf("Case #%d: %d\n", i, f(n));
        }
    }

    return 0;
}
