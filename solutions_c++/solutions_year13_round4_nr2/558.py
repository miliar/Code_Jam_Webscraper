#include <cstdio>
#include <algorithm>
using namespace std;

long long p2(int k)
{
   long long x = 1;
   for(int i=0; i<k; i++)
      x *= 2;
   return x;
}

int main()
{
   int nbTests;
   scanf("%d", &nbTests);
   for(int iTest=1; iTest<=nbTests; iTest++)
   {
      int n; long long p;
      scanf("%d%lld", &n, &p);
      int k = 0, l = n;
      long long pk = 1, pl = 1, pn = 1;
      for(int i=0; i<n; i++)
         pn *= 2;
      pl = pn;
      while(2*pk <= p)
      {
         pk *= 2;
         k++;
      }
      while(pn - pl / 2 + 1 <= p)
      {
         pl /= 2;
         l--;
      }
     // printf("%lld %lld %lld\n", pn, pk, pl);
     // printf("%d %d\n", k, l);
      long long a, b;
      if(p == pn) a = pn - 1;
      else a = 2*pn/pl - 2;

      b = pn - pn/pk;

      printf("Case #%d: %lld %lld\n", iTest, a, b);
   }
   return 0;
}
