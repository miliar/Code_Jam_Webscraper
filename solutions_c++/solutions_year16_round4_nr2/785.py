#include <bits/stdc++.h>
using namespace std;

typedef long double ld;
const int MAXN = 210;

int t, n, k;
ld arr[MAXN], dp[MAXN][MAXN], p[MAXN], ans = 0;

void check() {
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1 - p[0];
    dp[0][1] = p[0];
    for (int j = 1; j < k; j++) {
        for (int h = 0; h <= j + 1; h++) {
            if (h == 0) dp[j][h] = (1 - p[j]) * dp[j - 1][h];
            else dp[j][h] = p[j] * dp[j - 1][h - 1] + (1 - p[j]) * dp[j - 1][h];
        }
    }
    ans = max(ans, dp[k - 1][k / 2]);
}

void recur(int i, int ind) {
    if (ind == k) {
        check();
        return ;
    }
    if (i == n && ind < k) return ;
    recur(i + 1, ind);
    p[ind] = arr[i];
    recur(i + 1, ind + 1);
}

int main(void) {
    if (fopen("b-small.in", "r")) {
        freopen("b-small.in", "r", stdin);
        freopen("b-small.out", "w", stdout);
    }
    if (fopen("b-large.in", "r")) {
        freopen("b-large.in", "r", stdin);
        freopen("b-large.out", "w", stdout);
    }
    cin >> t;
    for (int ii = 1; ii <= t; ii++) {
        ans = 0;
        cin >> n >> k;
        for (int i = 0; i < n; i++) cin >> arr[i];
        sort(arr, arr + n);
        recur(0, 0);
        printf("Case #%d: %.12f\n", ii, (double)ans);
    }
    return 0;
}
