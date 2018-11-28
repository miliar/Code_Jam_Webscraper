#include <ctime>
#include <iterator>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
using namespace std;


#define PB	push_back
#define MP  make_pair
#define ALL(a) 		(a).begin(), (a).end()
#define FILL(a,v) memset(a,v,sizeof(a))

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define SQR(x) (x)*(x)

const double PI = acos(-1.0);
const double EPS = 1e-7;

const int MOD = 1000000007;

typedef long long ll;

int r,c,m;
char cmap[10][10];
int a[10][10];
void generate(int mask)
{
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			cmap[i][j] = '*';
	for (int j = 0; j < c; ++j)
	{
		int k = mask%(r+1)-1;
		for (int i = 0; i <= k; ++i)
			cmap[i][j]='_';
		mask/=(r+1);
	}
}

int fcnt(int y, int x)
{
	int res = 0;
	if (y > 0)
	{
		if (x > 0)
		{
			if (cmap[y-1][x-1]=='*')
				++res;
		}
		if (cmap[y-1][x]=='*')
			++res;
		if (x < c-1)
		{
			if (cmap[y-1][x+1]=='*')
				++res;
		}
	}
	if (y < r-1)
	{
		if (x > 0)
		{
			if (cmap[y+1][x-1]=='*')
				++res;
		}
		if (cmap[y+1][x]=='*')
			++res;
		if (x < c-1)
		{
			if (cmap[y+1][x+1]=='*')
				++res;
		}
	}
	
	{
		if (x > 0)
		{
			if (cmap[y][x-1]=='*')
				++res;
		}
		if (cmap[y][x]=='*')
			++res;
		if (x < c-1)
		{
			if (cmap[y][x+1]=='*')
				++res;
		}
	}
	return res;
}

void bfs(int y, int x)
{
	if (y < 0 || y >= r || x < 0 || x >= c)
		return;
	if (cmap[y][x] != '_')
		return;

	cmap[y][x] = '.';

	 if (a[y][x] != 0)
		return;

	bfs(y-1,x-1);
	bfs(y-1,x);
	bfs(y-1,x+1);
	bfs(y,x-1);
	bfs(y,x+1);
	bfs(y+1,x-1);
	bfs(y+1,x);
	bfs(y+1,x+1);
}

bool can(int mask)
{
	generate(mask);
	int cnt = r*c;
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			if (cmap[i][j]=='_')
				--cnt;
	if (cnt != m)
		return false;



	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
			a[i][j] = fcnt(i,j);
	}
	if (a[0][0] != 0)
	{
		if (m == r*c-1)
		{
			cmap[0][0]='c';
			return true;
		}
		return false;
	}
	bfs(0,0);
	cmap[0][0] = 'c';

	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			if (cmap[i][j]=='_')
				return false;

	return true;
}

void solve()
{
	FILL(cmap,0);
	cin >> r >> c >> m;
	int mx=1;
	for (int i = 0; i < c; ++i)
		mx *= (r+1);
	for (int t = 0; t < mx; ++t)
	{
		if (can(t))
		{
			for (int i = 0; i < r; ++i)
			{
				for (int j = 0; j < c; ++j)
				{
					cout << cmap[i][j];
				}
				cout << endl;
			}
			return;
		}
	}
	cout << "Impossible\n";
}


int main()
{
	ios_base::sync_with_stdio(false);
	freopen( "input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		cout << "Case #" << test << ": ";
		cout << endl;
		solve();
		//cout << endl;
	}

	return 0;
} 
