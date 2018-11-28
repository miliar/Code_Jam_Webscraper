#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
#define vi vector<int>
#define vs vector<string>
#define vl vector<LL>
#define pb push_back
#define endl "\n"

#define MAXN 1010

int dp[MAXN][MAXN];

void initdp()
{
   for (int i=1;i<MAXN;++i) for(int j=1;j<MAXN;++j)
   {
      if (j >= i) dp[i][j] = 0;
      else if (i==1) dp[i][j] = 1;
      else if (j == 1) dp[i][j] = i-1;
      else {
         dp[i][j] = i / j;
         if (i % j == 0) dp[i][j]--;
         for (int b = 2; b < i; b++)
         {
            dp[i][j] = min(dp[i][j], 1 + dp[i-b][j] + dp[b][j]);
         }
      }
   }
}

LL solve()
{
   vector<LL> v;
   LL D;
   cin >> D;
   LL maxelem = 0;
   for (LL i=0; i < D; ++i)
   {
      LL p;
      cin >> p;
      v.pb(p);
      maxelem = max(maxelem,p);
   }

   LL ans = maxelem;
   for (LL i = 1; i <= maxelem; ++i)
   {
      LL silent = 0;
      for(auto j : v)
      {
         silent += dp[j][i];
      }
      ans = min(ans, silent + i);
   }

   return ans;
}

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   initdp();
   for (int i = 1; i <= T; ++i)
   {
      LL ret = solve();
      cout  << "Case #" << i << ": " << ret << endl;
   }

   return 0;
}
