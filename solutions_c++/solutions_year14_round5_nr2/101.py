#include <bits/stdc++.h>

using namespace std;

#define long int64_t

#define rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=a;i<(b);++i)
#define all(u) begin(u),end(u)
#define rall(u) (u).rbegin(),(u).rend()
#define uniq(u) (u).erase(unique(all(u)),end(u))

#define mp make_pair
#define pb push_back
#define eb emplace_back

const int N = 128;

int p, q, n, h[N], g[N];

void input()
{
    cin >> p >> q >> n;
    rep(i, n) cin >> h[i] >> g[i];
}

int mod[N], need[N], tower[N];

void prepare()
{
    rep(i, n) {
        mod[i] = (h[i] - 1) % q + 1;
        need[i] = max(0, mod[i] - 1) / p;
        tower[i] = (h[i] + q - 1) / q;
        // cerr << mod[i] << ' ' << need[i] << ' ' << tower[i] << endl;
    }
}

const int M = 10000;

int mmm = -1;
long dp[N][M] = {};

void solve()
{
    prepare();

    memset(dp, -1, sizeof(dp));
    dp[0][1] = 0;

    rep(i, n) rep(j, M) if (dp[i][j] >= 0) {
        mmm = max(mmm, j);
        dp[i + 1][j + tower[i]] = max(dp[i + 1][j + tower[i]], dp[i][j]);
        // cerr << i + 1 << ' ' << j + tower[i] << " << " << dp[i][j] << endl;

        const int dj = (h[i] - need[i] * p - 1) / q - need[i] - 1;
        if (j + dj >= 0) {
            dp[i + 1][j + dj] = max(dp[i + 1][j + dj], dp[i][j] + g[i]);
            // cerr << i + 1 << ' ' << j + dj << " << " << dp[i + 1][j + dj] << " << " << i << ' ' << j << endl;
        }
    }
    long ans = 0;
    rep(j, M) ans = max(ans, dp[n][j]);
    cout << ans << endl;
}

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    rep(i, T) {
        input();

        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    cerr << mmm << endl;

    return 0;
}
