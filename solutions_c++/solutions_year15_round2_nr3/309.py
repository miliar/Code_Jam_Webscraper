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
      long long t[n][3];
      for(int i=0; i<n; i++)
         cin >> t[i][0] >> t[i][1] >> t[i][2];
      int r;
      if(n == 1)
         r = 0;
      else
      {
         long long a1 = (360-t[0][0]) * t[0][2];
         long long a2 = a1 + 360 * t[0][2];
         long long b1 = (360-t[1][0]) * t[1][2];
         long long b2 = b1 + 360 * t[1][2];
         r = max(a1, b1) >= min(a2, b2);
      }
      printf("Case #%d: %d\n", test, r);
   }
   return 0;
}