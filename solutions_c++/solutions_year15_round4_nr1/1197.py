#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)

using namespace std;

int di[4] = {-1, 1, 0, 0};
int dj[4] = {0, 0, -1, 1};
char dc[4] = {'^', 'v', '<', '>'};

void solve() {
  int n, m;
  cin >> n >> m;
  vector<string> v(n);
  forn(i, n) cin >> v[i];
  int ans = 0, imp = 0;
  forn(i, n) forn(j, m) if(v[i][j] != '.') {
    int t = find(dc, dc + 4, v[i][j]) - dc;
    assert(t < 4);
    auto fnd = [&](int x, int y, int t) -> bool {
      while (0 <= x && x < n && 0 <= y && y < m) {
        if (v[x][y] != '.') return true;
        x += di[t]; y += dj[t];
      } return false;
    };
    if (!fnd(i + di[t], j + dj[t], t)) {
      bool is_any = false;
      forn(tt, 4) is_any |= fnd(i + di[tt], j + dj[tt], tt);
      if (is_any) {
        ++ans;
      } else {
        ++imp;
      }
    }
  }
  if (imp) cout << "IMPOSSIBLE\n";
  else cout << ans << '\n';
}

int main() {
  int T;
  cin >> T;
  forn(t, T) {
    cout << "Case #" << t + 1 << ": ";
    solve();
  }
  return 0;
}
