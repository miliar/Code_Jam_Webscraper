#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <list>
#include <set>
#include <queue>

using namespace std;

typedef long long int LL;
typedef pair<int,int> pii;

#define F first
#define S second
#define pb push_back
#define mp make_pair

#define N 101

int g[N][N], h[N][N], vis[N][N];
int n, m;

bool can_cut(int i, int j, int di, int dj, int hei)
{

	for( ;i < n && i >= 0 && j < m && j >= 0; i+=di, j+=dj)
		if(vis[i][j] && h[i][j] > hei) return false;
	return true;
}

int cut(int i, int j, int di, int dj, int hei)
{
	for( ;i < n && i >= 0 && j < m && j >= 0; i+=di, j+=dj)
		h[i][j] = hei;
}

bool solve()
{
	vector< pair<int, pii> > v;
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			v.push_back( mp(-g[i][j], mp(i, j) ) );

	sort(v.begin(), v.end());

	memset(vis, 0, sizeof vis);

	for(int x = 0; x < v.size(); ++x)
	{
		int i = v[x].S.F;
		int j = v[x].S.S; 
		int H = -v[x].F;
		int ok = 0;

		if( can_cut(i, 0, 0, 1, H) ) cut(i, 0, 0, 1, H), ok = 1;
		if( can_cut(0, j, 1, 0, H) ) cut(0, j, 1, 0, H), ok = 1;

		vis[i][j] = 1;
		if(!ok) return false;
		
	}

	return true;
}

int main (void)
{
	int T;
	cin >> T;

	for(int c = 1; c <= T; ++c)
	{
		cin >> n >> m;
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				cin >> g[i][j];

		bool ok = solve();
		printf("Case #%d: %s\n", c, ok ? "YES" : "NO");
	}

	return 0;
}
