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

const int N = 2 * 1000 + 3;

int n;
char t[N];
int idx[N];

inline bool read()
{
	if (scanf("%d", &n) != 1) return false;
	
	forn(i, n)
	{
		assert(scanf(" %c %d", &t[i], &idx[i]) == 2);
		idx[i]--;
	}
	
	return true;
}

int ans;
char s[N];

void solve(int pos, int last)
{
	if (pos == n)
	{
		int cur = 0;
		forn(i, last) cur += int(s[i] == 'E');
		ans = min(ans, cur);
		return;
	}
	
	if (idx[pos] != -1)
	{
		int v = idx[pos];
		
		if (s[v] == t[pos]) return;
		
		char old = s[v];
		s[v] = t[pos];
		solve(pos + 1, last);
		s[v] = old;
	}
	else
	{
		forn(v, last + 1)
		{
			if (s[v] != t[pos])
			{
				char old = s[v];
				s[v] = t[pos];
				solve(pos + 1, max(last, v + 1));
				s[v] = old;
			}
		}		
	}
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	vector<int> v;
	forn(i, n)
		if (idx[i] != -1)
			v.pb(idx[i]);
			
	sort(all(v));
	v.erase(unique(all(v)), v.end());
	
	forn(i, n)
		if (idx[i] != -1)
			idx[i] = int(lower_bound(all(v), idx[i]) - v.begin());
			
	ans = INF;
	memset(s, '?', sizeof s);
	solve(0, sz(v));
	
	if (ans > INF / 2)
		puts("CRIME TIME");
	else
		printf("%d\n", ans);
}

int main()
{
#ifdef SU2_PROJ
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;
    
    srand(time(NULL));
    
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
