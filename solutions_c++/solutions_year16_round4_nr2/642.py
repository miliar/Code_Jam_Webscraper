#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")

#include <bits/stdc++.h>

#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(), v.end()

using namespace std;
using ll = int64_t;

double tie_prob(vector<double> cprobs) {
  using ld = long double;
  int n = cprobs.size();
  assert(n % 2 == 0);
  vector<vector<ld>> d(n + 1, vector<ld>(n + 1));
  d[0][0] = 1.0;
  for (double p : cprobs) {
    for (int i = n - 1; i >= 0; i--) {
      for (int j = n - 1; j >= 0; j--) {
        d[i + 1][j] += d[i][j] * p;
        d[i][j + 1] += d[i][j] * (1.0 - p);
      }
    }
  }
  return d[n / 2][n / 2];
}

void solve() {
  int n, k;
  cin >> n >> k;

  vector<double> probs(n);
  for (int i = 0; i < n; i++)
    cin >> probs[i];
  sort(all(probs));

  double res = 0.0;

  for (int p = 0; p <= k; p++) {
    int s = k - p;
    vector<double> cprobs;
    for (int i = 0; i < p; i++) {
      cprobs.pb(probs[i]);
    }
    for (int i = 0; i < s; i++) {
      cprobs.pb(probs[n - i - 1]);
    }
    res = max(res, tie_prob(cprobs));
  }

  cout << setprecision(10) << res << endl;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;

  for (int test = 1; test <= tests; test++) {
    cout << "Case #" << test << ": ";
    solve();
  }

  return 0;
}
