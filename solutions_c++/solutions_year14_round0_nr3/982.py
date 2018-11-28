#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cstdio>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <time.h>
using namespace std;

bool mp[10][10];
int dx[] = {-1,-1,-1,0,0,1,1,1};
int dy[] = {-1,0,1,-1,1,-1,0,1};
bool vis[10][10];
int r, c, si, sj, n;

bool can (int x, int y)
{
	for (int i=0;i<8;i++)
	{
		int ni = x + dx[i];
		int nj = y + dy[i];
		if (ni < 0 || nj < 0 || ni == r || nj == c)
			continue;
		if (mp[ni][nj])
			return false;
	}
	return true;
}

void dfs (int x, int y)
{
	//cout << x << " " << y << endl;
	
	vis[x][y] = true;

	if (!can(x, y))
		return;

	for (int i=0;i<8;i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || ny < 0 || nx >= r || ny >= c)
			continue;
		if (vis[nx][ny])
			continue;
		dfs(nx, ny);
	}

}

bool check ()
{
	memset (vis, 0, sizeof(vis));
	for (int i=0;i<r;i++)
		for (int j=0;j<c;j++)
		{
			if (can(i, j) && !mp[i][j])
			{
				si = i, sj = j;
				dfs (i, j);
				goto a;
			}
		}
	a:
	for (int i=0;i<r;i++)
		for (int j=0;j<c;j++)
			if (!mp[i][j] && !vis[i][j])
				return false;
	return true;
}

bool sol (int x, int y, int m)
{
	if (m == 0)
		return check();
	if (y == c)
		return sol (x+1, 0, m);
	if (x == r)
		return false;
	mp[x][y] = true;
	if (sol (x, y+1, m-1))
		return true;
	mp[x][y] = false;
	return sol (x, y+1, m);
}

int main ()
{
	int t;

	freopen ("C-small.in", "r", stdin);
	freopen ("C-small.out", "w", stdout);

	scanf ("%d", &t);

	for (int cc=1;cc<=t;cc++)
	{
		printf ("Case #%d:\n", cc);


		cin >> r >> c >> n;
		//cout<< r << " " << c << " " << n << endl;
		
		memset (mp, 0, sizeof(mp));
		
		int x = r*c - n;
		
		if (x == 1)
		{
			for (int i=0;i<r;i++)
			{
				for (int j=0;j<c;j++)
				{
					if (i==r-1 && j == c-1)
						cout <<"c";
					else
						cout <<"*";
				}
				cout << endl;
			}
			continue;
		}
		
		if (!sol(0, 0, n))
			cout << "Impossible\n";
		else
			for (int i=0;i<r;i++)
			{
				for (int j=0;j<c;j++)
				{
					if (i == si && j == sj)
						cout << "c";
					else
					{
						if (mp[i][j])
							cout << "*";
						else
							cout << ".";
					}
				}
				cout << endl;
			}

	}
	return 0;
}
