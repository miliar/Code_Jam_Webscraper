#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 111, Inf = 0x3f3f3f3f;

char *res[] = {"YES","NO"};

int b[MaxN][MaxN];
int c[MaxN][MaxN];

int main (void)
{
  int test, tests;

  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, j, nres = 0, n, m, mx;
    scanf ("%d %d", &n, &m);
    memset (c, Inf, sizeof(c));

    for (i = 0; i < n; i++)
      for (j = 0; j < m; j++)
        scanf (" %d", &b[i][j]);
    nres = 0;

    for (i = 0; i < n; i++)
    {
      mx = -1;
      for (j = 0; j < m; j++)
        if (mx < b[i][j])
          mx = b[i][j];
      for (j = 0; j < m; j++)
        if (mx < c[i][j])
          c[i][j] = mx;
    }    
    for (j = 0; j < m; j++)
    {
      mx = -1;
      for (i = 0; i < n; i++)
        if (mx < b[i][j])
          mx = b[i][j];
      for (i = 0; i < n; i++)
      {
        if (mx < c[i][j])
          c[i][j] = mx;
        if (c[i][j] != b[i][j])
          nres = 1;
      }
    }    
    printf ("Case #%d: %s\n", test + 1, res[nres]);
    
  }
  return 0;
}
