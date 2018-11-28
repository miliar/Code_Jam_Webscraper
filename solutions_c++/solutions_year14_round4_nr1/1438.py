#include <cstdio>
#include <algorithm>
using namespace std;

int n, x, s[10005];

int main()
{
   int nbTests;
   scanf("%d", &nbTests);
   for(int iTest = 1 ; iTest <= nbTests; iTest++)
   {
      scanf("%d%d", &n, &x);
      for(int i=0; i<n; i++)
         scanf("%d", &s[i]);
      sort(s, s+n);
      int i = 0, t = 0;
      for(int j=n-1; j>=i; j--)
      {
         if(s[i] + s[j] <= x)
            i++;
         t++;
      }
      printf("Case #%d: %d\n", iTest, t);
   }
   return 0;
}
