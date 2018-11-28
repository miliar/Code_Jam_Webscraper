#pragma comment(linker, "/stack:128000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define x first
#define y second
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 20 + 1;
const int L = 1000 * 1000 + 3;

int n;
//vector<string> s[N];
vector<li> h[N];
char buf[L];

const int CNT = N * 1000;
li hs[CNT];
int sz;

inline li hash(const string& s);

inline bool read()
{
	if (scanf("%d", &n) != 1)
		return false;

	assert(gets(buf));

	sz = 0;

	forn(i, n)
	{
		assert(gets(buf));
		string str = string(buf);

		//s[i].clear();
		h[i].clear();

		stringstream ss;
		ss << str;
		string cur;
		while(ss >> cur)
		{
			li hh = hash(cur);
			h[i].pb(hh);
			//s[i].pb(cur);
			hs[sz++] = hh;
			assert(sz < CNT);
		}
	}
	
    return true;
}

const li P = 1009;
const li MOD = 1000000000000000031ll;

inline li myMul (li a, li b, li m)
{
	li q = li(ld(a) * b / m);
	li ans = (a * b - q * m) % m;

	if (ans < 0)
		ans += m;

	return ans;
}

inline li norm (li a)
{
	if (a >= MOD)
		a -= MOD;

	if (a < 0)
		a += MOD;

	return a;
}

inline li hash(const string& s)
{
	int n = sz(s);
	li hash = 0;
	forn (i, n)
	{
		hash = myMul(hash, P, MOD);
		hash = norm(hash + s[i]);
	}

	return hash;
}

bitset<CNT> z[2];
bitset<CNT> idx[N]; 

inline void setV(int id, int v)
{
	z[id] |= (idx[v]);
}

inline bool has(int mask, int pos)
{
	return (mask & (1 << pos)) != 0;
}

inline int getId(li h)
{
	int idx = int(lower_bound(hs, hs + sz, h) - hs);
	return idx;
}

inline void solve(int test)
{
	cerr << test << endl;
	printf("Case #%d: ", test + 1);

	sort(hs, hs + sz);
	sz = int(unique(hs, hs + sz) - hs);

	forn(i, n)
		idx[i] = 0;

	forn(pos, n)
	{
		forn(j, sz(h[pos]))
		{
			li hh = h[pos][j];
			int id = getId(hh);
			idx[pos][id] = 1;
		}
	}

	int ans = INF;

	int rg = (1 << (n - 2));

	forn(mask, rg)
	{
		z[0] = z[1] = 0;

		setV(0, 0);
		setV(1, 1);

		forn(pos, (n - 2))
			if (has(mask, pos))
				setV(0, pos + 2);
			else
				setV(1, pos + 2);

		int res = (z[0] & z[1]).count();
		ans = min(ans, res);
	}

	cout << ans << endl;
}

int main()
{
#ifdef HP
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

	int testCnt;
	assert(cin >> testCnt);

	forn(test, testCnt)
	{
    	assert(read());
    	solve(test);
	}

    return 0;
}

