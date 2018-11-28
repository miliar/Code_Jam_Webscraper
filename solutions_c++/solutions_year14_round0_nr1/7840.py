#include <stdio.h>
#include <math.h>

#define abs(a) (((a) < 0) ? -(a) : (a))

int main ()
{
     freopen("input.txt", "rt", stdin);
     freopen("output.txt", "wt", stdout);
     
     int t, x, y, j, i, k, a[4][4], b[4][4], res1[4], res2[4], count, res;
     scanf("%d", &t);
     
     for (j = 1; j<=t; j++)
     {
         scanf("%d", &x);
         
         for (i = 0; i < 4; i++)
         {
             for (k = 0; k < 4; k++)
             {
                 scanf("%d", &a[i][k]);
                 
             }
         }
         
         scanf("%d", &y);
         
         for (i = 0; i < 4; i++)
         {
             for (k = 0; k < 4; k++)
             {
                 scanf("%d", &b[i][k]);
                 
             }
         }
         
         count = 0;
         res = 0;
         for (i = 0; i < 4; i++)
         {
             for (k = 0; k < 4; k++)
             {
                 if ((a[x-1][i]) == (b[y-1][k]))
                 {
                      count++;
                      res = a[x-1][i];           
                               
                 }
             }
         }
         
         if (count == 1)
         {
                   printf("Case #%d: %d\n", j, res);
                   
         }
         if (count == 0)
         {
                   printf("Case #%d: Volunteer cheated!\n", j);
                   
         }
         if (count > 1)
         {
                   printf("Case #%d: Bad magician!\n", j);
         }         
              
     }
     
     
     return 0;
}
