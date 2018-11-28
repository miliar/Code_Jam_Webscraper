#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
 
using namespace std;
 
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define forn1(i, n) for(int i = 1; i <= (int)(n); i++)
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)((a).size())
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define x first
#define y second
#define y1 __y1
#define sqr(x) ((x) * (x))
 
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
 
const int INF = (int)(1e9);
const li INF64 = (li)(INF) * (li)(INF);
const ld eps = 1e-9;
const ld pi = ld(3.1415926535897932384626433832795);
 
bool in(int i, int j, int n, int m)
{
    return i >= 0 && i < n && j >= 0 && j < m;
}
 
inline int myrand()
{
    return (rand() ^ (rand() << 15));
}
 
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};
 
const int N = 11111;
const int N2 = 11111;

int n, m, c;
 
inline bool read()
{
	if(!(cin >> n >> m >> c))
		return false;
    return true;
}

inline void gen()
{
	n = myrand() % 10000;
	m = 10000 / n;
	c = myrand() % (n * m);
	cerr << "test == " << n << ' ' << m << ' ' << c << endl;
	return;
}

int a[N][N];

inline int solve1()
{
	forn(i, n + 3)
	{
		forn(j, m + 3)
		{
			a[i][j] = 0;
		}
	}

	for(int i = 1; i <= n; i++)
	{
		if((i & 1) == 1)
		{
			for(int j = 1; j <= m; j += 2)
			{
				a[i][j] = 1;
			}
		}
		else
		{
			for(int j = 2; j <= m; j += 2)
			{
				a[i][j] = 1;
			}
		}
	}

	int all = 0;
	forn1(i, n)
	{
		forn1(j, m)
		{
			all += a[i][j];
		}
	}

	while(all < c)
	{
		int mini = -1, minj = -1, mn = INF;
		forn1(i, n)
		{
			forn1(j, m)
			{
				if(a[i][j] == 1)
					continue;
				int cur = 0;
				forn(dir, 4)
				{
					int ni = i + dx[dir];
					int nj = j + dy[dir];
					cur += a[ni][nj];
				}

				if(cur < mn)
				{
					mn = cur;
					mini = i, minj = j;
				}
			}
		}

		all++;
		a[mini][minj] = 1;
	}

	int res = 0;
	forn1(i, n)
	{
		forn1(j, m)
		{
			if(a[i][j] == 1 && a[i + 1][j] == 1)
				res++;
			if(a[i][j] == 1 && a[i][j + 1] == 1)
				res++;
		}
	}

	/*cerr << "table solve1 == " << endl;
	forn1(i, n)
	{
		forn1(j, m)
		{
			cerr << a[i][j] << ' ';
		}

		cerr << endl;
	}*/

	return res;
}

inline int solve2()
{
	forn(i, n + 3)
	{
		forn(j, m + 3)
		{
			a[i][j] = 0;
		}
	}

	for(int i = 1; i <= n; i++)
	{
		if((i & 1) == 0)
		{
			for(int j = 1; j <= m; j += 2)
			{
				a[i][j] = 1;
			}
		}
		else
		{
			for(int j = 2; j <= m; j += 2)
			{
				a[i][j] = 1;
			}
		}
	}

	int all = 0;
	forn1(i, n)
	{
		forn1(j, m)
		{
			all += a[i][j];
		}
	}

	while(all < c)
	{
		int mini = -1, minj = -1, mn = INF;
		forn1(i, n)
		{
			forn1(j, m)
			{
				if(a[i][j] == 1)
					continue;
				int cur = 0;
				forn(dir, 4)
				{
					int ni = i + dx[dir];
					int nj = j + dy[dir];
					cur += a[ni][nj];
				}

				if(cur < mn)
				{
					mn = cur;
					mini = i, minj = j;
				}
			}
		}

		all++;
		a[mini][minj] = 1;
	}

	int res = 0;
	forn1(i, n)
	{
		forn1(j, m)
		{
			if(a[i][j] == 1 && a[i + 1][j] == 1)
				res++;
			if(a[i][j] == 1 && a[i][j + 1] == 1)
				res++;
		}
	}

	return res;
}

inline void solve()
{
	int ans = min(solve1(), solve2());
	//cerr << "solvs == " << solve1() << ' ' << solve2() << endl;
	//cerr << ans << ' ' << ans2 << endl;
	//assert(ans2 == ans);
	cout << ans << endl;
	return;
}

inline void clear()
{
	return;
}
 
int main(){
#ifdef _DEBUG
    assert(freopen("input.txt", "rt", stdin));
    assert(freopen("output.txt", "wt", stdout));
#endif
 
    cout << setprecision(10) << fixed;
    cerr << setprecision(10) << fixed;
 
    srand(int(time(NULL)));

	int T;
	assert(cin >> T);
 
	forn(test, T)
	{
		cerr << "RUNNING on test == " << test + 1 << endl;
		int startT = clock();
		assert(read());
		//gen();
		//gen();
		cout << "Case #" << test + 1 << ": ";
		solve();
		clear();
		int endT = clock();
		int Time = endT - startT;
		cerr << "Test " << test + 1 << " passed with TIME == " << Time << " ms" << endl;
		cerr << "Summary TIME == " << clock() << endl << endl << endl;
	}
 
    cerr << "TIME == " << clock() << " ms" << endl;
    return 0;
}