#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;
const int MaxN = 111;
char b[MaxN][MaxN];

int di[256], dj[256];

char dir[] = "<>^v";
              
int main (void)
{
  int test, tests;
  di['^'] = -1;
  di['v'] = 1;
  dj['>'] = 1;
  dj['<'] = -1;
  
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, j, d, ci, cj, n, m, res = 0, OK;
    scanf (" %d %d", &n, &m);
    memset (b, -1, sizeof b);
    for (i = 1; i <= n; i++)
      for (j = 1; j <= m; j++)
        scanf (" %c", &b[i][j]);
    OK = 1;
    for (i = 1; i <= n; i++)
      for (j = 1; j <= m; j++)
      {
        if (!OK)
          break;
        if (b[i][j] == '.')
          continue;
        d = b[i][j];
        ci = i + di[d]; 
        cj = j + dj[d];
        while (b[ci][cj] == '.')
        {
          ci += di[d];
          cj += dj[d];
        }
//        printf ("(%d %d) -> (%d %d),  %c\n", i, j, ci, cj, b[ci][cj]==-1? '!' : b[i][j]);
        if (b[ci][cj] != -1)
          continue;
        else 
          res++;
        int ok = 0;
        for (int k = 0; k < 4; k++)
        {
          d = dir[k];
          ci = i + di[d]; 
          cj = j + dj[d];
          while (b[ci][cj] == '.')          
          {
            ci += di[d];
            cj += dj[d];
          }
          if (b[ci][cj] != -1)
            ok = 1;
        }
        if (!ok)
        {
           printf ("Case #%d: IMPOSSIBLE\n", test + 1);
           OK = 0;
           break;
        }
      }
    if (OK)
      printf ("Case #%d: %d\n", test + 1, res);
  }
  return 0;
}
