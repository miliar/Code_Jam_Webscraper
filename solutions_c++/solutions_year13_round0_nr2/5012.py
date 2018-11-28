// File Name: b.cpp
// Author: gonewithsin
// Created Time: 2013/4/13 21:54:22

#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<queue>
#include<map>
using namespace std;

int T;
int n, m;
int a[105][105];

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);	
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++)
	{
		bool ans = 0;
		scanf("%d%d", &n, &m);
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				scanf("%d", &a[i][j]);
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= m; j++)
				if(a[i][j] == 1)
				{
					bool flag = 0;
					for(int k = 1; k <= m; k++)
						if(a[i][k] == 2)
							flag = 1;
					if(!flag)
						continue;
					flag = 0;
					for(int k = 1; k <= n; k++)
						if(a[k][j] == 2)
							flag = 1;
					if(!flag)
						continue;
					ans = 1;
				}
		if(!ans)
			printf("Case #%d: YES\n", cases);
		else
			printf("Case #%d: NO\n", cases);
	}
    return 0;
}
