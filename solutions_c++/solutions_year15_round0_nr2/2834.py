#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
   int T;
   scanf("%d", &T);
   for(int _i=1; _i<=T; _i++)
   {
      int d;
      vector<int> p;
      scanf("%d", &d);
      int mx = 0;
      for(int i=0; i<d; i++)
      {
         int pi;
         scanf("%d", &pi);
         p.push_back(pi);
         mx = max(pi, mx);
      }
      int m = mx;
      for(int i=1; i<mx; i++)
      {
         int k = 0;
         for(int j=0; j<d; j++)
            k += (p[j]+i-1)/i - 1;
         //printf("%d %d\n", i, k);
         m = min(m, i+k);
      }
      printf("Case #%d: %d\n",_i, m);
   }
   return 0;
}
