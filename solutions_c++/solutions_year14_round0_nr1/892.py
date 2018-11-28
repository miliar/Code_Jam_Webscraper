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
#define EPS                         1e-5
 
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
int a[4][4];
int b[4][4];
vector<int> ans;
vector<int> ans1;
vector<int> ans2;
void solve(int t)
{
	int n1;
	s(n1);
	ans.clear();
	ans1.clear();
	ans2.clear();
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			s(a[i][j]);
		}
	}
	n1--;
	for(int i=0;i<4;i++)
	ans2.pb(a[n1][i]);
	int n2;
	s(n2);
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			s(b[i][j]);
		}
	}
	n2--;
	int cnt=0;
	for(int i=0;i<4;i++)
	{
		ans1.pb(b[n2][i]);
	}
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(ans2[i] == ans1[j])
			ans.pb(ans2[i]);
		}
	}
	if(ans.size() == 1)
	{
		printf("Case #%d: %d\n",t,ans[0]);
	}
	else if(ans.size() > 1)
	{
		printf("Case #%d: Bad magician!\n",t);
	}
	else
	{
		printf("Case #%d: Volunteer cheated!\n",t);
	}
}
int main()
{
	int t;
	s(t);
	for(int i=0;i<t;i++)
	solve(i+1);
}