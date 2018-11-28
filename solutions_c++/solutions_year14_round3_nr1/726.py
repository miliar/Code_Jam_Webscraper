#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<cmath>
#include <map>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cassert>
using namespace std;
 
#define DEBUG //on-off switch for prlling statements
 
// Input macros
#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
 
// Useful constants
#define EPS                         1e-15
 
// Useful hardware instructions
#define bitcount1                    __builtin_popcount1
#define gcd                         __gcd
 
// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(ll i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((ll)(a.size()))
 
// Some common useful functions
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
 
#define ll long long int
#define llu long long unsigned
#define ld long
#define INF 1000000000
 
 
 #define llu long long unsigned
#define ld long
ll gcd(ll a,ll b)
{
	if(a<b)
	return gcd(b,a);
	if(b == 0)
	return a;
	return gcd(b,a%b);
}
void solve(int t)
{
	ll p;
	ll q;
	scanf("%lld/%lld",&p,&q);
	ll val=gcd(p,q);
	p=p/val;
	q=q/val;
	int flag=0;
	ll no=1;
	int idx;
	for(int i=0;i<=40;i++)
	{
		if(q==no)
		{
			flag=1;
			idx=i;
			break;
		}
		no=no*2;
	}
	if(flag == 0)
	{
		printf("Case #%d: impossible\n",t);
		return;
	}
	double ans=1;
	double value=(double)p/q;
	for(int i=0;i<=40;i++)
	{
		if(value > ans-EPS)
		{
			printf("Case #%d: %d\n",t,i);
			return;
		}
		ans=ans/2;
	}
	printf("Case #%d: impossible\n",t);
}

int main()
{
	int t;
	s(t);
	for(int i=0;i<t;i++)
	solve(i+1);
}