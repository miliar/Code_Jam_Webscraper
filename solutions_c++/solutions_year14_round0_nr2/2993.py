#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;
              
int main (void)
{
  int test, tests;
  freopen ("b.in", "rt", stdin);
  freopen ("b.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    double res1, res2, c, f, x, v, cur = 0;
    scanf ("%lf %lf %lf", &c, &f, &x);
    v = 2;
    while (1)
    {
       res1 = cur + x / v;
       res2 = cur + (c / v) + x / (f + v);

       if (res1 <= res2)
         break;
       cur += c / v;
       v += f;
    }
    printf ("Case #%d: %.12lf\n", test + 1, res1);

  }
  return 0;
}
