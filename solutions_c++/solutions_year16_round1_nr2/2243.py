#include <bits/stdc++.h>

using namespace std;

#ifdef ACMTUYO
struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#else
struct RTC{};
#define DBG(X)
#endif

#define fast_io() ios_base::sync_with_stdio(false)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long int number;
const int maxn = 52;
int n, nlist;
vector<vector<int> > v;
int mat[maxn][maxn];
bool col_vis[maxn];
bool check(int mask) {
  int row = 0;
  for (int i = 0; i < nlist; i++)
    if (mask & (1 << i)) {
      for (int j = 0; j < n; j++)
        mat[row][j] = v[i][j];
      row++;
    }
  assert(row == n);
  for (int col = 0; col < n; col++)
    for (int row = 1; row < n; row++)
      if (!(mat[row][col] > mat[row - 1][col]))
        return false;
  memset(col_vis, false, sizeof(col_vis));
  for (int i = 0; i < nlist; i++)
    if (!(mask & (1 << i))) {
      vector<int> &buscar = v[i];
      bool existe = false;
      for (int col = 0; col < n; col++) {
        if (!col_vis[col]) {
          bool igual = true;
          for (row = 0; row < n; row++) {
            if (buscar[row] != mat[row][col]) {
              igual = false;
              break;
            }
          }
          if (igual) {
            col_vis[col] = true;
            existe = true;
            break;
          }
        }
      }
      if (!existe)
        return false;
    }
  return true;
}
vector<int> solve() {
  sort(all(v));
  int lim = 1 << nlist;
  for (int mask = 0; mask < lim; mask++) {
    if (__builtin_popcount(mask) == n) {
      if (check(mask)) {
        vector<int> ans;
        for (int i = 0; i < n; i++)
          if (!col_vis[i]) {
            for (int j = 0; j < n; j++)
              ans.pb(mat[j][i]);
            return ans;
          }
      }
    }
  }
  assert(false);
  return vector<int>();
}
int main() {
  int t;
  scanf("%d", &t);
  for (int caso = 1; caso <= t; caso++) {
    scanf("%d", &n);
    nlist = 2 * n - 1;
    v.clear();
    for (int i = 0; i < nlist; i++) {
      vector<int> tmp(n);
      for (int j = 0; j < n; j++)
        scanf("%d", &tmp[j]);
      v.pb(tmp);
    }
    vector<int> ans = solve();
    assert(sz(ans) == n);
    printf("Case #%d:", caso);
    for (int i = 0; i < n; i++)
      printf(" %d", ans[i]);
    printf("\n");
  }
  return 0;
}

