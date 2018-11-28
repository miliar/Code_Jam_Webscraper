#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
const int MAXN = 200 + 10;
char mp[MAXN][MAXN];
int n, m;

bool check() {
  for (int i = 0; i < n; ++ i) {
    for (int j = 0; j < m; ++ j) if (mp[i][j] != '.') {
      int c = 0;
      for (int k = 0; k < n; ++ k) if (mp[k][j] != '.') ++ c;
      for (int k = 0; k < m; ++ k) if (mp[i][k] != '.') ++ c;
      if (c == 2) return false;
    }
  }
  return true;
}

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++ cas) {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++ i) scanf("%s", mp[i]);
    int ret = 0;
    for (int j = 0; j < m; ++ j) {
      char c = '.';
      for (int i = 0; i < n; ++ i) {
        if (mp[i][j] != '.') {
          c = mp[i][j];
          break;
        }
      }
      ret += c == '^';
      c = '.';
      for (int i = n - 1; i >= 0; -- i) {
        if (mp[i][j] != '.') {
          c = mp[i][j];
          break;
        }
      }
      ret += c == 'v';
    }
    for (int i = 0; i < n; ++ i) {
      char c = '.';
      for (int j = 0; j < m; ++ j) {
        if (mp[i][j] != '.') {
          c = mp[i][j];
          break;
        }
      }
      ret += c == '<';
      c = '.';
      for (int j = m - 1; j >= 0; -- j) {
        if (mp[i][j] != '.') {
          c = mp[i][j];
          break;
        }
      }
      ret += c == '>';
    }
    printf("Case #%d: ", cas);
    if (check()) printf("%d\n", ret);
    else puts("IMPOSSIBLE");
  }
  return 0;
}