#include<bits/stdc++.h>
#define ll long long int
#define mod 1000000007
#define X first
#define Y second
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
#define forn(n) for(ll i=0;i<n;i++)
#define forin(n1,n2) for(ll i=n1;i<n2;i++)
using namespace std;
typedef pair<int,int>pii;
FILE *ptr=freopen("in.txt","r",stdin);
FILE *ptr1=freopen("out.txt","w",stdout);
int main()
{
	ll tc;
	cin>>tc;
	forn(tc)
	{
		string s;cin>>s;
		ll k,flag=1; cin>>k;
		ll ans=0;
		for(int j=0;j+k<=s.length();j++)
		{
			if(s[j]=='-')
			{
				ans++;
				for(int p=j;p<j+k;p++)
				{
					if(s[p]=='+') s[p]='-';
					else s[p]='+';
				}
			}
		}
		for(int h=s.length()-k+1;h<s.length();h++) if(s[h]=='-') flag=0;
		if(flag)
		cout<<"Case #"<<i+1<<": "<<ans<<"\n";
		else
		cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<"\n";
	}
	return 0;
}

