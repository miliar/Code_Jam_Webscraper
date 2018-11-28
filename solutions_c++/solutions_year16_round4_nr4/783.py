#include <bits/stdc++.h>

using namespace std;

const int N = 5;

int a[N][N], b[N][N];
int n;

int can[N];
bool dp[N][1 << N];

bool ok() {
    bool has[N];
    memset(has, 0, sizeof has);
    for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j)
        if (b[i][j]) has[j] = true;
    for (int i = 1; i <= n; ++i) if (!has[i]) return false;
    vector<int> p;
    for (int i = 1; i <= n; ++i) p.push_back(i);
    do {
        memset(dp, 0, sizeof dp);
        dp[0][0] = true;
        for (int i = 0; i < n; ++i) for (int mask = 0; mask < (1 << n); ++mask) if (dp[i][mask]) {
            bool got = false;
            for (int j = 1; j <= n; ++j) if (b[p[i]][j] && !(mask >> (j - 1) & 1)) {
                dp[i + 1][mask | (1 << (j - 1))] = true;
                got = true;
            }
            if (!got) return false;
        }
    } while (next_permutation(p.begin(), p.end()));
    return true;
}

int main() {
    //freopen("input.txt", "r", stdin);
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; cin >> ntest;
    for (int it = 1; it <= ntest; ++it) {
        cin >> n;
        for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) {
            char c; cin >> c;
            a[i][j] = c - '0';
        }
        vector<pair<int, int> > C;
        for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j)
            C.push_back(make_pair(i, j));
        int ans = n * n + 1;
        for (int cost = 0; cost <= n * n; ++cost) {
            for (int mask = 0; mask < (1 << C.size()); ++mask) if (__builtin_popcount(mask) == cost) {
                bool fail = false;
                for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) b[i][j] = a[i][j];
                for (int i = 0; i < C.size(); ++i) if (mask >> i & 1) {
                    if (a[C[i].first][C[i].second]) {
                        fail = true;
                        break;
                    }
                    b[C[i].first][C[i].second] = 1;
                }
                if (ok()) {
                    ans = cost;
                    break;
                }
            }
            if (ans != n * n + 1) break;
        }
        cout << "Case #" << it << ": ";
        cout << ans << endl;
    }
    return 0;
}
