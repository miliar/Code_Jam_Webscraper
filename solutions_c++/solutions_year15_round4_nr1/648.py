#define PRETEST
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <iomanip>
#include <sstream>
using namespace std;

#define INF 0x4f4f4f4f
#define FILL(a,b) memset(a,b,sizeof(a))
#define SQR(a) ((a) * (a))

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<string, int> psi;
typedef map<string, int> msi;
typedef map<int, int> mii;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
char pos[] = {'^', '>', 'v', '<'};
int R, C;
char s[110][110];

int index(char c) {
  for (int k = 0; k < 4; ++k) {
    if (pos[k] == c) {
      return k;
    }
  }
  return -1;
}

bool is_out(int r, int c) {
  int dir = index(s[r][c]);
  int x = r;
  int y = c;
  while (true) {
    x += dx[dir];
    y += dy[dir];
    if (x >= 0 && x < R && y >= 0 && y < C) {
      if (s[x][y] != '.') {
        return false;
      }
    } else {
      return true;
    }
  }
  return false;
}

bool change(int r, int c) {
  char cc = s[r][c];
  for (int k = 0; k < 4; ++k) {
    if (cc != pos[k]) {
      s[r][c] = pos[k];
      if (!is_out(r, c)) {
        return true;
      }
    }
  }
  return false;
}

int main(int argc, char *argv[]) {
#ifdef PRETEST
  freopen("A-large.in", "r", stdin);
#endif
  int T;
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    scanf("%d%d", &R, &C);
    for (int i = 0; i < R; ++i) {
      scanf("%s", s[i]);
    }
    int ans = 0;
    bool flag = true;
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        if (s[i][j] != '.') {
          if (is_out(i, j)) {
            if (!change(i, j)) {
              flag = false;
              break;
            }
            ++ans;
          }
        }
      }
    }
    printf("Case #%d: ", cas);
    if (flag) {
      printf("%d\n", ans);
    } else {
      printf("IMPOSSIBLE\n");
    }
  }
  return 0;
}
