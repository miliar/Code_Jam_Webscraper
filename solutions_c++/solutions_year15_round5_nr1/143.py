#include <bits/stdc++.h>

using namespace std;

void solve() {
  long long n, d;
  long long s0, as, cs, rs;
  long long m0, am, cm, rm;
  cin >> n >> d;
  cin >> s0 >> as >> cs >> rs;
  cin >> m0 >> am >> cm >> rm;
  vector<long long> s(n);
  vector<long long> m(n);
  vector<vector<long long>> t(n);
  s[0] = s0;
  m[0] = m0;
  for (int i = 0; i < n - 1; ++i) {
    s[i + 1] = (s[i] * as + cs) % rs;
    m[i + 1] = (m[i] * am + cm) % rm;
  }
  for (int i = 1; i < n; ++i) {
    m[i] %= i;
    t[m[i]].emplace_back(i);
  }
  long long res = 0;
  for (int i = 0; i <= 1000; ++i) {
    stack<int> st;
    if (i <= s0 && s0 <= i + d) st.push(0);
    long long r = 0;
    while (!st.empty()) {
      ++r;
      int now = st.top();
      st.pop();
      for (const auto& v : t[now]) {
        if (i <= s[v] && s[v] <= i + d) st.push(v);
      }
    }
    res = max(res, r);
  }
  cout << res;
}

int main() {
  int t;
  cin >> t;
  //#pragma omp parallel for
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
    cout << endl;
  }
}
