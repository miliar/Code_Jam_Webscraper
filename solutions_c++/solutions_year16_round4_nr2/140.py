#include <algorithm>
#include <iostream>
#include <valarray>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <complex>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <ctime>
#include <cmath>
#include <queue>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for (int i = (a); i < int(n); ++i)
#define error(x) cout << #x << " = " << (x) << endl;
#define all(n) (n).begin(), (n).end()
#define Size(n) ((int)(n).size())
#define mk make_pair
#define pb push_back

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

template <class P, class Q> void smin(P &a, Q b) { if (b < a) a = b; }
template <class P, class Q> void smax(P &a, Q b) { if (b > a) a = b; }
template <class P, class Q> bool in(const P &a, const Q &b) { return a.find(b) != a.end(); }

const int MAXN = 20;

int n, k;
double dp[MAXN][MAXN];
double probs[MAXN];

double solve(vector<double> p) {
  FOR(i, 0, MAXN) {
    FOR(j, 0, MAXN) {
      dp[i][j] = 0;
    }
  }
  dp[0][0] = 1;
  FOR(i, 0, Size(p)) {
    FOR(j, 0, MAXN - 1) {
      dp[i + 1][j] += p[i] * dp[i][j];
      dp[i + 1][j + 1] += (1 - p[i]) * dp[i][j];
    }
  }
  return dp[k][k / 2];
}

void solve() {
  cin >> n >> k;
  FOR(i, 0, n) {
    cin >> probs[i];
  }
  double best = 0;
  FOR(mask, 0, 1 << n) {
    if (__builtin_popcount(mask) == k) {
      vector<double> p;
      FOR(i, 0, n) {
        if (mask & (1 << i)) {
          p.pb(probs[i]);
        }
      }
      best = max(solve(p), best);
    }
  }
  cout << fixed << setprecision(10) << best << endl;
}

int main() {
  int t;
  cin >> t;
  FOR(test_number, 1, t + 1) {
    cout << "Case #" << test_number << ": ";
    solve();
  }
	return 0;
}
