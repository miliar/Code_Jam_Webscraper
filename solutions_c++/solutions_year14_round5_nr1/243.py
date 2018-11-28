#include <bits/stdc++.h>
using namespace std;

long long sum[1000010];
int a[1000010];

long long cal(int tL, int n, long long val) {
    int L = tL, R = n - 1;
    while (L + 1 < R) {
        int mid = (L + R) / 2;
        if (sum[tL] - sum[mid + 1] <= val) L = mid;
        else R = mid;
    }
    long long tsum = sum[tL], ans = sum[tL];
    for (int i = L - 2; i <= R + 2; i++) {
        if (i >= tL && i < n) {
            ans = min(ans, max(sum[tL] - sum[i + 1], tsum - (sum[tL] - sum[i + 1])));
        }
    }
    return ans;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, p, q, r, s;
        scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
        for (int i = 0; i < n; i++) {
            a[i] = (i * p + q) % r + s;
        }
        sum[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            sum[i] = a[i] + sum[i + 1];
        }
        long long ans = sum[0];
        for (int L = 0; L <= n - 1; L++) {
            long long sum1 = sum[0] - sum[L];
            long long tsum = sum[L];
            long long x1 = tsum / 2, x2 = tsum / 2 + 1;
            long long t1sum2, t1sum3, t2sum2, t2sum3;
            t1sum2 = cal(L, n, x1);
            t2sum2 = cal(L, n, x2);
            t1sum3 = tsum - t1sum2;
            t2sum3 = tsum - t2sum2;
            ans = min(ans, max(max(sum1, t1sum2), t1sum3));
            ans = min(ans, max(max(sum1, t2sum2), t2sum3));
        }
        printf("Case #%d: %.20f\n", cas, (sum[0] - ans) * 1.0 / sum[0]);
    }
    return 0;
}
