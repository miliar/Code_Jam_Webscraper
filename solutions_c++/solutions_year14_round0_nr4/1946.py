#include <cstdio>
#include <algorithm>
using namespace std;;

double a[1001], b[1001];

int main()
{
   int nbT;
   scanf("%d", &nbT);
   for(int test=0; test<nbT; test++)
   {
      int n;
      scanf("%d", &n);
      for(int i=0; i<n; i++)
         scanf("%lf", &a[i]);
      for(int i=0; i<n; i++)
         scanf("%lf", &b[i]);
      sort(a, a+n);
      sort(b, b+n);

      int r1=0, j=0;
      for(int i=0; i<n; i++)
      {
         while(j<n && b[j] < a[i]){
            j++;
            r1++;
         }
         j++;
      }

      j=0; int k=n-1, r2 = 0;
      for(int i=0; i<n; i++)
      {
         if(a[i] < b[j]) k--;
         else {
            r2++;
            j++;
         }
      }

      printf("Case #%d: %d %d\n", test+1, r2, r1);
   }
   return 0;
}
