#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int a[1234], b[1234];
int up[1234], dn[1234];
int ans[1234];

map <int, int> p;
void out (int * a, int n)
{
  for (int i = 1; i <= n; i++)
    printf ("%d ", a[i]);
  printf ("\n");
}
              
int main (void)
{
  int test, tests;
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, j, tres, res = 0, n;
    scanf ("%d", &n);
    for (i = 1; i <= n; i++)
    {
      scanf ("%d", &a[i]);
      b[i] = a[i];
      p[a[i]] = i;
    }
    sort (b + 1, b + n + 1);

//    out (a, n);
    res = n * n * 2;
    do
    {
      for (i = 1; i <= n; i++)
        if (b[i] <= b[i-1])
          break;
      for (i++; i <= n; i++)
        if (b[i] >= b[i-1])
          break;
      if (i <= n)
        continue;
      tres = 0;
      for (i = 1; i <= n; i++)
        for (j = i+1; j <= n; j++)
          if (p[b[i]] > p[b[j]])
            tres++;
      if (res > tres)
      {
        res = tres;
        for (i = 1; i <= n; i++)
          ans[i] = b[i];
      }
    } while (next_permutation (b  + 1, b + n + 1));
    printf ("Case #%d: %d\n", test + 1, res);
//    out (ans, n);

  }
  return 0;
}
