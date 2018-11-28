#include<iostream>

using namespace std;

#define rep(i, n) for (int i = 0; i < int(n); ++i)

int g[111][111];
int f[111][111];

int main() {
  int t;
  cin >> t;
  rep (iii, t) {
    int n, m;
    cin >> n >> m;
    rep (i, n) rep (j, m) cin >> g[i][j];
    rep (i, n) rep (j, m) f[i][j] = 100;
    rep (i, n) {
      int mx = 0;
      rep (j, m) mx = max(mx, g[i][j]);
      rep (j, m) f[i][j] = min(f[i][j], mx);
    }
    rep (j, m) {
      int mx = 0;
      rep (i, n) mx = max(mx, g[i][j]);
      rep (i, n) f[i][j] = min(f[i][j], mx);
    }
    bool ok = true;
    rep (i, n) rep (j, m) if (g[i][j] != f[i][j]) ok = false;
    cout << "Case #" << iii + 1 << ": " << (ok ? "YES" : "NO") << endl;
  }
  return 0;
}
