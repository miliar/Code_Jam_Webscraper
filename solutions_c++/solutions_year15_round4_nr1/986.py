#include<string>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<vector>
#include<iostream>
#include<deque>
#include<queue>
#include<set>
#pragma comment(linker, "/STACK:102400000,102400000")
#define LL __int64
#define eps 1e-8
#define zero(x) ((x > +eps) - (x < -eps))
#define mem(a,b) memset(a,b,sizeof(a))
#define MOD 1000000007
#define INF 99999999
#define MAX 110
using namespace std;

int n, m, ans;
char str[MAX][MAX];
char dir[5] = {"^>v<"};

bool solve(int x, int y, int dir)
{
	if(dir == 0)
	{
		for(int i = x - 1; i >= 0; -- i) 
		{
			if(str[i][y] != '.')
			{
				return true;
			}
		}
		return false;
	}
	if(dir == 1)
	{
		for(int i = y + 1; i < m; ++ i)
		{
			if(str[x][i] != '.') 
			{
				return true;
			}
		}
		return false;
	}
	if(dir == 2)
	{
		for(int i = x + 1; i < n; i ++)
		{
			if(str[i][y] != '.')
			{
				return true;
			}
		}
		return false;
	}
	if(dir == 3)
	{
		for(int i = y - 1; i >= 0; i --)
		{
			if(str[x][i] != '.') 
			{
				return true;
			}
		}
		return false;
	}
	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ii = 1; ii <= t; ii ++)
	{
		scanf("%d%d",&n,&m);
		for(int i = 0; i < n; ++ i)
		{
			scanf("%s",str[i]);
		}
		ans = 0;
		int flag = 0;
		for(int i = 0; i < n; i ++)
		{
			for(int j = 0; j < m; j ++)
			{
				if(str[i][j] == '.')
				{
					continue;
				}
				int f = 0;
				for(int k = 0; k < 4; k ++) 
				{
					if(solve(i,j,k)) 
					{
						if(dir[k] == str[i][j]) 
						{
							f = 1;
							break;
						}
						else 
						{
							f = 2;
						}
					}
				}
				if(!f) 
				{
					flag = 1;
					break;
				}
				if(f == 2) 
				{
					ans ++;
				}
			}
			if(flag)
			{
				break;
			}
		}
		if(flag)
		{
			printf("Case #%d: IMPOSSIBLE\n",ii);
			continue;
		}
		printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}