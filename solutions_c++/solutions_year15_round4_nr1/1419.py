#include <iostream>  
#include <cstdio>  
#include <cstring>  
#include <vector>  
#include <queue>  
#include <cmath>  
#include <algorithm>  
#include <map>  
#include <ctime> 
#include <functional>

using namespace std;
#pragma warning(disable:4996)
#define ll long long 
#define rep(i,n) for(int i=0; i<n; i++)
#define FOR(i,n) for(int i=1; i<=n; i++)
#define oo 1000000007
#define N 10010

#define low(t) (t & ( t ^ ( t - 1 ) ))

int max(int a, int b) { return a>b ? a : b; }
int min(int a, int b) { return a<b ? a : b; }

int r, c;
char a[101][101];
int d[4][2];

int find(int x, int y, char w)
{
	if (w == '.') return 0;
	int dx, dy;
	if (w == '<') dx = 0, dy = -1; else
		if (w == '>') dx = 0, dy = 1; else
			if (w == '^') dx = -1, dy = 0; else
				if (w == 'v') dx = 1, dy = 0;

	int px = x, py = y;
	bool pp = false;
	rep(i, 4) {
		x = px, y = py;
		while (1) {
			x += d[i][0];
			y += d[i][1];
			if (x < 0 || x >= r || y < 0 || y >= c) break;
			if (a[x][y] != '.') {
				pp = true;
				if (dx == d[i][0] && dy == d[i][1]) return 0;
			}
		}
	}
	if (!pp) return -1; else return 1;
}

void work()
{
	int ans = 0;
	rep(i, r)
		rep(j, c) 
	{
		int w = find(i, j, a[i][j]);
		if (w == -1) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		ans += w;
	}
	cout << ans << endl;
}
int main()
{
	d[0][0] = 1;
	d[1][0] = -1;
	d[2][1] = 1;
	d[3][1] = -1;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T = 0;
	scanf("%d", &T);
	rep(t, T)
	{
		cin >> r >> c;
		rep(i, r) cin >> a[i];
		printf("Case #%d: ", t+1);
		work();
	}
}