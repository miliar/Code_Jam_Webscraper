#include <cstdio>
#include <iostream>

using namespace std;

char a[111][111];
int n, m;

bool go_outside(int x, int y) {
  if (a[x][y] == '.')
    return false;

  int inc_x = 0;
  int inc_y = 0;

  if (a[x][y] == '^') inc_x = -1;
  if (a[x][y] == 'v') inc_x = +1;
  if (a[x][y] == '>') inc_y = +1;
  if (a[x][y] == '<') inc_y = -1;

  bool outside = true;

  while (x >= 0 && y >= 0 && x < n && y < m) {
    x += inc_x;
    y += inc_y;

    if (!(x >= 0 && y >= 0 && x < n && y < m)) break;

    if (a[x][y] != '.') {
      outside = false;
      break;
    }
  }

  return outside;
}

bool not_possible(int x, int y) {
  if (a[x][y] == '.')
    return false;

  a[x][y] = '^';
  if (!go_outside(x, y)) return false;
  a[x][y] = 'v';
  if (!go_outside(x, y)) return false;
  a[x][y] = '<';
  if (!go_outside(x, y)) return false;
  a[x][y] = '>';
  if (!go_outside(x, y)) return false;

  return true;
}

int main() {
  freopen("a.inp", "r", stdin);
  freopen("a.out", "w", stdout);

  int nTest;
  scanf("%d", &nTest);

  for (int test = 0; test < nTest; test++) {
    scanf("%d %d", &n, &m);
    scanf("\n");
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++)
        scanf("%c", &a[i][j]);
      scanf("\n");
    }

    int res = 0;
    bool found = true;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++)
        if (a[i][j] != '.')
          if (go_outside(i, j)) {
            if (not_possible(i, j))
              found = false;
            res++;
          }
    }

    printf("Case #%d: ", test + 1);
    if (found)
      printf("%d\n", res);
    else
      printf("IMPOSSIBLE\n");
  }

  return 0;
}
