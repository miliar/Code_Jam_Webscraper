#include <bits/stdc++.h>
using namespace std;

const int MAX = 1005;

int nTests, n, k;
int a[MAX], dp[MAX][MAX];

int cal(int i, int x) {
    if (i > n) return 0;
    int &res = dp[i][x];
    if (res >= 0) return res;
    res = max(a[i], cal(i + 1, x));
    for (int j = 1; j < a[i] && j <= x; ++j) {
        int t = (a[i] + j) / (j + 1);
        res = min(res, max(cal(i + 1, x - j), t));
    }
    return res;
}

int main() {
    //freopen("B.txt", "r", stdin);
    freopen("B-small-attempt5.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> nTests;
    for (int test = 1; test <= nTests; ++test) {
        cin >> n;
        k = 0;
        for (int i = 1; i <= n; ++i) {
            cin >> a[i];
            k += (a[i] - 1);
        }

        memset(dp, -1, sizeof dp);
        int res = accumulate(a + 1, a + n + 1, 0);
        for (int i = 0; i <= k; ++i) {
            res = min(res, i + cal(1, i));
        }

        cout << "Case #" << test << ": " << res << endl;
    }
}

