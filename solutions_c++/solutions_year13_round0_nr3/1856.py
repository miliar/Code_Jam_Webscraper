#include <stdio.h>
#include <algorithm>

int C[10000001];

template <typename T>
bool ispal(T x) {
    T r = 0;
    for (T a = x; a != 0; a /= 10)
        r = 10 * r + a % 10;
    return r == x;
}

void precompute() {
    for (int i = 1; i < sizeof(C) / sizeof(C[0]); i++) {
        if (ispal(i) && ispal((long long)i * i))
            C[i] = C[i - 1] + 1;
        else
            C[i] = C[i - 1];
    }
}

int floor_sqrt(long long n) {
    long long a = 1;
    long long b = n + 1;
    while (a != b) {
        long long mid = (a + b) / 2;
        if (mid <= n / mid)
            a = mid + 1;
        else
            b = mid;
    }
    return (int)a - 1;
}

int ceil_sqrt(long long n) {
    long long a = 1;
    long long b = n + 1;
    while (a != b) {
        long long mid = (a + b) / 2;
        if (mid < n / mid + bool(n % mid))
            a = mid + 1;
        else
            b = mid;
    }
    return (int)b;
}

int solve() {
   long long a, b;
   scanf("%lld %lld", &a, &b);
   return C[floor_sqrt(b)] - C[ceil_sqrt(a) - 1];
}

int main() {
    int n;
    scanf("%d\n", &n);
    precompute();
    for (int i = 1; i <= n; i++)
        printf("Case #%d: %d\n", i, solve());
    return 0;
}
