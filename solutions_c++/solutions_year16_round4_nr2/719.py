#include <bits/stdc++.h>
#define vec vector
#define sz(c) int(c.size())
#define FOR(i, a, b) for (int i = a; i < (b); ++i)
#define DOWN(i, a, b) for(int i = (a) - 1; i >= (b); --i)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vec<int> vi;

double calc(const vec<double> &p) {
  int n = sz(p);
  int m = n / 2;
  vec<vec<vec<double>>> dp(n + 1, vec<vec<double>>(m + 1, vec<double>(m + 1)));
  dp[0][0][0] = 1;
  FOR(i, 0, n) {
    FOR(j, 0, min(i + 1, m + 1)) {
      FOR(k, 0, min(i + 1, m + 1)) {
        if (j + 1 <= m) dp[i + 1][j + 1][k] += dp[i][j][k] * p[i];
        if (k + 1 <= m) dp[i + 1][j][k + 1] += dp[i][j][k] * (1 - p[i]);
      }
    }
  }
  return dp[n][m][m];
}

void solve(int testcase) {
  cout << "Case #" << testcase << ": ";
  int n, K;
  cin >> n >> K;
  vec<double> p(n);
  FOR(i, 0, n) cin >> p[i];

  double res = 0;
  FOR(i, 0, 1<<n) {
    if (__builtin_popcount(i) == K) {
      vec<double> tmp;
      tmp.reserve(K);
      FOR(j, 0, n) {
        if (i>>j&1) tmp.push_back(p[j]);
      }
      res = max(res, calc(tmp));
    }
  }
  cout << res << endl;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << setprecision(10) << fixed;

  int testcases;
  cin >> testcases;
  FOR(testcase, 1, testcases + 1) {
    cerr << "Case " << testcase << "/" << testcases << endl;
    solve(testcase);
  }

  return 0;
}
