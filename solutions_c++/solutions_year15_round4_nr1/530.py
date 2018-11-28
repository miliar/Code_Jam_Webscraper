#include <bits/stdc++.h>
  
using namespace std;

template<class T> inline T sqr(const T& a) { return a * a; }
  
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
  
const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 110;

int colc[N];
int rowc[N];
char a[N][N];
bool used[N][N];

void Solve() {
  int n, m;
  scanf("%d%d\n", &n, &m);
  memset(colc, 0, sizeof colc);
  memset(rowc, 0, sizeof rowc);

  for (int i = 0; i < n; ++i) {
    scanf("%s", a[i]);
    for (int j = 0; j < m; ++j) {
      if (a[i][j] != '.')
        ++colc[j], ++rowc[i];   
    }
  }
  int ans = 0;
  memset(used, 0, sizeof used);

  for (int i = 0; i < n; ++i) {
    int lf = -1, rg = -1;
    for (int j = 0; j < m; ++j) {
      if (a[i][j] != '.') {
        if (colc[j] == 1 && rowc[i] == 1) {
          puts("IMPOSSIBLE");
          return;
        }
        if (lf == -1)
          lf = j;
        rg = j;
      }
    }
    if (lf != -1 && 
        (a[i][lf] == '<' || (lf == rg && a[i][lf] == '>'))) {
      ++ans;
      used[i][lf] = true;
    }
    if (rg != -1 && lf != rg && a[i][rg] == '>') {
      ++ans;
      used[i][rg] = true;
    }
  }

  for (int j = 0; j < m; ++j) {
    int lf = -1, rg = -1;
    for (int i = 0; i < n; ++i) {
      if (a[i][j] != '.') {
        if (lf == -1)
          lf = i;
        rg = i;
      }
    }  
    if (lf != -1 && (a[lf][j] == '^' || (lf == rg && a[rg][j] == 'v')) && !used[lf][j]) {
      ++ans;
      used[lf][j] = true;
    }
    if (rg != -1 && lf != rg && a[rg][j] == 'v' && !used[rg][j]) {
      ++ans;
      used[rg][j] = true;
    }
  }
  printf("%d\n", ans);
}

int main() {
  int tests;
  scanf("%d", &tests);
  for (int it = 1; it <= tests; ++it) {
    printf("Case #%d: ", it);
    Solve();
  }

  return 0;
}
