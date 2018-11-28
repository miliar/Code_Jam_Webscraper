#include <cstdio>
#include <cstring>
#define MODER 1000002013

using namespace std;

long long n, m;
long long oldpay, newpay;
long long ans;
long long re[1100];

long long min(long long a, long long b) {
    return (a > b) ? b : a;
}

void work() {
    newpay = 0;
    int p;
    for (int i = 1; i <= n; i++) {
        if (re[i] == 0) continue;
        while (re[i] > 0) {
            int j = i + 1;
            while(re[j] > 0) j++;
            p = 1;
            for (int k = i; k < j; k++) re[k] -= p;
            newpay += (n * (j - i) - ((j - i) * (j - i - 1)) / 2) * p;
        }
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    int oi, ei, pi;
    scanf("%d", &t);
    for(int tc = 1; tc <= t; tc++) {
        scanf("%d%d", &n, &m);
        oldpay = 0;
        memset(re, 0, sizeof(re));
        for (int i = 0; i < m; i++) {
            scanf("%d%d%d", &oi, &ei, &pi);
            oldpay += (n * (ei - oi) - ((ei - oi) * (ei - oi - 1)) / 2) * pi;
            for(int j = oi; j < ei; j++) {
                re[j] += pi;
            }
        }
        work();
        ans = oldpay - newpay;
        ans %= MODER;
        while (ans < 0) ans += MODER;
        printf("Case #%d: %d\n", tc, ans);
    }
    return 0;
}


