#include <bits/stdc++.h>
using namespace std;

int t;
int n, m;
int lv[105];
bool done[105];
int nx[105];
int pv[105];
char c[105][105];

struct pos {
  bool horiz;
  int x, y;
};

pos get_original(int x) {
  pos tmp;
  if (x < m) {
    tmp.horiz = true;
    tmp.x = 0;
    tmp.y = x;
  } else if (x < m + n) {
    tmp.horiz = false;
    tmp.y = m;
    tmp.x = x - m;
  } else if (x < m + n + m) {
    tmp.horiz = true;
    tmp.x = n;
    tmp.y = m - 1 - (x - m - n);
  } else {
    tmp.horiz = false;
    tmp.y = 0;
    tmp.x = n - 1 - (x - m - n - m);
  }
  return tmp;
}
int state;
void print() {
  printf("=====\n");
  for (int i = 0; i < n; i++) {
    for (int j = 0;j < m; j++) {
      printf("%c",c[i][j]);
    }
    printf("\n");
  }
}
int main() {
  scanf("%d", &t);
  int cs = 0;
  while (t--) {
    memset(done, 0, sizeof(done));
    memset(lv, 0, sizeof(lv));
    memset(nx, 0, sizeof(nx));
    memset(pv, 0, sizeof(pv));
    memset(c, 0, sizeof(c));
    scanf("%d %d", &n, &m);
    int k = 2 * (n + m);
    for (int i = 0; i < k / 2; i++) {
      int tmp, tmp2;
      scanf("%d %d", &tmp, &tmp2);
      --tmp; --tmp2;
      lv[tmp] = tmp2;
      lv[tmp2] = tmp;
    }
    for (int i =0 ; i < k; i++) {
      nx[i] = i + 1;
      pv[i] = i - 1;
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        c[i][j] = ' ';
      }
    }
    pv[0] = k - 1;
    nx[k - 1] = 0;
    int cntdone = 0;
    while (true) {
      bool found = false;
      for (int i = 0; i < k; i++) {
        if (!done[i] && lv[i] == nx[i]) {
          found = true;
          pos now = get_original(i);
          int state;
          if (i < m) {
            state = 0;
          } else if ( i < m + n) {
            state = 1;
          } else if ( i < m + n + m) {
            state = 2;
          } else {
            state = 3;
          }

          pos target = get_original(lv[i]);
          while (true) {
            if (target.x == now.x && target.y == now.y && target.horiz == now.horiz) {
              break;
            }
            if (state == 0) {
              if (now.x < 0 || now.y < 0 || now.x >= n || now.y >= m) {
                cntdone = -1;
                goto hell;
              }
              if (c[now.x][now.y] == '/') {
                state = 1;
                now.horiz = false;
              } else {
                state = 3;
                c[now.x][now.y] = '\\';
                now.y++;
                now.horiz = false;
              }
            } else if (state == 1) {
              if (now.x < 0 || now.y - 1 < 0 || now.x >= n || now.y -1 >= m) {
                cntdone = -1;
                goto hell;
              }
              if (c[now.x][now.y - 1] == '\\') {
                state = 2;
                now.y--;
                now.horiz = true;
              } else {
                state = 0;
                c[now.x][now.y - 1] = '/';
                now.y--;
                now.x++;
                now.horiz = true;
              }
            } else if (state == 2) {
              if (now.x  - 1< 0 || now.y < 0 || now.x  - 1>= n || now.y >= m) {
                cntdone = -1;
                goto hell;
              }
              if (c[now.x - 1][now.y] == '/') {
                state = 3;
                now.x--;
                now.y++;
                now.horiz = false;
              } else {
                state = 1;
                c[now.x - 1][now.y] = '\\';
                now.x--;
                now.horiz = false;
              }
            } else {
              if (now.x < 0 || now.y < 0 || now.x >= n || now.y >= m) {
                cntdone = -1;
                goto hell;
              }
              if (c[now.x][now.y] == '\\') {
                state = 0;
                now.x++;
                now.horiz = true;
              } else {
                state = 2;
                now.horiz = true;
                c[now.x][now.y] = '/';
              }
            }
          }
          int pppp = pv[i];
          int nnnn = nx[nx[i]];
          nx[pppp] = nnnn;
          pv[nnnn] = pppp;
          done[i] = true;
          done[lv[i]] = true;
          cntdone += 2;
        }
      }
      if (!found) {
        cntdone = -1;
        break;
      }
      if (cntdone == k) {
        break;
      }
    }
hell:
    cs++;
    printf("Case #%d:\n", cs);
    if (cntdone == -1) {
      printf("IMPOSSIBLE\n");
    } else {
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          if (c[i][j] == ' ') {
            c[i][j] = '/';
          }
          printf("%c", c[i][j]);
        }
        printf("\n");
      }
    }
  }

}
