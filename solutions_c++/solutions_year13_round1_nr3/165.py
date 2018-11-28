#include<cassert>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;

const int NMAX=3;
const int MMAX=5;
const int KMAX=7;

int T,N,M,K,R[KMAX];
int num[NMAX];
ll best; int ans[NMAX];
int cnt[1+78125];
int smp[1+78125];

void dfs(int dep,int x)
{
	if(dep==N)
	{
		if(smp[x]!=T)
		{
			smp[x]=T;
			cnt[x]=1;
		}
		else
		{
			cnt[x]++;
		}
		return;
	}
	dfs(dep+1,x);
	dfs(dep+1,x*num[dep]);
}

void check()
{
	T++;
	dfs(0,1);
	ll mul=1;
	for(int i=0;i<K;i++)
	{
		if(smp[R[i]]!=T)return;
		mul*=cnt[R[i]];
	}
	if(mul>best)
	{
		best=mul;
		memcpy(ans,num,N*sizeof(int));
	}
}

void gen(int dep,int i)
{
	if(dep==N)
	{
		check();
		return;
	}
	do
	{
		num[dep]=i;
		gen(dep+1,i);
	} while(++i<=M);
}

int main()
{
	scanf("%*d");
	puts("Case #1:");
	int t;
	scanf("%d%d%d%d",&t,&N,&M,&K);
	assert(1<=N&&N<=NMAX);
	assert(2<=M&&M<=MMAX);
	assert(1<=K&&K<=KMAX);
	while(t-->0)
	{
		for(int i=0;i<K;i++)scanf("%d",R+i);
		best=0;
		gen(0,2);
		for(int i=0;i<N;i++)putchar('0'+ans[i]);
		putchar('\n');
	}
	return 0;
}
