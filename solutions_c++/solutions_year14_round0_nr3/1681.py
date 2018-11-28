#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <map>
using namespace std;

bool G[5][5];
bool visited[5][5];
int R, C;
int X, Y;

map < int, string > cache;

void dfs(int x, int y)
{
	if (visited[x][y])	return;
	visited[x][y] = true;
	for (int i = x-1; i <= x+1; i++)
		for (int j = y - 1; j <= y + 1; j++)
			if ( i >= 0 && i < R && j >= 0 && j < C && (i != x || j != y ) && !G[i][j])
				return;
	for (int i = x-1; i <= x+1; i++)
		for (int j = y - 1; j <= y + 1; j++)
			if ( i >= 0 && i < R && j >= 0 && j < C && (i != x || j != y ))
				dfs(i,j);
}

bool go(int x, int y, int rem)
{
	if (x >= R || y >= C)	return false;
	if (rem == 0)
	{
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				if (G[i][j])
				{
					memset(visited,false,sizeof(visited));
					dfs(i,j);
					for (int a = 0; a < R; a++)
						for (int b = 0; b < C; b++)
							if (G[a][b] && !visited[a][b])	goto nxt;
					X = i, Y = j;
					return true;
					nxt:;
				}
		return false;
	}
	if (x + 1 < R)
	{
		if (go(x+1,y,rem))	return true;
	}
	else if (y+1 < C)
	{
		if (go(0,y+1,rem))	return true;
	}
	G[x][y] = false;
	if (x + 1 < R)
	{
		if (go(x+1,y,rem-1))	return true;
	}
	else if (y+1 < C)
	{
		if (go(0,y+1,rem-1))	return true;
	}
	G[x][y] = true;
	return false;
}

int main(void)
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++)
	{
		int M;
		cin >> R >> C >> M;
		memset(G,true,sizeof(G));
		cout << "Case #" << c << ": \n";
		string ans;
		if (cache.count(25*M+5*(R-1)+(C-1)) > 0)
			ans = cache[25*M+5*(R-1)+(C-1)]; // it should work in time without this...
		else
		{
			if (go(0,0,M))
			{
				for (int i = 0; i < R; i++)
				{
					for (int j = 0; j < C; j++)
					{
						if (!G[i][j])
							ans += "*";
						else if (X == i && Y == j)
							ans += "c";
						else
							ans += ".";
					}
					ans += "\n";
				}
			}
			else
				ans = "Impossible\n";
		}
		cache[25*M+5*(R-1)+(C-1)] = ans;
		cout << ans;
	}
	return 0;
}
