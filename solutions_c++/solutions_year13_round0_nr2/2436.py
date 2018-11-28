#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>

using namespace std;

typedef long long LL;

typedef struct
{
	int type;
	int pos;
	int value;
}ss;

int t,n,m;
ss s[210];
int a[110][110],b[110][110];

int cmp(const void *a, const void *b)
{
	return (*(ss *)b).value - (*(ss *)a).value;
}

void tran(int i)
{
	int j;
	if(s[i].type)
	{
		for(j = 0; j < n; j++)
			b[j][s[i].pos] = min(b[j][s[i].pos], s[i].value);
	}
	else
	{
		for(j = 0; j < m; j++)
			b[s[i].pos][j] = min(b[s[i].pos][j], s[i].value);
	}
}

int pd()
{
	int i,j;
	for(i = 0; i < n; i++)
		for(j = 0; j < m; j++)
			if(a[i][j] != b[i][j]) return 0;
	return 1;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	int cnt;
	int i,j,k,tem;
	for(cnt = 1; cnt <= t; cnt++)
	{
		scanf("%d%d", &n, &m);
		k = 0;
		for(i = 0; i < n; i++)
		{
			tem = 0;
			for(j = 0; j < m; j++)
			{
				scanf("%d", &a[i][j]);
				tem = max(tem, a[i][j]);
			}
			s[k].type = 0;
			s[k].pos = i;
			s[k++].value = tem;
		}
		for(j = 0; j < m; j++)
		{
			tem = 0;
			for(i = 0; i < n; i++)
				tem = max(tem, a[i][j]);
			s[k].type = 1;
			s[k].pos = j;
			s[k++].value = tem;
		}
		qsort(s, k, sizeof(s[0]), cmp);
		for(i = 0; i < n; i++)
			for(j = 0; j < m; j++)
				b[i][j] = 100;
		for(i = 0; i < k; i++)
			tran(i);
		printf("Case #%d: ", cnt);
		if(pd()) puts("YES");
		else puts("NO");
	}
	return 0;
}