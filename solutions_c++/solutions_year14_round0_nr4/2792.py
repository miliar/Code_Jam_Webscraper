#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 1000;
              
double naomi[MaxN], ken[MaxN];
int u[MaxN];

int main (void)
{
  int test, tests;
  freopen ("d.in", "rt", stdin);
  freopen ("d.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int n, i, j, sc1 = 0, sc2 = 0;
    scanf ("%d", &n);
    for (i = 0; i < n; i++)
      scanf ("%lf", &naomi[i]);
    for (i = 0; i < n; i++)
      scanf ("%lf", &ken[i]);
   sort (naomi, naomi + n);
   sort (ken, ken + n);
   memset (u, 0, sizeof(u));
   for (i = 0; i < n; i++)
   {
     for (j = 0; j < n; j++)
       if (u[j] == 0 && ken[j] > naomi[i])
       {
         u[j] = 1;
         break;
       }
     if (j == n)
     { 
       sc1 = n - i;
       break;
     }  
   }
   memset (u, 0, sizeof(u));
   for (i = 0; i < n; i++)
   {
     for (j = 0; j < n; j++)
       if (u[j] == 0 && ken[j] < naomi[i])
       {
         u[j] = 1;
         sc2++;
         break;
       }
     if (j == n)
     {
       for (j = n-1; j >= 0; j--)
         if (u[j] == 0 && ken[j] > naomi[i])
         {
           u[j] = 1;
           break;
         }
     }
     if (j == n)
     {
       assert (false);
       for (j = 0; j < n; j++)
         if (u[j] == 0)
         {
           u[j] = 1;
           break;
         }
     }
   }
     
   printf ("Case #%d: %d %d\n", test + 1, sc2, sc1);
  }
  return 0;
}
