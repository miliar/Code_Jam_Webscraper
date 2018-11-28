#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define inf 1e18
#define MOD 1000000007
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out5.out","w",stdout);
	ll T;
	scanf("%lld",&T);
	for(ll t=1;t<=T;++t)
	{
		string s;
		cin>>s;
		ll a[26];
		memset(a,0,sizeof(a));
		ll ans[10];
		memset(ans,0,sizeof(ans));
		ll n=s.length();
		for(ll i=0;i<n;++i)
		{
			a[s[i]-65]++;
		}
		ans[0]=a['Z'-65];
		ans[2]=a['W'-65];
		ans[4]=a['U'-65];
		ans[6]=a['X'-65];
		ans[8]=a['G'-65];
		ans[3]=a['R'-65]-ans[0]-ans[4];
		ans[7]=a['S'-65]-ans[6];
		ans[5]=a['V'-65]-ans[7];
		ans[9]=a['I'-65]-ans[5]-ans[6]-ans[8];
		ans[1]=a['N'-65]-2*ans[9]-ans[7];
		printf("Case #%lld: ",t);
		for(ll i=0;i<10;++i)
		{
			while(ans[i])
			{
				cout<<i;
				ans[i]--;
			}
		}
		cout<<endl;
	}
	return 0;
}
