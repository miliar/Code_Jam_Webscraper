#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <iomanip>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;
const ld PI = acosl(ld(-1));

const int N = 16 + 3;
int n, m;
int p[2 * N];

inline bool read()
{
	if (scanf ("%d%d", &n, &m) != 2)
		return false;
		
	forn (i, 2 * (n + m))
	{
		assert(scanf ("%d", &p[i]) == 1);
		
		p[i]--;
	}

	return true;
}

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

inline bool valid (int x, int y)
{
	return x >= 0 && y >= 0 && x < n && y < m;
}

int a[N][N];
int dsu[10000];

int getParent (int v)
{
	if (dsu[v] == v)
		return v;
		
	return dsu[v] = getParent(dsu[v]);
}

inline void unite (int a, int b)
{
	a = getParent(a), b = getParent(b);
	
	if (rand() & 1)
		swap(a, b);
		
	dsu[a] = b;
}

inline int getId (int x, int y, int dir)
{
	if (!valid (x, y))
	{
		if (x == -1)
			return 2 * n * m + y;
		if (y == m)
			return 2 * n * m + m + x;
		if (x == n)
			return 2 * n * m + n + m + (m - 1 - y);
			
		return 2 * n * m + n + m + m + (n - 1 - x);
	}
	
	if (a[x][y])
	{
		if (dir < 2)
			return x * m + y;
		return n * m + x * m + y;
	}

	if (dir == 0 || dir == 3)
		return x * m + y;
	return n * m + x * m + y;
}

inline bool check ()
{
	forn (i, 2 * n * m + 2 * (n + m))
		dsu[i] = i;
		
	forn (i, n)
		forn (j, m)
		{
			if (a[i][j])
			{
				{
					int id = i * m + j;
					fore (it, 0, 1)
					{
						int nx = i + dx[it], ny = j + dy[it];
						int nid = getId(nx, ny, ((it + 2) & 3));
						
						unite(id, nid);
					}
				}
				
				{
					int id = n * m + i * m + j;
					fore (it, 2, 3)
					{
						int nx = i + dx[it], ny = j + dy[it];
						int nid = getId(nx, ny, ((it + 2) & 3));
						
						unite(id, nid);
					}				
				}
			}
			else
			{
				{
					int id = i * m + j;
					forn (it, 4)
					{
						if (it == 1 || it == 2)
							continue;
						
						int nx = i + dx[it], ny = j + dy[it];
						int nid = getId(nx, ny, ((it + 2) & 3));
						
						unite(id, nid);
					}
				}
				
				{
					int id = n * m + i * m + j;
					fore (it, 1, 2)
					{
						int nx = i + dx[it], ny = j + dy[it];
						int nid = getId(nx, ny, ((it + 2) & 3));
						
						unite(id, nid);
					}				
				}			
			}
		}
		
	//forn (i, 2 * n * m + 2 * (n + m))
//		cerr << dsu[i] << ' ';
//	cerr << endl;
		
	set<int> q;
		
	for (int i = 0; i < 2 * (n + m); i += 2)
	{
		//cerr << 2 * n * m + p[i] << ' ' << 2 * n * m + p[i + 1] << endl;
	
		if (getParent(2 * n * m + p[i]) != getParent(2 * n * m + p[i + 1]))
			return false;

		q.insert(getParent(2 * n * m + p[i]));
	}
	
	return sz(q) == n + m;
}

inline void solve(int test)
{
	printf ("Case #%d:\n", test + 1);
	
	forn (mask, (1 << (n * m)))
	{
		forn (i, n)
			forn (j, m)
				a[i][j] = ((mask >> (i * m + j)) & 1);
				
		if (check())
		{
			forn (i, n)
			{
				forn (j, m)
					if (a[i][j])
						putchar('\\');
					else
						putchar('/');
				puts("");
			}
			
			return;
		}
	}
	
	puts("IMPOSSIBLE");
}

int main()
{
#ifdef SU2_PROJ
	assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	cout << setprecision(25) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));
	
	int testCnt;
	assert(scanf ("%d", &testCnt) == 1);

	forn (test, testCnt)
	{
		assert(read());
		solve(test);
	}

#ifdef SU2_PROJ
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}
