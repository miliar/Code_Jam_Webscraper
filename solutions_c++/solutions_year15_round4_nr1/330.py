/* 
  2014.03.26 15:10
  http://codeforces.ru/gym/100289/
*/


#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <memory.h>
#include <cmath>
#include <string> 
#include <ctime>

using namespace std;

// #undef Fdg_Home

char f[102][102];

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

void solveTest(int CS) {
  printf("Case #%d: ", CS);
  int n, m;
  scanf("%d%d\n", &n, &m);
  for (int i = 0; i < n; ++i) {
    gets(f[i]);
  }
  int ans = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (f[i][j] != '.') {
        int d = -1;
        if (f[i][j] == '>') d = 2;
        else if (f[i][j] == '<') d = 1;
        else if (f[i][j] == 'v') d = 3;
        else if (f[i][j] == '^') d = 0;

        bool ok = false;
        int x = i + dx[d], y = j + dy[d];
        while (x >= 0 && x < n && y >= 0 && y < m) {
          if (f[x][y] != '.') ok = true;
          x += dx[d]; y += dy[d];
        }
        if (!ok) {
          for (d = 0; d < 4; ++d) {
            int x = i + dx[d], y = j + dy[d];
            while (x >= 0 && x < n && y >= 0 && y < m) {
              if (f[x][y] != '.') ok = true;
              x += dx[d]; y += dy[d];
            }
          }
          if (ok) ans++;
          else {
            puts("IMPOSSIBLE");
            return;
          }
        }
      }
    }
  }
  printf("%d\n", ans);
}

int main() {
// #ifndef Fdg_Home
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
// #endif
  int T;
  scanf("%d\n", &T);
  for (int test = 1; test <= T; ++test) {
    solveTest(test);
  }
  return 0;
}