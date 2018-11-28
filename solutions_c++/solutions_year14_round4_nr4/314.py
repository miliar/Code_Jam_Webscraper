#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define int64 long long
#define Sort sort

using namespace std;

char a[10][20];
int b[10];
int son[100][26];
int N,M,worst,cnt;
int tot;

void insert(int j)
{
	int now = 1;
	for (int k=0;k<strlen(a[j]);++k)
	{
		int x = a[j][k] - 'A';
		if (son[now][x] == 0) son[now][x] = ++ tot;
		now = son[now][x];
	}
}

void check()
{
	int res = 0;
	for (int i=0;i<N;++i)
	{
		memset(son,0,sizeof(son));
		tot = 1;
		for (int j=0;j<M;++j)
			if (b[j] == i)
				insert(j);
		if (tot == 1) return;
		res += tot;
	}
	if (res > worst)
	{
		worst = res;
		cnt = 0;
	}
	if (res == worst) ++cnt;
}

void dfs(int x)
{
	if (x == M)
	{
		check();
		return;
	}
	for (int i=0;i<N;++i)
	{
		b[x] = i;
		dfs(x+1);
	}
}

int main()
{
	freopen("input1.in","r",stdin);
	freopen("output1.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	for (int ii=0;ii<T;++ii)
	{
		printf("Case #%d: ",ii+1);
		scanf("%d%d",&M,&N);
		for (int i=0;i<M;++i)
			scanf("%s",a[i]);
		worst = 0;
		cnt = 0;
		dfs(0);
		printf("%d %d\n",worst,cnt);
	}
		
	return 0;
}