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

const int N = 100 + 13;
const int MASK = (1 << 8) + 13;

int n, m;
string s[N];

inline bool read()
{
	if (scanf("%d%d", &n, &m) != 2) return false;
	
	char buf[50 + 3];
	
	forn(i, n)
	{
		assert(scanf("%s", buf) == 1);
		s[i] = string(buf);
	}
	
	return true;
}

int szt = 1;
int cost[MASK];

int next[N][26];

inline void add(const string& s)
{
	int v = 0;
	forn(i, sz(s))
	{
		int c = int(s[i] - 'A');
		
		if (next[v][c] == -1)
			next[v][c] = szt++;
			
		v = next[v][c];
	}
}

int z[N][MASK][N];
int u, used[N][MASK][N];

const int mod = 1000000007;

inline int add(int a, int b)
{
	int res = a + b;
	while (res >= mod) res -= mod;
	return res;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	memset(next, -1, sizeof next);
	
	forn(mask, 1 << n)
	{
		if (mask == 0) continue;
		
		forn(i, szt) memset(next[i], -1, sizeof next[i]);
		
		szt = 1;
		forn(i, n)
			if (mask & (1 << i))
				add(s[i]);
				
		cost[mask] = szt;
	}
	
	u++;
	memset(z, 0, sizeof z);
	
	z[0][(1 << n) - 1][0] = 1;
	used[0][(1 << n) - 1][0] = u;
	
	forn(i, m)
		forn(mask, 1 << n)
			forn(sum, N)
			{
				const int& dv = z[i][mask][sum];
				if (used[i][mask][sum] != u) continue;
				
				for (int curmask = mask; curmask > 0; curmask = (curmask - 1) & mask)
				{
					int ni = i + 1, nmask = mask ^ curmask, nsum = sum + cost[curmask];
					assert(sum < N);
					
					z[ni][nmask][nsum] = add(z[ni][nmask][nsum], dv);
					used[ni][nmask][nsum] = u;
				}
			}
			
	int ansx = -1, ansy = -1;
	
	forn(sum, N)
		if (used[m][0][sum] == u)
		{
			ansx = sum, ansy = z[m][0][sum];
		}
		
	assert(ansx != -1);
	cout << ansx << ' ' << ansy << endl;
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
    
#ifdef SU2_PROJ
    cerr << "== TIME: " << clock() << " ==" << endl;
#endif

    return 0;
}
