#include <bits/stdc++.h>

using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define abs(x) ((x)<0?-(x):(x))
#define pii pair<int,int>
#define m_p make_pair(n,m)
#define mod 1000000007
#define pb push_back
#define bp(x) __builtin_popcount(x)
typedef long long int ll;
ll ipow(int a, int b)
{
	ll x=1,y=a; 
	while(b > 0)
	{
		if(b%2 == 1)
		{
			x=(x*y);
		}
		y = (y*y);
		b /= 2;
	}
	return x;
}
int main()
{
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	ios::sync_with_stdio(false);cin.tie(0);
	int t,n,i,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		int k,c,s;
		ll sum;
		cin>>k>>c>>s;
		ll d=ipow(k,c-1);
		cout<<"Case #"<<z<<": ";
		cout<<1<<" ";
		sum=0;
		for(i=1;i<k;i++)
		{
			sum=sum+d;
			cout<<sum+1<<" ";
		}
		cout<<"\n";
	}
	return 0;
}
