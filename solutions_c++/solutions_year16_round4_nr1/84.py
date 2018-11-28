#include <bits/stdc++.h>

using namespace std;

struct Initializer {
  Initializer() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    cout << fixed << setprecision(15);
  }
} initializer;

void solve() {
  int n, r, p, s;
  cin >> n >> r >> p >> s;
  int rr = r, pp = p, ss = s;
  vector<vector<string>> v(3), u(3);
  for (int i = 0; i < r; ++i) v[0].emplace_back("R");
  for (int i = 0; i < p; ++i) v[1].emplace_back("P");
  for (int i = 0; i < s; ++i) v[2].emplace_back("S");
  for (int i = 0; i < n; ++i) {
    sort(v[0].rbegin(), v[0].rend());
    sort(v[1].rbegin(), v[1].rend());
    sort(v[2].rbegin(), v[2].rend());
    int r0 = (rr - pp + ss) / 2;
    int p0 = (rr + pp - ss) / 2;
    int s0 =(-rr + pp + ss) / 2;
    if (r0 < 0 || p0 < 0 || s0 < 0) {
      cout << "IMPOSSIBLE";
      return;
    }
    rr = r0;
    pp = p0;
    ss = s0;
    while (r0 | p0 | s0) {
      string rs = "~", ps = "~", ss = "~";
      if (r0) rs = min(v[0].back() + v[2].back(), v[2].back() + v[0].back());
      if (p0) ps = min(v[1].back() + v[0].back(), v[0].back() + v[1].back());
      if (s0) ss = min(v[2].back() + v[1].back(), v[1].back() + v[2].back());
      if (rs < ps && rs < ss) {
        u[0].emplace_back(rs);
        v[0].pop_back();
        v[2].pop_back();
        --r0;
      } else if (ps < ss) {
        u[1].emplace_back(ps);
        v[0].pop_back();
        v[1].pop_back();
        --p0;
      } else {
        u[2].emplace_back(ss);
        v[1].pop_back();
        v[2].pop_back();
        --s0;
      }
    }
    v = move(u);
    u.clear();
    u.resize(3);
  }
  for (int i = 0; i < 3; ++i) if (!v[i].empty()) cout << v[i][0];
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
}
