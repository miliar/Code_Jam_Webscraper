#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <utility>

using namespace std;

#define ABS(x) (((x) < 0) ? (-(x)) : (x))
#define MIN(a,b) (((a) < (b)) ? (a) : (x))
#define MAX(a,b) (((a) > (b)) ? (a) : (x))

int g[100][100];
int n, m;
char signs[4] = {'v', '^', '<', '>'};

bool ok (int I, int J, char c) {
  int dx = 0, dy = 0;
  if (c == 'v') {
    dx = 1;
  } else if (c == '^') {
    dx = -1;
  } else if (c == '<') {
    dy = -1;
  } else if (c == '>') {
    dy = 1;
  } else {
    fprintf(stderr, "eRRor\n");
    exit(1);
  }
  int i = I+dx, j = J+dy;
  while (i >= 0 && j >= 0 && i < n && j < m) {
    if (g[i][j] != '.') return true;
    i += dx;
    j += dy;
  }
  return false;
}

int main (void) {
  int T;
  scanf("%d", &T);
  for (int currentcase = 1; currentcase <= T; ++currentcase) {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        char c = getchar();
        while (c != '^' && c != '.' && c != '<' && c != '>' && c != 'v')
          c = getchar();
        g[i][j] = c;
      }
    }
    bool works = true;
    int num = 0;
    for (int i = 0; i < n && works; i++) {
      for (int j = 0; j < m && works; j++) {
        if (g[i][j] != '.') {
          if (!ok(i, j, g[i][j])) {
            if (ok(i, j, signs[0]) || ok(i, j, signs[1]) || ok(i, j, signs[2]) || ok(i, j, signs[3])) {
              num++;
            } else {
              works = false;
            }
          }
        }
      }
    }
    printf("Case #%d: ", currentcase);
    if (works) {
      printf("%d", num);
    } else {
      printf("IMPOSSIBLE");
    }
    printf("\n");
  }
  return 0;
}
