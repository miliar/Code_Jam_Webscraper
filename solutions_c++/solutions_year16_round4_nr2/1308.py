#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <tuple>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>

using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-12;
static const double PI = acos(-1.0);

#define FOR(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define ALL(a) (a).begin(), (a).end()
#define DEBUG(x) cout << #x << ": " << x << endl

double dp[32][32];

double solve() {
  int N;
  int K;
  cin >> N >> K;
  vector<double> p(N);
  REP(i, N) {
    cin >> p[i];
  }
  double max_ = 0;
  REP(i, 1 << N) {
    vector<int> v;
    REP(j, N) {
      if (i & (1 << j)) {
        v.push_back(j);
      }
    }
    if ((int)v.size() != K) {
      continue;
    }
    REP(x, K + 1) {
      REP(y, K + 1) {
        dp[x][y] = 0;
      }
    }
    dp[0][0] = 1;
    // REP(j, K) {
    //   std::cout << p[v[j]] << " ";
    // }
    // std::cout << std::endl;
    REP(j, K) {
      REP(k, j + 2) {
        int x = k;
        int y = j - k + 1;
        if (0 <= x - 1) {
          dp[x][y] += dp[x - 1][y] * p[v[j]];
        }
        if (0 <= y - 1) {
          dp[x][y] += dp[x][y - 1] * (1 - p[v[j]]);
        }
      }
      // REP(x, K + 1) {
      //   REP(y, K + 1) {
      //     std::cout << dp[x][y] << " ";
      //   }
      //   std::cout << std::endl;
      // }
      // std::cout << std::endl;
    }
    // std::cout << K / 2 << std::endl;
    // std::cout << dp[K / 2][K / 2] << std::endl;
    max_ = max(max_, dp[K / 2][K / 2]);
  }
  return max_;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    printf("Case #%d: %0.8f\n", i + 1,  solve());
  }
  return 0;
}
