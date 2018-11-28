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

const int D = 5 + 1;

int c, d, v;
int a[D];

inline bool read()
{
	if (!(cin >> c >> d >> v))
		return false;

	forn(i, d)
		assert(cin >> a[i]);

    return true;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	assert(c == 1);

	set<int> z;
	forn(mask, (1 << d))
	{
		int val = 0;
		forn(i, d)
			if ((mask & (1 << i)) != 0)
				val += a[i];

		z.insert(val);
	}

	int ans = 0;
	while(true)
	{
		int minv = -1;
		fore(i, 1, v)
			if (!z.count(i))
			{
				minv = i;
				break;
			}

		if (minv == -1)
			break;

		ans++;

		vector<int> cur(all(z));
		z.insert(minv);
		forn(i, sz(cur))
			z.insert(cur[i] + minv);
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

