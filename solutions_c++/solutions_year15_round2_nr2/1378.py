#include <bits/stdc++.h>
typedef long long int lli;
#define rep(i,a,b) for(lli i=(a);i<(b);i++)
using namespace std;
 
lli dp[1 << 18];
lli j, C, N;
 
lli mes(lli i)
{
  lli ans = 0;
  rep(r,0,j)
  {
    rep(c,0,C)
    {
      if (c > 0 and (i & (1 << (r * C + c))) and (i & (1 << (r * C + c - 1))))
        ans++;
      if (r > 0 and (i & (1 << (r * C + c))) and (i & (1 << (r * C + c - C))))
        ans++;
    }
  }
  return ans;
}
int main() 
{
  int T;
  cin >> T;
  rep(t,1,T+1)
  {
    cin >> j >> C >> N;
 
    lli maxi = j * C * N * 100;
    rep(i,1,(1 << (j * C)))
    {
      dp[i] = dp[i - (i & -i)] + 1;
      if (dp[i] == N) maxi = min(maxi, mes(i));
    }
    printf("Case #%lld: %lld\n", t, maxi);
  }
  return 0;
}

