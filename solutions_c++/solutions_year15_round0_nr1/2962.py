#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
   int T;
   scanf("%d", &T);
   for(int _i=1; _i<=T; _i++)
   {
      int n;
      char s[1001];
      scanf("%d %s", &n, s);
      int t = 0, m = 0;
      for(int i = 0; i <= n; i++)
      {
         int d = max(i - t, 0);
         m += d;
         t += d + (s[i] - '0');
      }
      printf("Case #%d: %d\n",_i, m);
   }
   return 0;
}
