#include <cassert>
#include <cstdio>

int main () {
  int tn;
  assert (scanf ("%d", &tn) == 1);
  for (int t = 1; t <= tn; t++) {
    int r, c;
    assert (scanf ("%d%d", &r, &c) == 2);
    char m[r][c];
    for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++)
        assert (scanf (" %c", &m[i][j]) == 1);
    int d[r][c], ok[r][c];
    for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++)
        d[i][j] = 4, ok[i][j] = 1;

    for (int i = 0; i < r; i++) {
      int j = 0;
      while (j < c && m[i][j] == '.')
        j++;
      if (j < c) {
        d[i][j]--;
        if (m[i][j] == '<')
          ok[i][j] = 0;
      }
      j = c - 1;
      while (j >= 0 && m[i][j] == '.')
        j--;
      if (j >= 0) {
        d[i][j]--;
        if (m[i][j] == '>')
          ok[i][j] = 0;
      }
    }
    for (int j = 0; j < c; j++) {
      int i = 0;
      while (i < r && m[i][j] == '.')
        i++;
      if (i < r) {
        d[i][j]--;
        if (m[i][j] == '^')
          ok[i][j] = 0;
      }
      i = r - 1;
      while (i >= 0 && m[i][j] == '.')
        i--;
      if (i >= 0) {
        d[i][j]--;
        if (m[i][j] == 'v')
          ok[i][j] = 0;
      }
    }
    bool good = true;
    int ans = 0;
    for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++) {
        if (m[i][j] == '.')
          continue;
        // fprintf (stderr, "[i=%d][j=%d] d=%d ok=%d\n", i, j, d[i][j], ok[i][j]);
        if (d[i][j] == 0)
          good = false;
        if (!ok[i][j])
          ans++;
      }
    if (good)
      printf ("Case #%d: %d\n", t, ans);
    else
      printf ("Case #%d: IMPOSSIBLE\n", t);
  }
  return 0;
}

