#pragma warning(disable: 4996)
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>
#include <exception>
#include <functional>

using namespace std;

#define mp make_pair
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define fori(i,n) for (int i = 0; i < (n); ++ i)
#define forv(i,v) for (int i = 0; i < (sz(v)); ++ i)
#define fi(n) for (int i = 0; i < n; ++ i)
#define fj(n) for (int j = 0; j < n; ++ j)
typedef unsigned long long ull;
typedef long long lint;
typedef pair < int, int > pii;
typedef double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef WIN32
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if (s == "input_txt")
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	else if (sz(s) != 0)
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

int n, m, x;

void read()
{
	cin >> n >> m >> x;
}

const int MAXN = 6;
char a[MAXN][MAXN];
char b[MAXN][MAXN];

int dx[] = { 1, 1, 1, 0, -1, -1, -1, 0 };
int dy[] = { -1, 0, 1, -1, -1, 0, 1, 1};


string Impossible = "Impossible";

bool print(int cnt)
{
	for (int i = n - 1; i >= 0; --i)
	{
		for (int j = m - 1; j >= 0; --j)
		{
			if (a[i][j] != 0)
				continue;
			if (cnt)
			{
				--cnt;
				a[i][j] = '*';
			}
			else
			{
				a[i][j] = '.';
			}
		}
	}
	a[0][0] = 'c';

	fi(n)
	{
		cout << endl;
		fj(m)
		{
			cout << a[i][j];
		}
	}
	return false;
}

bool In(int x, int y)
{
	return x >= 0 && x < n && y >= 0 && y < m;
}



bool check()
{
	fi(n)
	{
		fj(m)
		{
			if (a[i][j] == '*')
				continue;
			_(b, 0);
			queue<pii> q;
			q.push(pii(i, j));
			b[i][j] = true;
			while (!q.empty())
			{
				int i = q.front().first;
				int j = q.front().second;
				q.pop();
				int cnt = 0;
				for (int k = 0; k < 8; ++k)
				{
					int x = i + dx[k];
					int y = j + dy[k];
					if (In(x, y) && a[x][y] == '*')
						++cnt;
				}
				if (cnt == 0)
				{

					for (int k = 0; k < 8; ++k)
					{
						int x = i + dx[k];
						int y = j + dy[k];
						if (In(x, y))
						{
							if (b[x][y] == false)
							{
								b[x][y] = true;
								q.push(pii(x, y));
							}
						}
					}
				}
			}
			bool T_T = false;
			for (int x = 0; x < n; ++x)
			{
				for (int y = 0; y < m; ++y)
				{
					if (b[x][y] == false && a[x][y] == '.')
						T_T = true;
				}
			}
			if (!T_T)
				return true;
		}
	}
	return false;
}

bool f(int i, int j, int x)
{
	if (x < 0)
		return false;
	if (i == n)
	{
		if (x == 0 && check())
		{
			print(0);
			return true;
		}
		return false;
	}
	if (j == m)
	{
		return f(i + 1, 0, x);
	}
	if ((n - i - 1) * m + (m - j) < x)
		return false;

	a[i][j] = '.';
	if (f(i, j + 1, x))
		return true;
	a[i][j] = '*';
	if (f(i, j + 1, x - 1))
		return true;
	return false;
}

bool solve()
{
	_(a, 0);
	
	if (!f(0, 0, x))
		cout << endl << Impossible;

	return false;
}

int main()
{
	prepare("");
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cout << "Case #" << (i + 1) << ": ";
		cerr << "Case #" << (i + 1) << endl;
		read();
		solve();
		cout << endl;
	}

	return 0;
}
