#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

#define MAXN 2
int n;
ld V, T;
ld R[MAXN], C[MAXN];
ld solve() {
  cin >> n >> V >> T;
  for (int i = 0; i < n; ++i)
    cin >> R[i] >> C[i];
  if (n == 1) {
    return C[0] == T ? V / R[0] : -1;
  } else if (n == 2) {
    if (max(C[0], C[1]) < T)
      return -1;
    if (C[0] == C[1])
      return V / (R[0] + R[1]);
    double t[2];
    for (int i = 0; i < 2; ++i)
      t[i] = V * (T - C[1-i]) / (R[i] * (C[i] - C[1-i]));
    if (min(t[0], t[1]) < 0)
      return -1;
    return max(t[0], t[1]);
  }
  return -1;
}

int main() {
  ios::sync_with_stdio(0);
  int tc;
  cin >> tc;
  cout << fixed << setprecision(8);
  for (int cs = 1; cs <= tc; ++cs) {
    cout << "Case #" << cs << ": ";
    ld ans = solve();
    if (ans >= 0)
      cout << ans;
    else
      cout << "IMPOSSIBLE";
    cout << endl;
  }
  return 0;
}

