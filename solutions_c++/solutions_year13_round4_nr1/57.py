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
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int N = 2000 + 3;

int n, m;
pair<pt, int> a[N];

inline bool read()
{
	if (scanf("%d%d", &n, &m) != 2) return false;
	forn(i, m) assert(scanf("%d%d%d", &a[i].ft.x, &a[i].ft.y, &a[i].sc) == 3);
	return true;
}

const li mod = 1000002013;

struct event
{
	int x, type, cnt;
	event() { }
	event(int x, int type, int cnt): x(x), type(type), cnt(cnt) { }
};

inline bool operator< (const event& a, const event& b)
{
	if (a.x != b.x) return a.x < b.x;
	if (a.type != b.type) return a.type > b.type;
	return a.cnt < b.cnt;
}

inline li cost(int x, int y)
{
	int k = y - x;
	if (k == 0) return 0;
	li ans = li(n) * k - li(k) * (k - 1) / 2;
	ans %= mod;
	(ans < 0) && (ans += mod);
	return ans;
}

int szev;
event ev[N];

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	szev = 0;
	
	forn(i, m)
	{
		ev[szev++] = event(a[i].ft.x, +1, a[i].sc);
		ev[szev++] = event(a[i].ft.y, -1, a[i].sc);
	}
	
	sort(ev, ev + szev);
	
	li ans = 0;
	
	multiset<pt, greater<pt> > val;
	
	forn(i, szev)
	{
		if (ev[i].type == -1)
		{
			int cnt = ev[i].cnt;
			
			while (cnt > 0)
			{
				assert(!val.empty());
				pt p = *val.begin();
				val.erase(val.begin());
				int cur = min(cnt, p.sc);
				ans += (cur % mod) * 1ll * cost(p.ft, ev[i].x);
				ans %= mod;
				cnt -= cur;
				p.sc -= cur;
				if (p.sc > 0) val.insert(p);
			}
		}
		else
			val.insert(mp(ev[i].x, ev[i].cnt));
	}
	
	li sum = 0;
	
	forn(i, m)
	{
		sum += cost(a[i].ft.x, a[i].ft.y) * 1ll * (a[i].sc % mod);
		sum %= mod;
	}
	
	//cerr << sum << ' ' << ans << endl;
	
	ans = sum - ans;
	ans %= mod;
	(ans < 0) && (ans += mod);
	
	cout << ans << endl;
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
        assert(read());
        solve(test);
    }
	
    return 0;
}
