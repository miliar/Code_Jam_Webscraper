#include <algorithm>
#include <functional>

#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <string>
#include <vector>

using namespace std;

const int MAXN  = 123;

int r, s;
int mat[MAXN][MAXN];

int row[MAXN];
int col[MAXN];

bool check(int h) {
  memset(row, 0, sizeof row);
  memset(col, 0, sizeof col);
  for (int i = 0; i < r; ++i)
    for (int j = 0; j < s; ++j) {
      if (mat[i][j] <= h) {
        ++row[i];
        ++col[j];
      }
    }

  for (int i = 0; i < r; ++i)
    for (int j = 0; j < s; ++j) {
      if (mat[i][j] == h) {
        if (row[i] == s) continue;
        if (col[j] == r) continue;
        return false;
      }
    }

  return true;
}

int main(void)
{
  int T; scanf("%d", &T);

  for (int counter = 0; counter < T; ++counter) {
    scanf("%d %d", &r, &s);
    for (int i = 0; i < r; ++i)
      for (int j = 0; j < s; ++j)
        scanf("%d", mat[i] + j);

    bool ok = true;

    for (int h = 1; h <= 100; ++h) {
      ok &= check(h);
    }

    printf("Case #%d: %s\n", counter + 1, ok ? "YES" : "NO");
    fflush(stdout);
  }

  return (0-0);
}
