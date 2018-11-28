#include <bits/stdc++.h>

using namespace std;

int main()
{
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      int n; string s;
      cin >> n >> s;
      int r = 0;
      for(int i=0, j=0; i<=n; i++)
      {
         if(i > j)
         {
            r++;
            j++;
         }
         j += s[i] - '0';
      }
      printf("Case #%d: %d\n", test, r);
   }
   return 0;
}