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

const int N = 8;
const int M = 10000 + 3;
const int ALPH = 26 + 3;

int n, m;
string s[N];

inline bool read()
{
	if (scanf("%d%d", &n, &m) != 2) return false;
	
	forn(i, n) cin >> s[i];
	
	return true;
}

pt d[(1 << N) + 3][5];
int z[(1 << N) + 3];
int t[M][ALPH], szt;

void add (const string& s)
{
	int v = 0;
	
	forn(i, sz(s))
	{
		int c = s[i] - 'A';
		if (t[v][c] == -1)
		{
			memset(t[szt], -1, sizeof(t[szt]));
			t[v][c] = szt++;
		}
		v = t[v][c];
	}
}

int calc (int mask)
{
	int& ans = z[mask];
	if (ans != -1) return ans;
	
	ans = 0;
	szt = 1;
	memset(t[0], -1, sizeof(t[0]));
	
	forn(i, n) if (mask & (1 << i)) add(s[i]);
	
	return ans = szt;
}

pt solve (int mask, int rem)
{
	pt& ans = d[mask][rem];
	if (ans != mp(-1, -1)) return ans;
	
	if (rem == 0) return mask == 0 ? mp(0, 1) : mp(-INF, 0);
	
	ans = mp(0, 1);
	
	for (int submask = mask; submask != 0; submask = ((submask - 1) & mask))
	{
		int cnt = calc(submask);
		pt t = solve(mask ^ submask, rem - 1);
		t.ft += cnt;
		
		if (ans.ft < t.ft) ans = mp(t.ft, 0);
		if (ans.ft == t.ft) ans.sc += t.sc;
	}
	
	return ans;
}

inline void solve(int test)
{
	printf("Case #%d: ", test);
	
	forn(i, (1 << n)) z[i] = -1;
	forn(i, (1 << n)) forn(j, m + 1) d[i][j] = mp(-1, -1);
	
	pt ans = solve((1 << n) - 1, m);
	
	printf("%d %d\n", ans.ft, ans.sc);
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
