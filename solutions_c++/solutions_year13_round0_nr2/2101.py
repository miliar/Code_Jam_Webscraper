//Seikang

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <stdlib.h>
#include <assert.h>

#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>

#include <cmath>
#include <complex>
#include <algorithm>

#include <ctime>
#define gtime clock()

using namespace std;

#define SZ(cont) (int)(cont.size())
#define ALL(cont) (cont).begin(), (cont).end()
#define DEBUG(x) cerr << ">" << #x << ":" << x << endl

typedef long long int64;
typedef pair<int64, int64> ii;
typedef vector<int64> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<string> vs;

const int64 oo32 = 1ll << 30, oo64 = 1ll << 60;
const double pi = acos(-1.0), eps = 1e-9;
inline bool equal(const double &a, const double &b){return abs(a - b) < eps;}

int grid[100][100];
int mark[100][100];
int n, m;
bool read()
{
	memset(grid, 0, sizeof grid);
	memset(mark, 0, sizeof mark);
	cin >> n >> m;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < m; j++)
		{
			cin >> grid[i][j];
			mark[i][j] = oo32;
		}
	}
}
bool solve()
{
	for(int i = 0; i < n; i++)
	{
		int maxRow = 0;
		for(int j = 0; j < m; j++)
			maxRow = max(maxRow, grid[i][j]);
		for(int j = 0; j < m; j++)
			mark[i][j] = min(mark[i][j], maxRow);
	}
	for(int j = 0; j < m; j++)
	{
		int maxCol = 0;
		for(int i = 0; i < n; i++)
			maxCol = max(maxCol, grid[i][j]);
		for(int i = 0; i < n; i++)
			mark[i][j] = min(mark[i][j], maxCol);
	}

	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			if (grid[i][j] != mark[i][j])
				return false;
	return true;
}
int main()
{
//	freopen ("in.txt", "rt", stdin);
//	freopen ("out.txt", "wt", stdout);
	int T;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		read();
		cout << "Case #" << t + 1 << ": " << (solve() ? "YES" : "NO") << endl;
	}
	return 0;
}
