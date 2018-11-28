#undef NDEBUG
#ifdef SU2_PROJ
#define _GLIBCXX_DEBUG
#endif

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define ft first
#define sc second
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }
inline ostream& operator<< (ostream& out, const pt& p) { return out << '(' << p.x << ", " << p.y << ')'; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int N = 1000 + 13;

int W, H, n;
int d[N][N];
pt p[N][4];

inline bool read()
{
	if (scanf("%d%d%d", &W, &H, &n) != 3) return false;
	
	forn(i, n)
	{
		int ax, ay, bx, by;
		assert(scanf("%d%d%d%d", &ax, &ay, &bx, &by) == 4);
		p[i][0] = mp(ax, ay);
		p[i][1] = mp(bx, ay);
		p[i][2] = mp(bx, by);
		p[i][3] = mp(ax, by);
	}
	
	p[n][0] = mp(-1, 0);
	p[n][1] = mp(-1, H);
	p[n][2] = mp(-1, H);
	p[n][3] = mp(-1, 0);
	n++;
	
	p[n][0] = mp(W, 0);
	p[n][1] = mp(W, H);
	p[n][2] = mp(W, H);
	p[n][3] = mp(W, 0);
	n++;
	
	return true;
}

int z[N];
int inq[N];

/*inline int dist (const pt& a, const pt& b)
{
	return max(0, min(abs(a.x - b.x), abs(a.y - b.y)) - 1);
}*/

inline int dist (const pt& a, const pt& b)
{
	return max(abs(a.x - b.x), abs(a.y - b.y)) - 1;
}

inline int dist (const pt& c, const pt& a, const pt& b)
{
	if (a.x == b.x)
	{
		if (min(a.y, b.y) <= c.y && c.y <= max(a.y, b.y))
			return abs(a.x - c.x) - 1;
		return min(dist(a, c), dist(b, c));
	}
	
	if (a.y == b.y)
	{
		if (min(a.x, b.x) <= c.x && c.x <= max(a.x, b.x))
			return abs(a.y - c.y) - 1;
		return min(dist(a, c), dist(b, c));
	}
	
	throw;
}

inline int dist (int i1, int i2)
{
	if (i1 == i2) return 0;
	int res = INF;
	//forn(i, 4) forn(j, 4) res = min(res, dist(p[i1][i], p[i2][j]));
	forn(i, 4) forn(j, 4)
	{
		res = min(res, dist(p[i1][i], p[i2][j], p[i2][(j + 1) & 3]));
		res = min(res, dist(p[i2][i], p[i1][j], p[i1][(j + 1) & 3]));
	}
	return res;
}

inline void solve(int test)
{
	printf("Case #%d: ", test);
	
	forn(i, n) forn(j, n) d[i][j] = dist(i, j);
	
	//forn(i, n) { forn(j, n) cerr << d[i][j] << ' '; cerr << endl; }
	
	forn(i, n) z[i] = INF;
	z[n - 2] = 0;
	
	queue <int> q;
	q.push(n - 2);
	inq[n - 2] = true;
	
	while (!q.empty())
	{
		int v = q.front();
		q.pop();
		inq[v] = false;
		
		forn(i, n)
			if (z[i] > z[v] + d[v][i])
			{
				z[i] = z[v] + d[v][i];
				if (!inq[i])
				{
					inq[i] = true;
					q.push(i);
				}
			}
	}
	
	printf("%d\n", z[n - 1]);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	int testCount;
	cin >> testCount;
	
	forl(test, testCount)
	{
		assert(read());
		solve(test);
#ifdef SU2_PROJ
		cerr << test << ' ' << clock() << endl;
#endif
	}
	
	return 0;
}
