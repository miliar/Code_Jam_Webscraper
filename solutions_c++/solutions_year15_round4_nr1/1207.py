// TEMPLATE {{{
#include <bits/stdc++.h>
using namespace std;
#ifndef LOCAL
#define OJ 1
#else
#define OJ 0
#endif
 
#define endl '\n'
#define TIMESTAMP merr << "Execution time: " << (double)clock()/CLOCKS_PER_SEC << " s.\n"
class C_ {}; template <typename T> C_& operator <<(C_& __m, const T& __s) { if (!OJ) cerr << "\E[91m" << __s << "\E[0m"; return __m; }
C_ merr;
 
struct __s { __s() { if (OJ) { ios_base::Init i; cin.sync_with_stdio(0); cin.tie(0); } } ~__s(){ TIMESTAMP; } } __S;
/// END OF TEMPLATE }}}

int n,m;
char A[222][222];

bool ok(int x, int y) {
  int c = A[x][y];
  int dx = 0, dy = 0;
  if (c == '^') {
    dx = -1;
  } else if (c == 'v') {
    dx = 1;
  } else if (c == '<') {
    dy = -1;
  } else {
    dy = 1;
  }
  while (0 <= x+dx && x+dx < n && 0 <= y+dy && y+dy < m) {
    x += dx;
    y += dy;
    if (A[x][y] != '.') return true;
  }
  return false;
}

int main(void) {
  int T;
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
  cin >> T;
  for (int tt = 0; tt < T; tt++) {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
      string s;
      cin >> s;
      for (int j = 0; j < m; j++) {
        A[i][j] = s[j];
      }
    }
    int ans = 0;
    bool ook = true;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (A[i][j] == '.') continue;
        if (ok(i,j)) continue;
        char old = A[i][j];
        ans++;
        if (old != '^') { A[i][j] = '^'; if (ok(i,j)) continue; }
        if (old != 'v') { A[i][j] = 'v'; if (ok(i,j)) continue; }
        if (old != '>') { A[i][j] = '>'; if (ok(i,j)) continue; }
        if (old != '<') { A[i][j] = '<'; if (ok(i,j)) continue; }
        ook = false;
        break;
      }
      if (!ook) break;
    }
    cout << "Case #" << tt+1 << ": ";
    if (ook) {
      cout << ans << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
