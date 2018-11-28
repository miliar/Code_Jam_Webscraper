#include<cstdio>
#include<vector>
#include<queue>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<cmath>
#include <map>
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
#define EPS                         1e-12
 
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
#define mod 1000000009
#define llu long long unsigned
#define ld long
#define INF 1000000000

void solve(int t)
{
	double c;
	double f;
	double x;
	scanf("%lf %lf %lf",&c,&f,&x);
	double mul=2;
	double time=0;
	time=c/2;
	while(1)
	{
		if(((x-c)/mul)<((x/(mul+f))+EPS))
		{
			time=time+(x-c)/mul;
			break;
		}
		else
		{
			mul=mul+f;
			time=time+c/mul;
		}
	}
	printf("Case #%d: %0.7lf\n",t,time);
}
	
	

int main()
{
	int t;
	s(t);
	for(int i=0;i<t;i++)
	solve(i+1);
}