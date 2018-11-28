#include <bits/stdc++.h>
#define LL long long
using namespace std;

const int maxn = 1 << 17;

int t;
int N, J;

LL is_prime(LL n) {
    LL tail = sqrt(n + 0.5);
    for (LL i = 2; i <= tail; ++i)
        if (n % i == 0)
            return i;
    return -1;
}

LL calc(int n, int base) {
    LL val = 0;
    LL tmp = 1;
    for (int i = 0; i < N; ++i) {
        if (n >> i & 1) val += tmp;
        tmp *= base;
    }
    return is_prime(val);
}

void output(int n, LL *tmp) {
    for (int i = N - 1; i >= 0; --i)
        printf("%d", n >> i & 1);
    for (int i = 2; i <= 10; ++i)
        printf(" %lld", tmp[i]);
    printf("\n");
}

int main() {
    cin >> t;
    for (int cas = 1; cas <= t; ++cas) {
        printf("Case #%d:\n", cas);
        cin >> N >> J;
        int cnt = 0;
        for (int i = (1 << (N - 1)) + 1; i < (1 << N); i += 2) {
            LL tmp[11];
            bool ok = true;
            for (int j = 2; j <= 10; ++j) {
                tmp[j] = calc(i, j);
                if (tmp[j] == -1) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                ++cnt;
                output(i, tmp);
                if (cnt == J) break;
            }
        }
    }
}
