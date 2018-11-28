#include<stdio.h>
#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<sstream>
#include<set>
#include<map>
#include<stack>
#include<cmath>
#include <map>
#include<cstdlib>
#include<cstring>
#include<string>
#include<set>
using namespace std;
 
#define DEBUG //on-off switch for printing statements
 
// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
 
// Useful constants
#define INF                         (long long)1e18
#define EPS                         1e-9
 
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
 
// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())

#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
 
// Some common useful functions
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
 
#define ll long long int
#define mod 1000000007
#define F first
#define S second
#define pb push_back
#define B 27

ll n,b;
ll arr[10009], ans[10009];

int isvalid(ll val)
{
	ll sum=0;

	for(int i=0;i<b;i++)
	{
		sum += val/arr[i];
		if(val%arr[i] != 0) sum++;
	}

	if(sum <= n-1) return 1;
	return 0;

}

void solve(int t)
{
	sl(b);
	sl(n);

	for(int i=0;i<b;i++)
	{
		sl(arr[i]);
	}

	if(n==1) printf("Case #%d: 1\n",t);


	ll s = 	0, e = 1000000000000000L;

	while(e-s>1)
	{
	  ll	m=(e+s)/2;

		if(isvalid(m)==1)
		{
			s=m;
		}
		else
		{
			e=m;
		}

	}

	fill(ans,0);
	ll sum=0,fin=0;

	for(int i=0;i<b;i++)
	{
		sum += s/arr[i];
		fin += s/arr[i];
		if(s%arr[i] != 0) sum++;
		ans[i]= (arr[i] - (s)%arr[i])%arr[i];
		//cout<<fr[i]<<" , ";
	}

	//cout<<endl;
	//cout<<fin<<"  "<<sum<<" "<<s<<endl;
	ll mini=INF;
	int fidx;
	while(1)
	{
		mini=INF;

		
		for(int i=0;i<b;i++)
		{
			if(ans[i]<mini)
			{
				mini=ans[i];
				fidx=i;
			}
		}



		for(int i=0;i<b;i++)
		{
			ans[i] = ((ans[i] - mini));

		}

		ans[fidx]=arr[fidx];


		fin++;
		sum++;
		if(sum==n)
		{
			printf("Case #%d: %d\n",t,fidx+1);
			//cout<<fidx+1<<endl;
			return ;
		}


	}
}
int main()
{
	int t;
	s(t);
	for(int i=0;i<t;i++)
	solve(i+1);

}