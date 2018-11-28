#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fornn(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

typedef long long i64;
typedef pair<i64, i64> pi64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;

int h[200], g[200];
int dh[200];
int dp[200][2000];

int main() {
#ifdef LOCAL_DEFINE
//    freopen("input.txt", "rt", stdin);
//    freopen("output.txt", "wt", stdout);
#endif
    
    int T;
    cin >> T;
    forn(t, T) {
        int P, Q, N;
        cin >> P >> Q >> N;
        forn(i, N) cin >> h[i] >> g[i];
        forn(i, N + 1) forn(j, 10 * N + 1) dp[i][j] = -1e9;
        dp[0][1] = 0;
        forn(i, N) {
            forn(j, 10 * N + 1) {
                if (dp[i][j] < 0) continue;
                dp[i + 1][j + (h[i] + Q - 1) / Q] = max(dp[i + 1][j + (h[i] + Q - 1) / Q], dp[i][j]);
//                for (int p = 1; (p - 1) * P < h[i]; ++p) {
                for (int q = 0; (q - 1) * Q < h[i]; ++q) {
                    int p = q * Q >= h[i] ? 0 : (h[i] - q * Q + P - 1) / P;
                    if (p == 0 || p > j + q) continue;
                    dp[i + 1][j + q - p] = max(dp[i + 1][j + q - p], dp[i][j] + g[i]);
                }
            }
        }
        int ans = 0;
        forn(i, 10 * N + 1) ans = max(ans, dp[N][i]);
        cout << "Case #" << t + 1 << ": " << ans << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
