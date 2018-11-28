#include<iostream>
#include<cstring>
#include<string>

#define FOR(i,n) for(ll i=0; i<n; ++i)
#define FOR1(i,n) for(ll i=1; i<=n; ++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define ll long long

using namespace std;


int digs[10];

bool mark(ll n)
{
	while(n>0)
	{
		digs[n%10]=1;
		n/=10;
	}
	FOR(i,10) if(digs[i]==0) return 0;
	return 1;
}

ll find(ll n)
{
	ll sum=n;
	while(mark(sum)==0) sum+=n;
	return sum;
}
int main()
{
	int T; cin>>T;
	FOR1(i,T)
	{
		ll x; cin>>x;		
		cout<<"Case #"<<i<<": ";		
		if(x==0) cout<<"INSOMNIA\n";
		else
		{
			CLR(digs,0);
			cout<<find(x)<<endl;		
		}
	}
}
