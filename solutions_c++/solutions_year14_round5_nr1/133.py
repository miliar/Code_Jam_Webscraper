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

int n, p, q, r, s;

inline bool read()
{
	if (scanf("%d%d%d%d%d", &n, &p, &q, &r, &s) != 5) return false;
	return true;
}

const int N = 1000 * 1000 + 13;

int a[N];
li suf[N];

inline void solve(int test)
{
	printf("Case #%d: ", test);
	
	forn(i, n) a[i] = int(((i * 1LL * p) + q) % r + s);
	
	suf[n] = 0;
	ford(i, n) suf[i] = suf[i + 1] + a[i];
	
	li ans = INF64;
	
	li v1 = 0, v2 = 0;
	
	int lf = 0;
	
	forn(rg, n)
	{
		v2 += a[rg];
		
		while (lf < rg)
		{
			li nv1 = v1 + a[lf], nv2 = v2 - a[lf];
			if (nv1 > nv2) break;
			v1 = nv1, v2 = nv2, lf++;
		}
		
		li curval = 0;
		curval = max(curval, suf[rg + 1]);
		curval = max(curval, v1);
		curval = max(curval, v2);
		
		ans = min(ans, curval);
		
		if (lf < rg)
		{
			li nv1 = v1 + a[lf], nv2 = v2 - a[lf];
			curval = 0;
			curval = max(curval, suf[rg + 1]);
			curval = max(curval, max(nv1, nv2));
			ans = min(ans, curval);
		}
	}
	
	li den = 0;
	forn(i, n) den += a[i];
	
	cout << ld(den - ans) / ld(den) << endl;
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
		cerr << "test = " << test << ", clock = " << clock() << endl;
#endif
	}
	
	return 0;
}
