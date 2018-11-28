#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <string.h>
#include <math.h>
#include <algorithm>

using namespace std;

double nao[1010], ken[1010];
int visit[1010];

int main (void)
{
	freopen("D:\\D-large.in", "r", stdin);
	freopen("D:\\D-large-out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int ca = 0;
	while(t--)
	{
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
			scanf("%lf", &nao[i]);
		for(int j = 0; j < n; ++j)
			scanf("%lf", &ken[j]);
		memset(visit, 0, sizeof(visit));
		int y, z;
		y = 0; z = 0;
		for(int i = 0; i < n; ++i)
		{
			int res = -1;
			int flag = 0;
			for(int j = 0; j < n; ++j)
			{
				if(nao[i] < ken[j] && !visit[j])
				{
					if(!flag || ken[res] > ken[j])
						res = j;
					flag = 1;
				}
				if(!flag && !visit[j])
				{
					if(res == -1 || ken[res] > ken[j])
						res = j;
				}
			}
			if(!flag)
				++z;
			visit[res] = 1;
		}
		memset(visit, 0, sizeof(visit));
		for(int i = 0; i < n; ++i)
		{
			int res = -1;
			int flag = 0;
			for(int j = 0; j < n; ++j)
			{
				if(ken[i] < nao[j] && !visit[j])
				{
					if(!flag || nao[res] > nao[j])
						res = j;
					flag = 1;
				}
				if(!flag && !visit[j])
				{
					if(res == -1 || nao[res] > nao[j])
						res = j;
				}
			}
			if(flag)
				++y;
			visit[res] = 1;
		}
		printf("Case #%d: %d %d", ++ca, y, z);
		printf("\n");
	}
	return 0;
}