#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <set>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

int a[111][111];

int n, m;
int cnt;

bool check() {
  REP(i, n) REP(j, m) {
    if (a[i][j] == 0) continue;
    int f = 0, z = 0;

    if (a[i][(j-1+m)%m] == a[i][j]) f++; else
      if (a[i][(j-1+m)%m] == 0) z++;

    if (a[i][(j+1)%m] == a[i][j]) f++; else
      if (a[i][(j+1)%m] == 0) z++;

    if (i > 0 && a[i-1][j] == a[i][j]) f++; else
      if (i > 0 && a[i-1][j] == 0) z++;

    if (i < n-1 && a[i+1][j] == a[i][j]) f++; else
      if (i < n-1 && a[i+1][j] == 0) z++;
    
    if (f > a[i][j]) return false;
    if (f + z < a[i][j]) return false;
  }
  return true;
}

set<vector<int>> S;

void go(int x, int y) {
  if (!check()) return;
  if (y == m) { go(x + 1, 0); return; }
  if (x == n) { 
    vector<int> v;
    REP(off, m) {
      vector<int> w;
      REP(i, n) REP(j, m)
        w.push_back(a[i][(off + j) % m]);
      if (v.size() == 0 || w < v) v = w;
    }
    S.insert(v);
    return;
  }

  for (int i = 1; i <= 3; ++i) {
    a[x][y] = i;
    go(x, y + 1);
    a[x][y] = 0;
  }
}

int ans[111][111];

int main(void) {
  FOR(r, 2, 7) FOR(c, 2, 7) {
    n = r, m = c;
    S.clear();
    go(0, 0);
    ans[r][c] = S.size();
  }

  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    scanf("%d %d", &n, &m);
    printf("Case #%d: ", tp);
    printf("%d\n", ans[n][m]);
  }
  return 0;
}
