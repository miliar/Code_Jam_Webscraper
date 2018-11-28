//*
#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <queue>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <functional>
#define MOD 1000000007
#define MAX ((1<<30)-1)
#define MAX2 ((1ll<<62)-1)
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef set<int>::iterator siit;

int n, m;
char a[200][200];

int mang;

int dir[4][2]={-1, 0, 0, 1, 1, 0, 0, -1};

int isvalid(int x, int y)
{
	return x >= 0 && y >= 0 && x < n && y < m;
}

int isexist(int x, int y, int d)
{
	int i;
	int flag=0;
	int nx=x+dir[d][0], ny=y+dir[d][1];
	for(i=0;;i++)
	{
		if(!isvalid(nx, ny)) break;
		if(a[nx][ny] != '.')
		{
			flag=1;
			break;
		}
		nx+=dir[d][0], ny+=dir[d][1];
	}
	return flag;
}

int main()
{
	int t, tt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tt);
	for(t=0;t<tt;t++)
	{
		int i, j, k;
		mang=0;
		scanf("%d%d", &n, &m);
		for(i=0;i<n;i++) scanf("%s", a[i]);
		int cnt=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				int x;
				if(a[i][j] == '.') continue;
				if(a[i][j] == '^') x=0;
				else if(a[i][j] == '>') x=1;
				else if(a[i][j] == 'v') x=2;
				else x=3;
				if(isexist(i, j, x)) continue;
				int fflag=0;
				for(k=0;k<4;k++)
				{
					if(x == k) continue;
					if(isexist(i, j, k))
					{
						fflag=1;
						break;
					}
				}
				if(fflag == 0)
				{
					mang=1;
					break;
				}
				cnt++;
			}
			if(mang) break;
		}
		printf("Case #%d: ", t+1);
		if(mang) printf("IMPOSSIBLE\n");
		else printf("%d\n", cnt);
	}
	return 0;
}
//*/