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
double a[10000];
double b[10000];
int vis[10000];
void solve(int t)
{
	int n;
	s(n);
	for(int i=0;i<n;i++)
	scanf("%lf",&b[i]);
	for(int i=0;i<n;i++)
	scanf("%lf",&a[i]);
	sort(a,a+n);
	sort(b,b+n);

	int pt=0;
	for(int i=0;i<n;i++)
	vis[i]=0;
	int flag=0;
	for(int i=0;i<n;i++)
	{
		flag=0;
		for(int j=0;j<n;j++)
		{
			if(!vis[j])
			{
				if(a[j]>(b[i]+EPS))
				{
					vis[j]=1;
					flag=1;
					break;
				}
			}
		}
		if(flag == 0)
		{
			pt++;
			for(int j=0;j<n;j++)
			{
				if(!vis[j])
				{
					vis[j]=1;
					break;
				}
			}
		}
	}
	for(int i=0;i<n;i++)
	{
		vis[i]=0;
	}
	int pt1=0;

	for(int i=0;i<n;i++)
	{
		flag=0;
		for(int j=0;j<n;j++)
		{
			if(!vis[j])
			{
				//printf("%lf %lf\n",b[i],a[j]);
				if(b[i] > a[j]+EPS)
				{
					//printf("%d %d\n",j,i);
					flag=1;
					pt1++;
					vis[j]=1;
				}
				else
				{
					flag=0;
				}
				break;
			}
		}
			if(flag == 0)
			{
				for(int j=n-1;j>=0;j--)
				{
					if(!vis[j])
					{
						vis[j]=1;
						break;
					}
				}
			}
	
	}
	printf("Case #%d: %d %d\n",t,pt1,pt);
}
int main()
{
	int t;
	s(t);
	for(int i=0;i<t;i++)
	solve(i+1);
}