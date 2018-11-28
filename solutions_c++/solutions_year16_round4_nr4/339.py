#include <bits/stdc++.h>

using namespace std;

#define FOR(i, n) for (int i = 0; i < n; ++i)

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef map<int, int> mii;
typedef set<int> si;
typedef map<string, int> msi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int M[4][4], MM[4][4];
ii v[16];
int a[4], x[4];
bool Free[4];
int n;

bool puc(int p) {
  if (p == n) return true;
  bool done = false;
  for (int i = 0; i < n; ++i) if (MM[a[p]][i] and Free[i]) {
    done = true;
    Free[i] = false;
    if (not puc(p + 1)) return false;
    Free[i] = true;
  }
  return done;
}

int hhh() {
  FOR(i, n) {
    x[i] = 0;
    FOR(j, n) {
      x[i] *= 2;
      x[i] += MM[i][j];
    }
  }
  sort(x, x + n);
  int h = 0;
  FOR(i, n) {
    h *= 2;
    h += x[i];
  }
  return h;
}

int main() {
  ios_base::sync_with_stdio(false);
  cout.setf(ios::fixed);
  cout.precision(10);
  int tt;
  cin >> tt;
  for (int ttt = 1; ttt <= tt; ++ttt) {
    map<int, bool> S;
    cout << "Case #" << ttt << ": ";
    cin >> n;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        char c;
        cin >> c;
        M[i][j] = c - '0';
      }
    }
    int m = 0;
    FOR(i, n) FOR(j, n) if (M[i][j] == 0) v[m++] = ii(i, j);
    int ans = 110000;
    for (int w = 0; w < (1 << m); ++w) {
      FOR(i, n) FOR(j, n) MM[i][j] = M[i][j];
      int cost = 0;
      for (int q = 0; q < m; ++q) if ((1 << q) & w) {
        MM[v[q].first][v[q].second] = 1;
        ++cost;
      }
      bool ok = true;
      FOR(i, n) {
        bool f = false, b = false;
        FOR(j, n) {
          if (MM[i][j] == 1) b = true;
          if (MM[j][i] == 1) f = true;
        }
        if (not f or not b) ok = false;
      }
      if (not ok) continue;
//       int h = hhh();
//       if (S.count(h)) {
//         if (S[h]) ans = min(ans, cost);
//         continue;
//       }
      FOR(i, n) a[i] = i;
      do {
        FOR(i, n) Free[i] = true;
        ok = ok and puc(0);
      } while (next_permutation(a, a + n));
      if (ok) ans = min(ans, cost);
//       S[h] = ok;
    }
    cout << ans << endl;
  }
}