#include <bits/stdc++.h>
using namespace std;

using VI = vector<int>;
using VVI = vector<VI>;
using ll = long long;
using VL = vector<ll>;
using VVL = vector<VL>;
using P = pair<int, int>;
using VP = vector<P>;
using VVP = vector<VP>;

using VD = vector<double>;

int n, k;
VD prob, p;

double d[205][205];

double Prob(int i, int l) {
  double &res = d[i][l];
  if (res == res) return res;

  if (i == k) {
    if (l == 0) return res = 1;
    return res = 0;
  }

  res = p[i] * Prob(i + 1, l);
  if (l) res += (1 - p[i]) * Prob(i + 1, l - 1);
  return res;
}

void solve(int cas) {
  cin >> n >> k;
  prob = VD(n);
  for (auto &p : prob) cin >> p;
  sort(prob.begin(), prob.end());

  double res = 0;
  for (int i = 0; i <= k; ++i) {
    p.clear();
    for (int j = 0; j < i; ++j) p.push_back(prob[j]);
    for (int j = n - (k - i); j < n; ++j) p.push_back(prob[j]);
    memset(d, -1, sizeof(d));
    res = max(res, Prob(0, k / 2));
  }
  cout << "Case #" << cas << ": " << res << endl;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.setf(ios::fixed);
  cout.precision(10);

  int t;
  cin >> t;
  for (int z = 1; z <= t; ++z) solve(z);
}
