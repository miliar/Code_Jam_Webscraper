#undef NDEBUG
#ifdef SU2_PROJ
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
inline ostream& operator<< (ostream& out, const pt& p) { return out << '(' << p.x << ", " << p.y << ')'; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int N = 100 + 3;
const int HP = 200 + 3;
const int STEP = 3 * 1000 + 13;

int p, q, n;
int h[N], g[N];

inline bool read()
{
	if (scanf("%d%d%d", &p, &q, &n) != 3) return false;
	
	forn(i, n)
		assert(scanf("%d%d", &h[i], &g[i]) == 2);
	
	return true;
}

int z[N][HP][STEP][2];

int solve(int idx, int hp, int cnt, int who)
{
	if (idx == n) return 0;
	if (hp <= 0) return solve(idx + 1, h[idx + 1], cnt, who);

	cnt = min(cnt, STEP - 1);	
	
	int &ans = z[idx][hp][cnt][who];
	if (ans != -1) return ans;
	
	if (who == 1) return ans = solve(idx, hp - q, cnt + 1, 0);
	
	ans = 0;
	
	if (cnt > 0)
	{
		int cost = 0;
		if (hp <= p) cost = g[idx];
		ans = max(ans, cost + solve(idx, hp - p, cnt - 1, who));
	}

	ans = max(ans, solve(idx, hp, cnt, who ^ 1));
	
	return ans;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	h[n] = g[n] = 0;
	memset(z, -1, sizeof z);
	
	cout << solve(0, h[0], 1, 0) << endl;
}

int main()
{
#ifdef SU2_PROJ
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
    	cerr << test << endl;
	    assert(read());
    	solve(test);
    }
    
#ifdef SU2_PROJ
    cerr << "== TIME: " << clock() << " ==" << endl;
#endif

    return 0;
}
