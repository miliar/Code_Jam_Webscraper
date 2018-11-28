#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

const int MAXN = 1001;

int dp[MAXN][MAXN];
vector<int> cost_left, cost_right;

int doit(int l, int r){
    if (dp[l][r] == -1) {
        if (l == 0 && r == 0)
            dp[l][r] = 0;
        else {
            int ans = MAXN * MAXN;

            if (l > 0)
                ans = min(ans, cost_left[l+r-1] + doit(l - 1, r));
            if (r > 0)
                ans = min(ans, cost_right[l+r-1] + doit(l, r - 1));

            dp[l][r] = ans;
        }
    }

    return dp[l][r];
}

int main() {
    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        int n;
        cin >> n;

        vector<int> v(n);

        for (int i = 0; i < n; i++)
            cin >> v[i];

        cost_left.clear();
        cost_right.clear();
        cost_left.resize(n);
        cost_right.resize(n);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (v[j] > v[i]) {
                    if (i < j)
                        cost_left[i]++;
                    else
                        cost_right[i]++;
                }
            }
        }

        memset(dp, -1, sizeof dp);

        int ans = n*n;

        for (int l = 0; l <= n; l++) {
            ans = min(ans, doit(l, n - l));
        }

        cout << "Case #" << tc << ": " << ans << '\n';
    }

    return 0;
}
