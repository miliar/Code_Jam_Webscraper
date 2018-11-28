#include<bits/stdc++.h>
using namespace std;
#define ll long 
#define lim 100005
#define mk make_pair
#define pll pair<ll,ll>
#define pb push_back
#define X first
#define Y second
#define MOD 1000000007
#define ios ios_base::sync_with_stdio(0)




int main(void)
{
	ios;
	ll a,n,b,m,c,d,t,e,f;
	freopen("input2.txt","r",stdin);
	freopen("output2.txt","w",stdout);
	cin>>t;
	for(a=1;a<=t;a++)
	{
		cin>>n;
		ll ans[n];
	bool temp[2*n];
	bool col[n];
	ll i=0;
	ll sum[2600];
		memset(sum,0,sizeof(sum));
		ll abc[2*n][n];
		for(b=0;b<2*n-1;b++)
		{
			for(c=0;c<n;c++)
			{
				cin>>abc[b][c];
				sum[abc[b][c]]++;
			}
		}
		
		for(ll j=0;j<2550;j++)
		{
			if(sum[j]%2)
			{
				ans[i]=j;
				i++;
			}
		}
		sort(ans,ans+n);
		cout<<"Case #"<<a<<": ";
		for(ll j=0;j<n;j++)
		cout<<ans[j]<<" ";
		cout<<endl;
		}
	return 0;
}
