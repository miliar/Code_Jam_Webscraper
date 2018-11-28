#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;
              
int main (void)
{
  int test, tests, n = 4;
  int ok[17] = {0};
  freopen ("a.in", "rt", stdin);
  freopen ("a.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, j, r, res = -1, a, k;
    memset (ok, 0, sizeof(ok));
    for (k = 0; k < 2; k++)
    {
      scanf ("%d", &r);
      for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
        {
          scanf ("%d", &a);
          if (i == r)
            ok[a]++;
        }
    }
    for (i = 1; i <= n * n; i++)
    {
      if (ok[i] == 2)
        if (res == -1)
          res = i;
        else
          res = -2;
    }
    if (res == -1)
      printf ("Case #%d: Volunteer cheated!\n", test + 1);
    else if (res == -2)
      printf ("Case #%d: Bad magician!\n", test + 1);
    else
      printf ("Case #%d: %d\n", test + 1, res);

  }
  return 0;
}
