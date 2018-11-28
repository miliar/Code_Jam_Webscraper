#include <stdio.h>

int main ()
{
     freopen("input.txt", "rt", stdin);
     freopen("output.txt", "wt", stdout);
     
     int t, j, i;
     double c, f, x, nofarm, withfarm, ans, step, n;
     scanf("%d", &t);
     
     for (j = 1; j<=t; j++)
     {
         
         scanf("%lf%lf%lf", &c, &f, &x);
         
         
         i = 0;
         n = 2.0;
         nofarm = x/n;
         withfarm = (c/n + x/(f+n));
         
         while (nofarm > withfarm)
         {
               step = x/(f+n);
               nofarm = withfarm;
               withfarm = withfarm - step + (c/(f+n) + x/(f+n+f));
               n+=f;
         }
         
         
         if (nofarm < withfarm)
         {
                    ans = nofarm;
                    
         }
         else
         {
             ans = withfarm;
         }
         
         
         printf("Case #%d: %.9lf\n", j, ans);
               
              
     }
     
     
     return 0;
}
