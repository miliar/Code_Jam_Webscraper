#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define INF 100000000
int t;
static char data[1010];
static ll idata[1010];
inline void solve(void)
{
  cin>>t;
  for(ll i=1;i<=t;i++)
  {
    ll sm;
    scanf("%lld",&sm);
    scanf("%s",data);
    ll l = strlen(data);
    for(ll j=0;j<l;j++)
      idata[j] = data[j]-'0';
    if(sm == 0)
    {
      printf("Case #%lld: 0\n",i);
    }
    else
    {
      ll cul = 0;
      cul+=idata[0];
      ll res = 0;
      for(ll j = 1;j<l;j++)
      {
        if(j>cul)
        {
          res+=(j-cul);
          cul+=(j-cul);
          cul+=idata[j];
        }
        else
          cul+=idata[j];
      }
      printf("Case #%lld: %lld\n",i,res);
    }
  }
}

int main()
{
  solve();
  return 0;
}
