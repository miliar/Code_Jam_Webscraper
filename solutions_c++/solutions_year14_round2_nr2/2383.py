#include <stdio.h>
#include <math.h>

int main ()
{
     freopen("input.txt", "rt", stdin);
     freopen("output.txt", "wt", stdout);
     
     int t, j, i, a, b, k, c, ia, ib, temp;

     scanf("%d", &t);
     
     
     for (j = 1; j<=t; j++)
     {
         scanf("%d%d%d", &a, &b, &k);
         c = 0;
         for (ia = 0; ia < a; ++ia) {
             for (ib = 0; ib < b; ++ib) {
                 temp = ia&ib;
                 if (temp < k) {
                          ++c;
                 }
             }
         }
         
         printf("Case #%d: %d\n", j, c);
     }
     
     return 0;
}
