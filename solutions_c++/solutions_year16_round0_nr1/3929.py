#include <cstdio>
#include <cstdlib>
#include <cstring>

int T, N;
int digits[10];

void fill(int n) {
    while (n > 0) {
        digits[n % 10] = 1;
        n /= 10;
    }
}

int full() {
    for (int i = 0; i < 10; i++) {
        if (!digits[i]) {
            return 0;
        }
    }
    return 1;
}

long long solve() {
    memset(digits, 0, sizeof(digits));
    for (int i = 0; i < 10000000; i++) {
        long long n = N * i;
        fill(n);
        if (full()) {
            return n;
        }
    }
    return -1;
}

int main() {
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d", &N);

        int ans = solve();
        if (ans != -1) {
            printf("Case #%d: %d\n", t, ans);
        } else {
            printf("Case #%d: INSOMNIA\n", t);
        }
    }
    return 0;
}
