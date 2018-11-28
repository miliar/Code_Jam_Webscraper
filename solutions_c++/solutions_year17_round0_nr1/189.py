#include <bits/stdc++.h>
#define SZ(x) ((int) (x).size())
using namespace std;

typedef long long i64;

void solve() {
    string s;
    cin >> s;
    int n = SZ(s);
    int k;
    cin >> k;
    vector<int> flip(n + 3, 0);
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        int sign = s[i] == '-';
        sign ^= flip[i];
        if (sign == 1) {
            if (i + k <= n) {
                flip[i + 1] ^= 1;
                flip[i + k] ^= 1;
                ans++;
            } else {
                cout << "IMPOSSIBLE\n";
                return;
            }
        }
        flip[i + 1] ^= flip[i];
    }
    cout << ans << '\n';
}

int main() {
    #ifdef LOCAL_RUN
    freopen("task.in", "r", stdin);
    freopen("task.out", "w", stdout);
    //freopen("task.err", "w", stderr);
    #endif // ONLINE_JUDGE
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
