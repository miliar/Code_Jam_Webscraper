#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

int t,n,j,cnt;
bool f[40];
long long s[10],top;

void calc(long long k, long long &p)
{
	long long x = 0;
	p = 0;
	for(int i = 0; i < n; i++)
		x = x * k + f[i];
	for(long long i = 2; i < sqrt(x) + 1; i++)
		if(x % i == 0)
		{
			p = i;
			break;
		}
}

void Dfs(int x)
{
	if(x == n-1)
	{
		int ans = true;
		memset(s,0,sizeof(s));
		for(int i = 2; i <= 10 && ans; i++)
		{
			calc(i,s[i]);
			if(s[i] == 0)
				ans = false;
		}
		if(ans)
		{
			cnt++;
			for(int i = 0; i < n; i++)
				printf("%d",f[i]);
			for(int i = 2; i <= 10; i++)
				printf(" %lld",s[i]);
			printf("\n");
		}
		return;
	}
	Dfs(x+1);
	if(cnt == j)
		return;
	f[x] = 1;
	Dfs(x+1);
	if(cnt == j)
		return;
	f[x] = 0;
	return;
}

int main()
{
	freopen("g3.in","r",stdin);
	freopen("g3.out","w",stdout);
	scanf("%d",&t);
	for(int ii = 1; ii <= t; ii++)
	{
		scanf("%d%d",&n,&j);
		memset(f,0,sizeof(f));
		cnt = 0;
		printf("Case #%d:\n",ii);
		f[0] = 1;
		f[n-1] = 1;
		Dfs(1);
	}
	return 0;
}
