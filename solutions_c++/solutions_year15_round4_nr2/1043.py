#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#define abs(x) (((x)<0)?(-(x)):(x))

using namespace std;

const int MaxN = 2;

double r[MaxN], c[MaxN], vv[MaxN], eps = 1e-9;
              
int main (void)
{
  int test, tests;
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, n;
    double v, x, res;
    scanf ("%d %lf %lf", &n, &v, &x);
    for (i = 0; i < n; i++)
      scanf ("%lf %lf", &r[i], &c[i]);
    if (n == 1)
    {
      if (abs(c[0] - x) < eps)
        printf ("Case #%d: %.12lf\n", test + 1, v/r[0]);
      else
        printf ("Case #%d: IMPOSSIBLE\n", test + 1);
    }
    else if (n == 2)
    {
      if (abs(c[0] - c[1]) < eps)
      {
        if (abs(c[0] - x) < eps)
          printf ("Case #%d: %.12lf\n", test + 1, v/(r[0] + r[1]));
        else
          printf ("Case #%d: IMPOSSIBLE\n", test + 1);
      }
      else
      {
        vv[1] = v * (x - c[0]) /(c[1] - c[0]);
        vv[0] = v - vv[1];
        if (c[0] > x && c[1] > x || c[0] < x && c[1] < x )
          printf ("Case #%d: IMPOSSIBLE\n", test + 1);
        else
        {
          res = max (vv[0]/r[0], vv[1]/r[1]);
          printf ("Case #%d: %.12lf\n", test + 1, res);
        }
      }
    }
    else 
      printf ("Case #%d: n > 2\n", test + 1);

  }
  return 0;
}
