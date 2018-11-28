#ifdef MG
//#define _GLIBCXX_DEBUG
#endif

#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cstring>
#include <cassert>
#include <ctime>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>

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

template<typename X> inline X abs(const X &a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X &a) { return a * a; }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const pair <X, Y>& p) { return out << '(' << p.x << ", " << p.y << ')'; }
template<typename X> inline ostream& operator<< (ostream& out, const vector<X>& p) { forn(i, sz(p)) { if (i != 0) out << ' '; out << p[i]; } return out; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = acosl(ld(-1));

const int N = 6 + 3;

int n, m;

inline bool read()
{
	return cin >> n >> m;
}

const int dx[] = { -1, 0, 1, 0 };
const int dy[] = { 0, -1, 0, 1 };

int a[N][N];

set<vector<int> > z;

inline bool can(int x, int y)
{
	if (a[x][y] == -1) return true;
	
	int cntSame = 0;
	int cntEmpty = 0;
	
	forn(k, 4)
	{
		int nx = x + dx[k], ny = y + dy[k];
		if (nx < 0 || nx >= n) continue;
		
		if (ny < 0) ny += m;
		if (ny >= m) ny -= m;
		
		if (a[nx][ny] == -1) cntEmpty++;
		if (a[nx][ny] == a[x][y]) cntSame++;
	}
	
	if (cntSame + cntEmpty < a[x][y]) return false;
   	if (cntSame > a[x][y]) return false;
   	return true;
}

void solve(int x, int y)
{
	if (x == n)
	{
		vector<int> cur(n * m, INF);
		forn(j, m)
		{
			vector<int> q;
			
			forn(k, m)
				forn(i, n)
					q.pb(a[i][(j + k) % m]);
					
			cur = min(cur, q);
		}
		
		z.insert(cur);
		return;
	}
	
	int tx = x, ty = y + 1;
	if (ty == m) tx++, ty = 0;
	
	forl(i, 4)
	{
		int cntSame = 0;
		int cntEmpty = 0;
		
		forn(k, 4)
		{
			int nx = x + dx[k], ny = y + dy[k];
			if (nx < 0 || nx >= n) continue;
			
			if (ny < 0) ny += m;
			if (ny >= m) ny -= m;
			
			if (a[nx][ny] == -1) cntEmpty++;
			if (a[nx][ny] == i) cntSame++;
		}
		
		if (cntSame + cntEmpty < i) continue;
		if (cntSame > i) continue;
		
		a[x][y] = i;

		bool ok = true;
		forn(k, 4)
		{
			int nx = x + dx[k], ny = y + dy[k];
			if (nx < 0 || nx >= n) continue;
			
			if (ny < 0) ny += m;
			if (ny >= m) ny -= m;
			
			if (!can(nx, ny))
			{
				ok = false;
				break;
			}
		}
		
		if (ok) solve(tx, ty);
		
		a[x][y] = -1;
	}
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	memset(a, -1, sizeof a);
	z.clear();
	solve(0, 0);
	
	cout << sz(z) << endl;
}

int main()
{
#ifdef MG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	
	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	int T;
	cin >> T;
	
	forn(t, T)
	{
		assert(read());
		solve(t);
	}
	
#ifdef MG
	cerr << "=== TIME: " << clock() << " ===" << endl;
#endif

	return 0;
}
