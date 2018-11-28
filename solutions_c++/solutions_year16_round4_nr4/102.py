#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, n, c[11][11], ans, r[5];
char a[11][11];
bool b[5], B[5];

bool checkcheck(int step) {
     if (step == n + 1) return true;
     int x = r[step];
     bool ok = false;
     for (int i = 1; i <= n; i++) 
          if (c[x][i] && !B[i]) {
               B[i] = true;
               ok = true;
               if (!checkcheck(step + 1)) return false;
               B[i] = false;
          }
     if (!ok) return false;
     return true;
}

bool check(int step) {
     if (step == n + 1) {
          memset(B, false, sizeof(B));
          return checkcheck(1);
     }
     for (int i = 1; i <= n; i++) 
          if (!b[i]) {
               b[i] = true;
               r[step] = i;
               if (!check(step + 1)) return false;
               b[i] = false;
          }
     return true;
}
  
inline void soso(int x, int y, int cnt) {
     if (cnt >= ans) return;
     if (x == n + 1) {
          memset(b, false, sizeof(b));
          if (check(1)) ans = cnt;
          return;
     } 
     int nx = x, ny = y + 1;
     if (ny == n + 1) ny = 1, nx++;
     if (a[x][y] == '1') {
          c[x][y] = 1;
          soso(nx, ny, cnt);
     } else {
          c[x][y] = 0;
          soso(nx, ny, cnt);
          c[x][y] = 1;
          soso(nx, ny, cnt + 1);
     }
}
              
int main() {
     freopen("d.in", "r", stdin);
     freopen("d.out", "w", stdout);
     scanf("%d", &test);
     for (int uu = 1; uu <= test; uu++) {
          scanf("%d", &n);
          for (int i = 1; i <= n; i++)
               scanf("%s", a[i] + 1);
          ans = 1 << 30;
          soso(1, 1, 0);
          printf("Case #%d: %d\n", uu, ans);
     }
}
