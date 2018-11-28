#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <functional>
#define pb push_back
#define mp make_pair
#define ST begin()
#define ED end()
#define XX first
#define YY second
#define elif else if 
#define foreach(i,x) for (__typeof((x).ST) i=(x).ST;i!=(x).ED;++i) 
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vci;
typedef vector<string> vcs;
typedef pair<int,int> PII;

const int N = 2005;

int n, m;
int a[N], b[N], d[N], ans[N], p[N];
int g[N][N];
set<int, greater<int> > f;

int check()
{
	memset(p, 0, sizeof p);
	for (int i=1;i<=n;++i)
		for (int j=0;j<i;++j)
			if (ans[j]<ans[i]&&p[j]+1>p[i])
				p[i]=p[j]+1;
	/*
	for (int i=1;i<=n;++i)
		printf("%d ", p[i]);
	printf("\n");*/
	for (int i=1;i<=n;++i)
		if (p[i]!=a[i])
			return 0;
	memset(p, 0, sizeof p);
	for (int i=n;i>=1;--i)
		for (int j=i+1;j<=n+1;++j)
			if (ans[j]<ans[i]&&p[j]+1>p[i])
				p[i]=p[j]+1;
	/*
	for (int i=1;i<=n;++i)
		printf("%d ", p[i]);
	printf("\n");*/
	for (int i=1;i<=n;++i)
		if (p[i]!=b[i])
			return 0;
}

int main()
{
	freopen("C-large.in","r",stdin);
	//freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int task;
	scanf("%d", &task);
	for (int _i=1;_i<=task;++_i)
	{
		scanf("%d", &n);
		memset(g, 0, sizeof g);
		memset(d, 0, sizeof d);
		for (int i=1;i<=n;++i)
		{
			scanf("%d", &a[i]);
			for (int j=i-1;j>=1;--j)
			{
				if (a[j]==a[i])
				{
					++g[i][j],++d[i];
//					printf("%d < %d\n", i, j);
				}
			}
			for (int j=i-1;j>=1;--j)
				if (a[j]==a[i]-1)
				{
					++g[j][i],++d[j];
//					printf("%d < %d\n", j, i);
					break;
				}
		}
		for (int i=1;i<=n;++i)
			scanf("%d", &b[i]);
		for (int i=n;i>=1;--i)
		{
			for (int j=i+1;j<=n;++j)
			{
				if (b[j]==b[i])
				{
					++g[i][j],++d[i];
//					printf("%d < %d\n", i, j);
				}
			}
			for (int j=i+1;j<=n;++j)
				if (b[j]==b[i]-1)
				{
					++g[j][i];
					++d[j];
//					printf("%d < %d\n", j, i);
					break;
				}
		}
		f.clear();
		for (int i=1;i<=n;++i)
			if (d[i]==0)
				f.insert(i);
		memset(ans, 0, sizeof ans);
		for (int i=n;i>=1;--i)
		{
			if (f.empty())
			{
				puts("fuckly");
				break;
			}
			int x=*f.begin();
			f.erase(x);
			ans[x]=i;
			for (int j=1;j<=n;++j)
				if (g[j][x])
				{
					d[j]-=g[j][x];
					if (d[j]==0)
						f.insert(j);
				}
		}
		printf("Case #%d:", _i);
		for (int i=1;i<=n;++i)
			printf(" %d", ans[i]);
		printf("\n");
		if (!check())
		{
			puts("fuckly");
		}
	}

	return 0;
}
