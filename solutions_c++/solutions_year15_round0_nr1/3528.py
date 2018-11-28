#include<bits/stdc++.h>
using namespace std;
#define ll long long 
#define fast() {cin.sync_with_stdio(false);cin.tie(false);cout.tie(false);}
#define pb push_back
#define mp make_pair
int main()
{
	fast();
	//freopen("A-large.in","r+",stdin);
    //freopen("output.txt","w+",stdout);
	ll t;
	cin>>t;
	ll test=0;
	while(t--)
	{
		test++;
		ll n;
		cin>>n;
		string s;
		cin>>s;
		ll ans=0;
		ll cnt=0;
		for(int i=0;i<=n;i++)
		{
			if(i>cnt)
			 {ans+=(i-cnt);cnt+=(i-cnt);}
			cnt += (int)(s[i]-'0');
		}
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
}
