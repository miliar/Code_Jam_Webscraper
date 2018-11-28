#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cstring>
#include <ctime>
#include <cmath>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>
#include <numeric>
#include <functional>

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

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int N = 10 * 1000 + 13;

int E, R, n;
int a[N];
int next[N];
vector <pt> v;
int mind[N];

inline bool read()
{
	if (scanf("%d%d%d", &E, &R, &n) != 3)
		return false;
		
	forn(i, n) assert(scanf("%d", &a[i]) == 1);		
	
	return true;
}

inline void solve(int test)
{
	v.clear();
	v.pb(mp(INF, INF));
	ford(i, n)
	{
		while (a[i] > v.back().ft) v.pop_back();
		next[i] = v.back().sc;
		mind[i] = max(0LL, E - (next[i] - i) * 1LL * R);
		v.pb(mp(a[i], i));
	}
	
	li ans = 0;
	int rem = E;
	
	forn(i, n)
	{
		int cur = max(0, rem - mind[i]);
		ans += cur * 1LL * a[i];
		rem -= cur;
		rem = min(E, rem + R);
	}
	
	printf("Case #%d: %I64d\n", test + 1, ans);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	int testCount;
	cin >> testCount;
	
	forn(test, testCount)
	{
		assert(read());
		solve(test);
		cerr << test + 1 << ' ' << clock() << endl;
	}
	
	return 0;
}
