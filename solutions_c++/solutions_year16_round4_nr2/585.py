#include <assert.h>
#include <memory.h>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define pb push_back
#define INF 1011111111
#define FOR(i, a, b) for (int _n(b), i(a); i < _n; i++)
#define rep(i, n) FOR(i, 0, n)
#define CL(a, v) memset((a), (v), sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int, int> pii;

/*** TEMPLATE CODE ENDS HERE */

const int N = 202;
double p[N];

double dp[N][N][N];
bool seen[N][N][N];

int n, K;

double F(int i, int k, int y) {
  if (i == n) {
    if (k == K && y * 2 == K) {
      return 1;
    } else {
      return 0;
    }
  }
  if (k > K || 2 * y > K) return -1e20;

  if (seen[i][k][y]) {
    return dp[i][k][y];
  }
  double &ans = dp[i][k][y];
  seen[i][k][y] = true;
  ans = F(i + 1, k, y);

  double ret = F(i + 1, k + 1, y + 1) * p[i] + F(i + 1, k + 1, y) * (1 - p[i]);

  return ans = max(ans, ret);
}

double q[N];
double dp2[N][N];

double solve2(int n) {
  CL(dp2, 0);
  dp2[0][0] = 1;
  rep(k, n) rep(y, n / 2 + 1) {
    dp2[k + 1][y + 1] += dp2[k][y] * q[k];
    dp2[k + 1][y] += dp2[k][y] * (1 - q[k]);
  }
  return dp2[n][n / 2];
}

void solve() {
  cin >> n >> K;
  rep(i, n) cin >> p[i];
  sort(p, p + n);

  double ans = -1e20;
  rep(i, n) FOR(j, i, n) {
    if (i + 1 + n - j == K) {
      int w = 0;
      rep(t, i + 1) q[w++] = p[t];
      FOR(t, j, n) q[w++] = p[t];
      double ret = solve2(K);
      ans = max(ans, ret);
    }
  }
  for (int i = 0; i + K <= n; ++i) {
    rep(j, K) q[j] = p[i + j];
    double ret = solve2(K);
    ans = max(ans, ret);
  }

  //  CL(dp, 0);
  //  CL(seen, 0);

  //  dp[0][0][0] = 1;
  //  rep(i, n) rep(k, K + 1) rep(y, min(i, k) + 1) {
  //    dp[i + 1][k][y] = max(dp[i + 1][k][y], dp[i][k][y]);
  //
  //    dp[i + 1][k + 1][y + 1] += dp[i][k][y] * p[i];
  //    dp[i + 1][k + 1][y] += dp[i][k][y] * (1 - p[i]);
  //  }

  //  double ans = F(0, 0, 0);

  cout.precision(9);
  cout << fixed << ans;

  //  cout << fixed << dp[n][K][K / 2];
}

int main() {
#ifdef LOCAL_HOST
  //  freopen("input.txt", "r", stdin);
  freopen("B-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  FOR(tt, 1, T + 1) {
    cout << "Case #" << tt << ": ";
    solve();
    cout << endl;
  }

  return 0;
}
