#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int n, k;
long double p[16], dp[20][20];
long double ans;
bool b[16];

void try_to_pick(int lv, int cnt) {
    if (lv == n) {
        if (cnt == k) {
            int m = k / 2;
            vector<long double> v;
            for (int i = 0; i < n; i++)
                if (b[i])
                    v.push_back(p[i]);

            memset(dp, 0, sizeof dp);
            dp[0][0] = 1.0;
            for (int i = 1; i <= k; i++)
                for (int j = 0; j < i; j++) {
                    dp[i][j+1] += dp[i-1][j] * v[i-1];
                    dp[i][j] += dp[i-1][j] * (1.0 - v[i-1]);
                }

            if (dp[k][m] > ans)
                ans = dp[k][m];
        }
        return;
    }
    b[lv] = 1;
    try_to_pick(lv+1, cnt+1);
    b[lv] = 0;
    try_to_pick(lv+1, cnt);
}

int main() {
    int t;

    ios::sync_with_stdio(0);

    cin >> t;
    for (int case_no = 1; case_no <= t; case_no++) {
        cin >> n >> k;
        for (int i = 0; i < n; i++)
            cin >> p[i];
        
        ans = 0.0;
        memset(b, 0, sizeof b);
        try_to_pick(0, 0);

        cout << fixed << setprecision(12) << "Case #" << case_no << ": " << ans << endl;
    }

    return 0;
}