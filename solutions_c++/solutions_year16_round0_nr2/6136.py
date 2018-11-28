#include <assert.h>
#include <memory.h>
#include <algorithm>
#include <cmath>
#include <cstdio>
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

int dp[111][2];

int main() {
#ifdef LOCAL_HOST
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  FOR(cs, 1, T + 1) {
    string s;
    cin >> s;
    int n = (int)s.size();
    dp[0][0] = dp[0][1] = 0;
    rep(i, n) {
      if (s[i] == '+') {
        dp[i + 1][1] = min(dp[i][1], dp[i][0] + 1);
        dp[i + 1][0] = min(dp[i][1] + 1, dp[i][0] + 2);
      } else {
        dp[i + 1][1] = min(dp[i][1] + 2, dp[i][0] + 1);
        dp[i + 1][0] = min(dp[i][1] + 1, dp[i][0]);
      }
    }
    cout << "Case #" << cs << ": " << dp[n][1] << endl;
  }

  return 0;
}
