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

#define MAX 10000001
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

VLL v;

bool is_pal(ll n)
{
	ll r=0,m=n;
	while(n)
	{
		r=r*10+(n%10);
		n/=10;
	}
	return m==r;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	FAB(i,1,MAX) if(is_pal(i) && is_pal(i*i)) v.push_back(i*i);		

	int t; cin>>t;
	FR(q,t)
	{		
		printf("Case #%d: ",q+1);
		
		ll a,b; LIN2(a,b);
		
		int beg,en;
		FR(i,v.size())
		{
			if(v[i]>=a)
			{
				beg=i;
				break;
			}
		}
		FR(i,v.size())
		{
			if(v[i]>=b)
			{
				if(v[i]==b) en=i+1;
				else		en=i;
				break;
			}
		}

		printf("%d\n",en-beg);
	}

	return 0;
}