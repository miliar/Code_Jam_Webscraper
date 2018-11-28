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

bool abc[200];
ll tmp;
bool chck()
{
	ll a,b;
	for(a=0;a<=9;a++)
	{
		if(!abc[a])
		return 0;
	}
	return 1;
}

void color(ll a)
{
	ll b,c;
	tmp=a;
	b=a;
	while(b>0)
	{
		c=b%10;
		b/=10;
		abc[c]=1;
	}
}


int main(void)
{
	ios;
	ll a,n,b,m,c,d,e,t,f;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(f=1;f<=t;f++)
	{
		cin>>n;
		memset(abc,0,sizeof(abc));
		if(!n)
		{
			cout<<"Case #"<<f<<": "<<"INSOMNIA\n";
		}
		else
		{
			m=n;
			while(!chck())
			{
				color(n);
				n+=m;
			}
			cout<<"Case #"<<f<<": "<<tmp<<"\n";
		}
		
	}
	return 0;
}
