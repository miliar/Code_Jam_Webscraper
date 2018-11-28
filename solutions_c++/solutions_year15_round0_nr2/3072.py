#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define INF 100000000
int t;
static ll data[1010];
static ll idata[1010];
inline void solve(void)
{
  cin>>t;
  for(ll z=1;z<=t;z++)
  {
      ll d;
      cin>>d;
      for(ll i =0;i<d;i++)
      scanf("%lld",&data[i]);
      ll mini = 1000000000;
      ll res = 0;
      for(ll i = 1;i<=1000; i++)
      {
		  res = i;
        for(ll j = 0; j<d;j++)
        {
          if(data[j]>i)
          {
            ll div = (data[j]/i);
            if(data[j]%i == 0)
            {
              res+=(div-1);
            }
            else
            {
              res+= div;
            }
          }
        }
        mini = min(mini,res);
      }
      printf("Case #%lld: %lld\n",z,mini);
  }
}

int main()
{
  solve();
  return 0;
}
