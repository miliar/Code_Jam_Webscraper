#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <cmath>
#include <queue>

using namespace std;

#define MAX 5000
#define INF 10000000000000
#define MOD 1000000009
#define CLR(a,x) memset(a,x,sizeof a)
#define ll long long
#define ALL(v) v.begin(),v.end()
#define FR(i,n) for(ll i=0;i<n;i++)
#define FAB(i,a,b) for(ll i=a;i<b;i++)
#define FBA(i,b,a) for(ll i=b;i>=a;i--)
#define IIN(x) scanf("%d",&x)
#define IIN2(x,y) scanf("%d%d",&x,&y)
#define LIN(x) scanf("%I64d",&x)
#define LIN2(x,y) scanf("%I64d%I64d",&x,&y)
#define PII pair<int,int>
#define PI 3.141592653589793238
#define VI vector<int>
#define VLL vector<ll>
#define VS vector<string>
#define SI set<int>
#define SLL set<ll>
#define SS set<string>
#define MII map<int,int>
#define MIV map<int,VI>
#define MSI map<string,int>
#define MIS map<int,string>
#define PLL pair<ll,ll>
#define PIS pair<int,string>

ll a,n,res;
VLL v;

void back(ll pos,ll sum,ll cnt)
{
	if(pos==n)
	{
		res=min(res,cnt);
		return;
	}

	if(v[pos]<sum)
	{
		back(pos+1,sum+=v[pos],cnt);
		return;
	}
	if(v[pos]<sum*2-1)
	{
		back(pos,sum*2-1,cnt+1);
		return;
	}
	else
	{
		back(pos,sum*2-1,cnt+1);
		back(pos+1,sum,cnt+1);
	}

}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);



	ll T; cin>>T;
	FR(q,T)
	{
		cout<<"Case #"<<q+1<<": ";

		v.clear();
		cin>>a>>n;
		FR(i,n) 
		{
			ll x; cin>>x;
			v.push_back(x);
		}
		sort(ALL(v));

		if(a==1)
		{
			cout<<n<<endl;
			continue;
		}

		res=100000;
		back(0,a,0);

		cout<<res<<endl;
	}

	return 0;
}