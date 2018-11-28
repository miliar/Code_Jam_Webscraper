#include<bits/stdc++.h>
using namespace std;

int n,k;
long double p[30],dp[30][30],a[30],ans;

long double solve()
{
  // for(int i=0;i<2*k;i++)
  //cout<<"************"<<a[i]<<endl;
  memset(dp,0,sizeof dp);
  dp[0][0]=1;
  for(int i=0;i<=k;i++)
    for(int j=0;j<=k;j++)
      if(i+j>0)
	dp[i][j]=(j>0?dp[i][j-1]*a[i+j-1]:0)+(i>0?dp[i-1][j]*(1.0-a[i+j-1]):0);
  return dp[k][k];
}

int main()
{
  int qw;
  cin>>qw;
  for(int q=1;q<=qw;q++)
    {
      ans=0;
      cin>>n>>k;
      k/=2;
      for(int i=0;i<n;i++)
	cin>>p[i];
      for(int i=0;i<(1<<n);i++)
	if(__builtin_popcount(i)==2*k)
	  {
	    int cnt=0;
	    for(int j=0;j<n;j++)
	      if(i&(1<<j))
		{
		  a[cnt++]=p[j];
		  //cout<<cnt<<" "<<a[cnt-1]<<endl;
		}
	    ans=max(ans,solve());
	  }
      cout<<"Case #"<<q<<": ";
      cout<<fixed<<setprecision(7)<<ans<<endl;
    }
}
