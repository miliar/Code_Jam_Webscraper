#include <bits/stdc++.h>

#define rep(i,n) for(i=0;i<n;i++)
#define ll long long 
#define elif else if
#define pii pair<ll int,ll int>
#define mp make_pair
#define pb push_back
using namespace std;

int main()
{
  //freopen("A-large.in","r",stdin);
  //freopen("out","w",stdout);
	int T,t;
	cin>>T;
	for (t=1;t<=T;t++)
	{
    int i,j,n,ans=0;
    string st;
    cin>>n>>st;
    int te=0;
    for(i=0;i<=n;i++)
    {
      int num=st[i]-'0';
      if(te<i)
      {
        ans+=(i-te);
        te=i;
      }
      te+=num;
    }
    printf("Case #%d: %d\n",t,ans);
	}
  //Case #1: 0	
	return 0;
}