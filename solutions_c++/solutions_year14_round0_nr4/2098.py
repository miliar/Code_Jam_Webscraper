#undef NDEBUG
#ifdef SU2_PROJ
#define _GLIBCXX_DEBUG
#endif

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

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

const int N = 1000 + 13;

int n;
int a[2][N];

inline bool read()
{
	if (scanf("%d", &n) != 1) return false;
	
	char buf[10];
	
	forn(it, 2) forn(i, n)
	{
		assert(scanf("%s", buf) == 1);
		int len = strlen(buf);
		while (len < 7) buf[len++] = '0';
		
		a[it][i] = 0;
		fore(j, 2, len - 1) a[it][i] = a[it][i] * 10 + buf[j] - '0';
	}
	
	return true;
}

int used[N];

inline void solve(int test)
{
	printf("Case #%d: ", test);
	
	forn(it, 2) sort(a[it], a[it] + n);
	
	//forn(it, 2) { forn(i, n) cerr << a[it][i] << ' '; cerr << endl; } cerr << endl;
	
	int cnt[] = { 0, 0 };
	
	forn(iter, 2)
	{
		memset(used, 0, sizeof(used));
		
    	forn(i, n)
    	{
    		bool beat = false;
    		forn(j, n) if (!used[j] && a[0][j] > a[1][i])
    		{
    			used[j] = true;
    			beat = true;
    			break;
    		}
    		if (beat) cnt[iter]++;
    	}
    	
    	forn(i, n) swap(a[0][i], a[1][i]);
    	if (iter == 1) cnt[iter] = n - cnt[iter];
	}
	
	printf("%d %d\n", cnt[0], cnt[1]);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	int testCount;
	cin >> testCount;
	
	forl(test, testCount)
	{
		assert(read());
		solve(test);
#ifdef SU2_PROJ
		cerr << test << ' ' << clock() << endl;
#endif
	}
	
	return 0;
}
