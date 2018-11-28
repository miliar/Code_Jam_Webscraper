#include <cstring>
#include <cstdio>
using namespace std;
int stk[1005];
int top;
int N, M, ss, tt;
int mp[1005][1005];

void dfs(int x) {
  stk[top++] = x;
  for (int i = 1; i <= N; ++i) {
    if (mp[x][i]) {
      mp[x][i] = mp[i][x] = 0;
      dfs(i);
      break;
    }
  }
}
void fleury(int ss) {
  int brige;
  top = 0;
  stk[top++] = ss;
  while (top) {
    brige = 1;
    for (int i = 1; i <= N; ++i) {
      if (mp[stk[top-1]][i]) {
        brige = 0;
        break;
      }
    }
    if (brige) printf("%d ", stk[--top]);
    else dfs(stk[--top]);
  }
}
int main() {
  int x, y, deg, num;
  while (scanf("%d %d", &N, &M) != EOF) {
    memset(mp, 0, sizeof (mp));
    for (int i = 0; i < M; ++i) {
      scanf("%d %d", &x, &y);
      mp[x][y] = mp[y][x] = 1;
    }
    for (int i = 1; i <= N; ++i) {
      deg = num = 0;
      for (int j = 1; j <= N; ++j) {
        deg += mp[i][j];
      }
      if (deg & 1) ss = i, ++num;
    }
    if (num == 0 || num == 2) fleury(ss);
    else puts("No Euler path");
  }
  return 0;
}
/*
  9 12
  1 5
  1 9
  5 3
  5 4
  5 8
  2 3
  2 4
  4 6
  6 7
  6 8
  7 8
  8 9

  path:
  4 5 8 7 6 8 9 1 5 3 2 4 6
*/
