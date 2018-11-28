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

int n;
int a[N];
int b[N];

inline bool read()
{
	if (scanf("%d", &n) != 1) return false;
	
	forn(i, n) assert(scanf("%d", &a[i]) == 1), a[i]--;
	forn(i, n) assert(scanf("%d", &b[i]) == 1), b[i]--;
	
	return true;
}

vector<int> g[N];
vector<int> z[N];

int pos[N];
int z1[N], z2[N];

inline bool check()
{
	forn(i, n)
	{
		z1[i] = 1;
		
		forn(j, i)
			if (pos[j] < pos[i])
				z1[i] = max(z1[i], z1[j] + 1);
				
		if (z1[i] != a[i] + 1) return false;
	}
	
	ford(i, n)
	{
		z2[i] = 1;
		
		fore(j, i + 1, n - 1)
			if (pos[j] < pos[i])
				z2[i] = max(z2[i], z2[j] + 1);
				
		if (z2[i] != b[i] + 1) return false;
	}
	
	return true;
}

bool le[N][N];

inline void bfs(int s)
{
	forn(i, n) le[s][i] = false;
	queue<int> q;
	
	forn(i, sz(g[s]))
	{
		int to = g[s][i];
		
		if (!le[s][to])
		{
			le[s][to] = true;
			q.push(to);
		}
	}
	
	while (!q.empty())
	{
		int v = q.front();
		q.pop();
		
		forn(i, sz(g[v]))
			if (!le[s][g[v][i]])
			{
				le[s][g[v][i]] = true;
				q.push(g[v][i]);
			}
	}
}

int perm[N];

inline bool cmp(int a, int b)
{
	if (le[a][b]) return true;
	if (le[b][a]) return false;
	return a < b;
}

inline void solve(int test)
{
	printf("Case #%d:", test + 1);
	
	forn(i, n) g[i].clear();
	
	forn(i, n) z[i].clear();
	
	forn(i, n)
	{
		forn(j, a[i])
			g[z[j].back()].pb(i);
		if (!z[a[i]].empty()) g[i].pb(z[a[i]].back());
		z[a[i]].pb(i);
	}
	
	forn(i, n) z[i].clear();
	
	ford(i, n)
	{
		forn(j, b[i])
			g[z[j].back()].pb(i);
		if (!z[b[i]].empty()) g[i].pb(z[b[i]].back());
		z[b[i]].pb(i);
	}
	
	forn(i, n) bfs(i);
	
	forn(i, n) perm[i] = i;
	sort(perm, perm + n, cmp);
	
	forn(i, n) pos[perm[i]] = i;
	
	assert(check());
	
	forn(i, n) printf(" %d", pos[i] + 1);
	puts("");
	
	cerr << test << endl;
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
