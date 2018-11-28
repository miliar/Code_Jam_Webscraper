#include <bits/stdc++.h>
using namespace std;
const int maxn = 205;

bool vis[maxn];
int n, m;
double a[maxn], dp[maxn], old[maxn];

void solve() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a + n);

    double res = -1;
    for (int pref = 0; pref <= m; pref++) {
        vector<double> c;
        for (int i = 0; i < pref; i++) {
           c.push_back(a[i]);
        }
        for (int i = 0; i < m - pref; i++) {
            c.push_back(a[n - 1 - i]);
        }

        memset(old, 0, sizeof(old));
        old[0] = 1;
        for (double p : c) {
            dp[0] = p * old[0];
            for (int i = 1; i <= m / 2; i++) {
                dp[i] = p * old[i] + (1 - p) * old[i - 1];
            }
            memcpy(old, dp, sizeof(old));
        }

        res = max(old[m / 2], res);
    }

    cout << fixed << setprecision(9) << res;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
    }
    return 0;
}
