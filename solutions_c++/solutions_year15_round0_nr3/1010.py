#ifdef MG
#define _GLIBCXX_DEBUG
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

const int N = 10 * 1000 + 13;

int n;
li k;
int a[N];

inline bool read()
{
	if (scanf("%d%lld", &n, &k) != 2) return false;
	
	char s[N];
	assert(scanf("%s", s) == 1);
	
	forn(i, n)
		a[i] = int(s[i] - 'i') + 2;
	
	return true;
}

map<pt, int> mult;

inline void prepare()
{
	mult[mp(1, 1)] = 1;
	mult[mp(1, 2)] = 2;
	mult[mp(1, 3)] = 3;
	mult[mp(1, 4)] = 4;

	mult[mp(2, 1)] = 2;
	mult[mp(2, 2)] = -1;
	mult[mp(2, 3)] = 4;
	mult[mp(2, 4)] = -3;

	mult[mp(3, 1)] = 3;
	mult[mp(3, 2)] = -4;
	mult[mp(3, 3)] = -1;
	mult[mp(3, 4)] = 2;

	mult[mp(4, 1)] = 4;
	mult[mp(4, 2)] = 3;
	mult[mp(4, 3)] = -2;
	mult[mp(4, 4)] = -1;	
}

inline int mul(int a, int b)
{
	if (a < 0) return -mul(-a, b);
	if (b < 0) return -mul(a, -b);
	return mult[mp(a, b)];
}

inline int binpow(int a, li b)
{
	int ans = 1;
	while (b)
	{
		if (b & 1)
			ans = mul(ans, a);
		
		a = mul(a, a);
		b >>= 1;
	}
	
	return ans;
}

inline bool go(li &pos, li sz, int value)
{
	set<pt> used;
	
	int cur = 1;
	used.insert(mp(cur, pos % n));
	
	while (pos < sz)
	{
		cur = mul(cur, a[pos % n]);
		
		pos++;
		int curpos = int(pos % n);
		
		if (cur == value)
			return true;
			
		if (used.count(mp(cur, curpos)))
			return false;
		
		used.insert(mp(cur, curpos));
	}
	
	return false;
}

inline void no()
{
	puts("NO");
}

inline int calc()
{
	int cur = 1;
	forn(i, n)
		cur = mul(cur, a[i]);
	return cur;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	li pos = 0;
	if (!go(pos, n * k, 2))
	{
		no();
		return;
	}
	
	if (!go(pos, n * k, 3))
	{
		no();
		return;
	}
	
	int cur = 1;
	while (pos % n != 0)
	{
		cur = mul(cur, a[pos % n]);
		pos++;
	}
	
	assert(pos <= n * k);
	
	li cnt = k - pos / n;
	cur = mul(cur, binpow(calc(), cnt));

	puts(cur == 4 ? "YES" : "NO");
}

int main()
{
#ifdef MG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	
	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	prepare();
	
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
