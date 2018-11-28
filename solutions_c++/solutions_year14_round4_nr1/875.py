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

const int N = 10 * 1000 + 3;

int n, x;
int a[N];

inline bool read()
{
	if (scanf("%d%d", &n, &x) != 2)
		return false;

	forn(i, n)
		assert(scanf("%d", &a[i]) == 1);

    return true;
}

int used[N];

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	memset(used, false, sizeof(used));
	sort(a, a + n);
	set<pt> z;

	forn(i, n)
		z.insert(mp(a[i], i));

	int ans = 0;

	ford(i, n)
	{
		if (used[i])
			continue;

		assert(z.count(mp(a[i], i)));
		z.erase(mp(a[i], i));
		used[i] = true;

		ans++;
		int rem = x - a[i];
		assert(rem >= 0);

		set<pt>:: iterator it = z.upper_bound(mp(rem, INF));

		if (it != z.begin())
		{
			it--;
	
			assert(it != z.end());

			{
				int val = (*it).ft;
				int idx = (*it).sc;

				assert(!used[idx]);
				assert(val <= rem);

				used[idx] = true;
				z.erase(it);
			}
		}
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
	assert(scanf("%d", &testCnt) == 1);

	forn(test, testCnt)
	{
	    assert(read());
    	solve(test);
	}

    return 0;
}

