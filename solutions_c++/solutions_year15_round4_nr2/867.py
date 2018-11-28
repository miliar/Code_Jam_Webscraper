#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <math.h>
#include <stack>
using namespace std;
double v, tmp, r[5], c[5], a, b;
int t, i, j, k, n;
int main()
{
   freopen("B-small-attempt0.in", "r",stdin);
   freopen("B-small-attempt0.out", "w",stdout);
   scanf("%d", &t);
   for (i = 1; i <= t; i++)
   {
      scanf("%d", &n);
      scanf("%lf%lf", &v, &tmp);
      printf("Case #%d: ", i);
      for (j = 0; j < n; j++)
         scanf("%lf%lf", &r[j], &c[j]);
      if (n == 1)
      {
         a = c[0];
         b = tmp;
         if (a + 0.0000001>b && a - 0.0000001 < b)
            printf("%.8f\n", v / r[0]);
         else
            printf("IMPOSSIBLE\n");
      }
      else
      {
         a = c[0];
         b = c[1];
         if (a + 0.0000001>b && a - 0.0000001 < b)
         {
            b = tmp;
            if (a + 0.0000001>b && a - 0.0000001 < b)
               printf("%.8f\n", v / (r[0]+r[1]));
            else
               printf("IMPOSSIBLE\n");
         }
         else
         {

            a = (v*(tmp - c[1])) / (r[0] * (c[0] - c[1]));
            b = (v*(tmp - c[0])) / (r[1] * (c[1] - c[0]));
            if (a < 0 || b < 0)
               printf("IMPOSSIBLE\n");
            else 
            {
               printf("%.8f\n", a>b ? a : b);
            }
         }
      }

   }
   return 0;
}