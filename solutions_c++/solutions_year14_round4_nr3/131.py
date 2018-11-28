#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
using namespace std;

struct block_struct
{
	int x0, y0, x1, y1;
} block[1009];

const long long oo = 10000000000LL;

int w, h, b;
long long g[1009][1009];
long long ans;

long long calcDist(block_struct &a, block_struct &b)
{
	long long dx = 0, dy = 0;
	if (a.x1 < b.x0)
		dx = b.x0 - a.x1 - 1;
	if (b.x1 < a.x0)
		dx = a.x0 - b.x1 - 1;
	if (a.y1 < b.y0)
		dy = b.y0 - a.y1 - 1;
	if (b.y1 < a.y0)
		dy = a.y0 - b.y1 - 1;
	return max(dx, dy);
}

int init()
{
	cin >> w >> h >> b;
	for (int i = 1; i <= b; i++)
		cin >> block[i].x0 >> block[i].y0 >> block[i].x1 >> block[i].y1;
	return 0;
}

int work()
{
	block[0].x0 = -1;	block[0].y0 = 0;
	block[0].x1 = -1;	block[0].y1 = h - 1;
	block[b + 1].x0 = w;	block[b + 1].y0 = 0;
	block[b + 1].x1 = w;	block[b + 1].y1 = h - 1;
	for (int i = 0; i <= b + 1; i++)
	{
		g[i][i] = 0;
		for (int j = i + 1; j <= b + 1; j++)
			g[i][j] = g[j][i] = calcDist(block[i], block[j]);
	}
	
	bool used[1009];
	memset(used, 0, sizeof(used));
	long long dist[1009];
	for (int i = 0; i <= b + 1; i++)
	{
		dist[i] = oo;
	}
	dist[0] = 0;
	for (int i = 0; i <= b; i++)
	{
		long long best = oo;
		int k = -1;
		for (int j = 0; j <= b + 1; j++)
		if (!used[j] && dist[j] < best)
		{
			best = dist[j];
			k = j;
		}
		used[k] = true;
		for (int j = 0; j <= b + 1; j++)
			dist[j] = min(dist[j], dist[k] + g[k][j]);
	}
	ans = dist[b + 1];
	return 0;
}

int main()
{
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		init();
		work();
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}