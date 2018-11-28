#include<cstdio>
#include<fstream>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int e,r,n,m,l0,b,l1,l2,l3,p,g;
int dp[100][100];
bool v[100][100];
int a[100];
int main()
{
  freopen("bsmall.in","r",stdin);
  freopen("b.out","w",stdout);
  cin>>m;
  for(l0=1;l0<=m;l0++)
  {
    cin>>e>>r>>n;
    b=0;
    memset(dp,0,sizeof(dp));
    memset(v,0,sizeof(v));
    v[1][e]=1;
    for(l1=1;l1<=n;l1++)
    {
      cin>>a[l1];
      for(l2=0;l2<=e;l2++)
        if(v[l1][l2])
        {
          b=max(b,dp[l1][l2]);
          for(l3=l2;l3>=0;l3--)
          {
            p=min(e,l3+r);
            dp[l1+1][p]=max(dp[l1+1][p],dp[l1][l2]+a[l1]*(l2-l3));
            v[l1+1][p]=1;
            b=max(dp[l1+1][p],b);
          }
        }
    }
    printf("Case #%d: %d\n",l0,b);
  }
  return 0;
}
