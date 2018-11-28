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
#define INF                         (int)1e9
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


void solve(int t)
{
	int n;
	s(n);
	string s;
	cin >> s;
	int cnt=0;
	int ans=0;
	for(int i=0;i<s.size();i++)
	{
		if(s[i]!='0')
		{
			if(cnt < i)
			{
				ans=ans+i-cnt;
				cnt=i;
			}
			cnt=cnt+s[i]-'0';
		}
	}
	printf("Case #%d: %d\n",t,ans);
}	
int main()
{
	int t;
	s(t);
	for(int i=0;i<t;i++)
	{
		solve(i+1);
	}
}