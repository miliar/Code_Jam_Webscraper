#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef vector<int> Vi;
typedef vector<Vi> Mi;

const int INF = 1000000000;

int N, P, Q;
Vi H, G;
Mi dp;

int fun(int m, int t) {
  if (m == N) return 0;
  if (dp[m][t] != -1) return dp[m][t];
  int res = fun(m + 1, t + (H[m] + Q - 1)/Q);
  int q = (H[m] - 1)/Q;
  int r = (H[m] - q*Q + P - 1)/P;
  if (r <= t + q) res = max(res, G[m] + fun(m + 1, t + q - r));
  return dp[m][t] = res;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cin >> P >> Q >> N;
    H = G = Vi(N);
    for (int i = 0; i < N; ++i) cin >> H[i] >> G[i];
    dp = Mi(N, Vi(20*N + 20, -1));
    int res = fun(0, 1);
    cout << "Case #" << cas << ": " << res << endl;
  }
}
