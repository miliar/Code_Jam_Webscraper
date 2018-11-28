/*
*	Copyright (C) Lyq root@lyq.me
*	File Name     : p4.cpp
*	Creation Time : 2014/04/12 16:55:27
*	Environment   : Ubuntu 12.04-64bit
*/
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <utility>
#include <queue>

using namespace std;

int f[5][5], g[5][5];
int r, c, m, X, Y;
bool flag;
queue< pair<int,int> > myque;
const int route[8][2] = {{0,1},{0,-1},{1,0},{-1,0},{1,1},{1,-1},{-1,-1},{-1,1}};

bool click(int x, int y)
{
	int xx, yy, k;

	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++) g[i][j] = f[i][j];
	}
	myque.push(make_pair(x,y));
	g[x][y] = 2;

	while (!myque.empty())
	{
		x = myque.front().first;
		y = myque.front().second;
		myque.pop();

		for (k = 0; k < 8; k++)
		{
			xx = x + route[k][0];
			yy = y + route[k][1];
			if (xx < 0 || xx >= r || yy < 0 || yy >= c) continue;
			if (f[xx][yy]) break;
		}
		
		if (k < 8) continue;
		for (k = 0; k < 8; k++)
		{
			xx = x + route[k][0];
			yy = y + route[k][1];
			if (xx < 0 || xx >= r || yy < 0 || yy >= c) continue;
			if (g[xx][yy] != 0) continue;

			g[xx][yy] = 2;
			myque.push(make_pair(xx,yy));
		}
	}
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++) if (g[i][j] == 0) return false;
	}
	return true;
}

void dfs(int x, int y, int m)
{
	if (m == 0)
	{
		for (x = 0; x < r; x++)
		{
			for (y = 0; y < c; y++)
			{
				if (f[x][y] == 0 && click(x, y))
				{
					flag = true;
					X = x; Y = y;
					return;
				}
			}
		}
		return;
	}
	
	int xx, yy, k;
	
	yy = y + 1; xx = x;
	if (yy == c)
	{
		yy = 0; xx++;
	}
	
	if (xx == r) return;

	dfs(xx,yy,m);
	if (flag) return;

	f[x][y] = 1;
	dfs(xx, yy, m-1);
	if (flag) return;
	f[x][y] = 0;	
}
int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);

	int test;
	cin>>test;

	for (int tt = 1; tt <= test; tt++)
	{
		printf("Case #%d:\n", tt);
		cin>>r>>c>>m;
		
		flag = false;
		memset(f, 0, sizeof(f));
		dfs(0, 0, m);
		
		if (flag)
		{
			f[X][Y] = 2;
			for (int x = 0; x < r; x++)
			{
				for (int y = 0; y < c; y++)
				{
					if (f[x][y] == 0) printf(".");
					if (f[x][y] == 1) printf("*");
					if (f[x][y] == 2) printf("c");
				}
				printf("\n");
			}
		}else printf("Impossible\n");

	}
	return 0;
}
