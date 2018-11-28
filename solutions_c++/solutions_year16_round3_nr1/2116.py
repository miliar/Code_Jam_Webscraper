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

ll bo;
ll maxi(ll abc[],ll n)
{
	ll a,c,d;
	bo=-2;
	c=0;
	for(a=0;a<n;a++)
	{
		if(abc[a]>bo)
		{
			bo=abc[a];
			c=a;
		}
	}
	return c;
}

bool chck(ll abc[],ll n)
{
	ll a,b,c,d;
	ll sum=0;
	b=-2;
	for(a=0;a<n;a++)
	{
		sum+=abc[a];
		b=max(abc[a],b);
	}
	if(2*b>sum)
	return 0;
	else
	return 1;
}

int main(void)
{
	ios;
	ll a,n,b,m,c,d,e,t,f;
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	bool count[200]={0};
	for(f=1;f<=t;f++)
	{
		cout<<"Case #"<<f<<": ";
		memset(count,0,sizeof(count));
		cin>>n;
		ll abc[100];
		for(ll i=0;i<n;i++)
		cin>>abc[i];
		while(1)
		{
			c=maxi(abc,n);
			if(bo==0)
			break;
			cout<<(char)('A'+c);
			abc[c]--;
			if(!chck(abc,n))
			{
			c=maxi(abc,n);
			if(bo==0)
			break;
			cout<<(char)('A'+c);
			abc[c]--;
			}
			cout<<" ";
		}
		cout<<endl;
	}
	return 0;
}
