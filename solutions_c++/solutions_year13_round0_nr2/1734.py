#include <iostream>
using namespace std;
int a[100][100];
int b[100][100];
int max(int i, int j) { return i>= j ? i : j;}
int main(int argc, char* argv[]) {
  int tc;
  scanf("%d", &tc);
  for (int cas = 1; cas <= tc; ++cas) {
    int n,m;
    int i, j;
    scanf("%d%d", &n,&m);
    for (i = 0; i < n; ++i) for (j= 0; j < m; ++j) scanf("%d", &a[i][j]);
    memset(b,0,sizeof(b));
    for (i = 0; i < n; ++i) {
      int v = 0;
      for (j =0; j < m; ++j) v = max(v, a[i][j]);
      for (j = 0; j < m; ++j) b[i][j] += (a[i][j] == v);
    }
    for (j =0; j < m; ++j) {
      int v = 0;
      for (i =0; i < n; ++i) v=  max(v, a[i][j]);
      for (i = 0;i < n ;++i) b[i][j] += (a[i][j] == v);
    }
    bool ans = true;
    for (i = 0; i < n; ++i) {
      for (j = 0; j < m; ++j) if (b[i][j] == 0) ans = false;
    }
    if (ans) {
      printf("Case #%d: YES\n", cas);
    } else {
      printf("Case #%d: NO\n", cas);
    }
  }
  return 0;
}
