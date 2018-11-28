#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FILL(i,v) memset(i,v,sizeof(i));

int nextint()
{
	int t;
	scanf("%d",&t);
	return t;
}

int cnt[201];
int type[201];
vector<int> val[201];
int used[(1<<20)];
int to[(1<<20)];
int k,n;

int testbit(int n,int m)
{
	return (n>>m)&1;
}

int solve(int cur)
{
	if(!used[cur])
	{
		used[cur]=1;
		to[cur]=n+1;
		if(cur==((1<<n)-1))
			to[cur]=n;
		else
		{
			for(int i=0;i<n;i++)
			{
				if(!testbit(cur,i)&&cnt[type[i]])
				{
					cnt[type[i]]--;
					REP(j,val[i].size())
						cnt[val[i][j]]++;
					if(solve(cur|(1<<i))!=n+1)
					{
						to[cur]=i;
						break;
					}
					REP(j,val[i].size())
						cnt[val[i][j]]--;
					cnt[type[i]]++;
				}
			}
		}
	}
	return to[cur];
}

int main()
{
	int t;
	t=nextint();
	for(int test=1;test<=t;test++)
	{
		FILL(used,0);
		FILL(cnt,0);
		REP(i,201)
			val[i].clear();
		k=nextint();
		n=nextint();
		REP(i,k)
			cnt[nextint()]++;
		REP(i,n)
		{
			type[i]=nextint();
			int k=nextint();
			REP(j,k)
			{
				int tmp=nextint();
				val[i].push_back(tmp);
			}
		}
		printf("Case #%d:",test);
		if(solve(0)==n+1)
			printf(" IMPOSSIBLE\n");
		else
		{
			int cur=0;
			for(int i=0;i<n;i++)
			{
				int t=solve(cur);
				printf(" %d",t+1);
				cur|=(1<<t);
			}
			puts("");
		}
	}
}
