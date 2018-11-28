#include <bits/stdc++.h>

using namespace std;

int main()
{
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      int n;
      cin >> n;
      int t[n];
      int m = 0;
      for(int i=0; i<n; i++)
      {
         cin >> t[i];
         m = max(t[i], m);
      }
      int r = 1000000;
      do
      {
         int maxi = 0;
         int nbSpec = 0;
         for(int i=0; i<n; i++)
         {
            int nb = 1 + ((double) t[i]-1e-7) / m;
            //printf("%d %d -> %d\n", t[i], m, nb-1);
            nbSpec += nb - 1;
            maxi = max(maxi, (int) ceil((double) t[i] / nb));
         }
         //printf("Test %d : nbSpec=%d, maxi=%d\n", test, nbSpec, maxi);
         r = min(nbSpec + maxi, r);
      }
      while(--m);
      printf("Case #%d: %d\n", test, r);
   }
   return 0;
}