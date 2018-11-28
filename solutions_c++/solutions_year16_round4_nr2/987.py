#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using VI = vector<int>;
using VLL = vector<ll>;
using LD = long double;
using VLD = vector<LD>;

const int maxn = 16;
LD memo[maxn][maxn/2][maxn/2];
VLD v;
int vpos[maxn];
int N;
LD f(int n, int yes, int no) {
  if (!(yes|no)) return 1.0;
  LD &ans = memo[n][yes][no];
  if (ans == ans) return ans;
  int ri = vpos[n];
  ans = 0;
  if (yes) ans += v[ri] * f(n+1, yes-1, no);
  if (no) ans += (1.0-v[ri])*f(n+1, yes, no-1);
  return ans;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int T; cin >> T;
  for (int ncase = 1; ncase <= T; ++ncase) {
    int k, n; cin >> n >> k;
    v.resize(n);
    for (int i = 0; i < n; ++i) {
      cin >> v[i];
    }
    LD ans = 0.0;
    for (int m = (1<<k)-1; m < (1<<n); ++m) {
      if (__builtin_popcount(m) != k) continue;
      memset(memo, -1, sizeof memo);
      int ind = 0;
      for (int j = 0; j < n; ++j) {
        if (m & (1<<j)) vpos[ind++] = j;
      }
      ans = max(ans, f(0, k/2, k/2));
    }

    cout.precision(9);
    cout << "Case #" << ncase << ": " << fixed << ans << endl;
  }
}
