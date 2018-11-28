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
#define llu long long unsigned
#define ld long
#define INF 1000000000
 
 
 #define llu long long unsigned
#define ld long
string a[101];
int pos[101];
int val[101];
void solve(int t)
{
	int n;
	s(n);
	for(int i=0;i<n;i++)
	cin >> a[i];
	string pattern=a[0];
	pattern[0]=a[0][0];
	int cnt=1;
	for(int i=1;i<a[0].size();i++)
	{
		if(a[0][i] != a[0][i-1])
		{
			pattern[cnt]=a[0][i];
			cnt++;
		}
	}
	int cnt1=0;
	for(int i=1;i<n;i++)
	{
		string pattern1;
		cnt1=1;
		pattern1[0]=a[i][0];
		for(int j=1;j<a[i].size();j++)
		{
			if(a[i][j] != a[i][j-1])
			{
				pattern1[cnt1]=a[i][j];
				cnt1++;
			}
		}
		if(cnt != cnt1)
		{
			printf("Case #%d: Fegla Won\n",t);
			return;
		}
		for(int i=0;i<cnt;i++)
		{
			if(pattern1[i]!=pattern[i])
			{
				printf("Case #%d: Fegla Won\n",t);
				return;
			}
		}
	}
	fill(pos,0);
	int ans=0;
	for(int i=0;i<cnt;i++)
	{
		char c=pattern[i];
		fill(val,0);
		for(int j=0;j<n;j++)
		{
			for(int k=pos[j];k<a[j].size();k++)
			{
				if(a[j][k] != c)
				break;
				pos[j]++;
				val[j]++;
			}
		}
		double mean=0;
		int pval;
		for(int j=0;j<n;j++)
		{
			mean=mean+val[j];
		}
		mean=mean/n;
		pval=round(mean);
		for(int j=0;j<n;j++)
		{
			ans = ans+abs(val[j]-pval);
		}
	}
	printf("Case #%d: %d\n",t,ans);
}
	
	
	
	

int main()
{
	int t;
	s(t);
	for(int i=0;i<t;i++)
	solve(i+1);
}