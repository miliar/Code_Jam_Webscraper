#include <bits/stdc++.h>
using namespace std;

char c[105][105];
int n,m;
int t;

int cannot[105][105];
int main() {
  scanf("%d", &t);
  int cs  = 0;
  while (t--) {
    ++cs;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
      scanf("%s",c[i]);
    }
    int num = 0;
    memset(cannot, 0, sizeof(cannot));
    //left to right
    for (int i = 0; i < n; i++) {
      int j = 0;
      while (j < m && c[i][j] == '.') ++j;
      if (j < m) cannot[i][j] |= 1;
    }

    //top to bottom
    for (int i = 0; i < m; i++) {
      int j = 0;
      while (j < n && c[j][i] == '.') ++j;
      if (j < n) cannot[j][i] |= 2;
    }

    //right to left
    for (int i = 0; i < n; i++) {
      int j = m-1;
      while (j >= 0 && c[i][j] == '.') --j;
      if (j >= 0) cannot[i][j] |= 4;
    }

    //bottom to top
    for (int i = 0; i < m; i++) {
      int j = n - 1;
      while (j >= 0 && c[j][i] == '.') --j;
      if (j >= 0) cannot[j][i] |= 8;
    }

    int res = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (cannot[i][j] == 15) res = 1000000000;
        bool add = false;
        if (c[i][j] == '>' && ((cannot[i][j] & 4) != 0)) add = true;
        if (c[i][j] == '<' && ((cannot[i][j] & 1) != 0)) add = true;
        if (c[i][j] == '^' && ((cannot[i][j] & 2) != 0)) add = true;
        if (c[i][j] == 'v' && ((cannot[i][j] & 8) != 0)) add = true;
        if (add) ++res;
      }
    }
    printf("Case #%d: ", cs);
    if (res >= 1000000000) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", res);
    }
  }
}
