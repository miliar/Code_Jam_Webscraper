/*************************************************************************
	> File Name: B.cpp
	> Author: Canoe
	> Mail: canoefzh@gmail.com 
	> Created Time: Sat 13 Apr 2013 08:45:02 PM CST
 ************************************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <ctime>

using namespace std;

const int oo = (1 << 20);
const int N = 128;

int dat[N][N], pre[N][N];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tcas, cas = 0;
	scanf("%d", &tcas);
	while(tcas -- )
	{
		int n, m;
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				scanf("%d", &dat[i][j]);
			}
		}
		bool isYes = true;
		while(true)
		{
			int Min = oo;
			for(int i = 0; i < n; i++)
			{
				for(int j = 0; j < m; j++)
				{
					Min = min(dat[i][j], Min);
				}
			}
			memcpy(pre, dat, sizeof(dat));
			if(Min > 110) break;
			bool isBreak = true;
			for(int j = 0; j < m; j++)
			{
				bool flag = true;
				for(int i = 0; i < n; i++)
				{
					if(dat[i][j] != Min)
						flag = false;
				}
				if(flag)
				{
					isBreak = false;
					for(int i = 0; i < n; i++)
						pre[i][j] = Min + 1;
				}
			}
			for(int i = 0; i < n; i++)
			{
				bool flag = true;
				for(int j = 0; j < m; j++)
				{
					if(dat[i][j] != Min)
						flag = false;
				}
				if(flag)
				{
					isBreak = false;
					for(int j = 0; j < m; j++)
						pre[i][j] = Min + 1;
				}
			}
			if(isBreak)
			{
				isYes = false;
				break;
			}
			memcpy(dat, pre, sizeof(pre));
		}
		printf("Case #%d: %s\n", ++cas, isYes ? "YES" : "NO");
	}
	return 0;
}
