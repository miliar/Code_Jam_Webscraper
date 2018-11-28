/*input
5
0
1
2
11
1692
*/

#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define PII pair<ll, ll>
#define f first
#define s second
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define inf LLONG_MAX
#define mod 1000000007
#define MAXN 100005
#define pb(x) push_back(x)

ll t, n, cnt, ind, tmp;
bool vis[10];

bool func(ll num)
{
	while(num>0)
	{
		ll dig=num%10;
		num/=10;
		if(!vis[dig])
		{
			vis[dig]=1;
			cnt++;
		}
	}
	return cnt==10;
}
int main() 
{
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	cin>>t;
	F(count,1,t)
	{
		cout<<"Case #"<<count<<": ";
		cin>>n;
		memset(vis,0,sizeof(vis));
		cnt=0;
		ind=1;
		if(n==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		while(1)
		{
			tmp=n*ind;
			if(func(tmp))
			{
				cout<<tmp<<endl;
				break;
			}
			ind++;
		}
	}	
	return 0;
}