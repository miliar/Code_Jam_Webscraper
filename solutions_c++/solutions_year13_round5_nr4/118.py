#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <cassert>
using namespace std;
typedef long long ll;
#define REP(i,n) for(int i=0;i<(n);i++)

int n;
char pat[201];

double dp[(1<<20)];
int used[(1<<20)];

int testbit(int n, int m)
{
	return (n>>m)&1;
}

double solve(int mask)
{
	if(!used[mask])
	{
		used[mask]=1;
		if(mask==(1<<n)-1)
			dp[mask]=0;
		else
		{
			int prev=-1;
			int cnt=0;
			for(int i=0;i<n;i++)
				if(!testbit(mask,i))
				{
					if(prev==-1)
						prev=i;
					cnt++;
				}
			dp[mask]=0;
			for(int i=n-1;i>=0;i--)
			{
				if(!testbit(mask,i))
					prev=i;
				dp[mask]+=solve(mask|(1<<prev))+(n-(prev-i+n)%n);
			}
			dp[mask]/=n;
		}
	}
	return dp[mask];
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		scanf("%s",pat);
		n=strlen(pat);
		REP(i,(1<<n))
			used[i]=0;
		int start=0;
		REP(i,n)
			if(pat[i]=='X')
				start|=(1<<i);
		printf("Case #%d: %.10lf\n",test,solve(start));
	}
	return 0;
}
