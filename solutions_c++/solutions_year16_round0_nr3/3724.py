/*input

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

ll n, j, cnt;
ll powNum[35][15];
ll arr[]={2,3,5,7,11,13,17,19,23,29};
ll ans[15];
void pre()
{
	F(j,2,10)
		powNum[0][j]=1;
	F(i,1,15)
		F(j,2,10)
			powNum[i][j]=powNum[i-1][j]*j;
}
int main() 
{
	pre();
	cout<<"Case #1:"<<endl;
	F(i,0,1<<13)
	{
		bool flag=1;
		F(j,2,10)
		{
			bool f=0;
			n=1+powNum[15][j];
			F(k,0,13)
				if((1<<k) & i)
					n+=powNum[k+1][j];
			F(k,0,9)
			{
				if(n%arr[k]==0)
				{
					ans[j]=arr[k];
					f=1;
					break;
				}
			}
			if(!f)
			{
				flag=0;
				break;
			}
		}
		if(flag)
		{
			cnt++;
			cout<<n<<" ";
			F(j,2,10)
				cout<<ans[j]<<" ";
			cout<<endl;
		}
		if(cnt==50)
			break;
	}	
	return 0;
}