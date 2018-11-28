#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <iomanip>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;
const ld PI = acosl(ld(-1));

int n, r, p, s;

inline bool read()
{
	if (scanf ("%d%d%d%d", &n, &r, &p, &s) != 4)
		return false;

	return true;
}

int cnt[3];
const char dc[3] = {'R', 'P', 'S'};
int a[(1 << 12) + 3], na[(1 << 12) + 3];
string ans, cur;

inline bool cmp (int i1, int i2, int len)
{
	forn(it, len)
	{
		if (cur[i1 + it] > cur[i2 + it])
			return true;
		if (cur[i1 + it] < cur[i2 + it])
			return false;
	}

	return false;	
}

inline void updateAns ()
{
	cur.resize(1 << n);
	
	forn (i, (1 << n))
		cur[i] = dc[ a[i] ];
		
	for (int j = 0; j < n; j++)
		for (int i = 0; i < (1 << n); i += (1 << (j + 1)))
		{
			//cerr << (1 << j) << ' ' << i << endl;
	
			if (cmp(i, i + (1 << j), (1 << j)))
				fore(it, i, i + (1 << j) - 1)
					swap(cur[it], cur[it + (1 << j)]);
		}
	
	if (ans == "" || ans > cur)
		ans = cur;
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);
	
	ans = "";
	
	forn (it, 3)
	{
		a[0] = it;
		
		for (int i = 1; i <= n; i++)
		{
			int nsz = 0;
			forn (j, (1 << (i - 1)))
			{
				na[nsz++] = a[j];
				na[nsz++] = (a[j] - 1 + 3) % 3;
			}
			
			forn (j, nsz)
				a[j] = na[j];
		}
		
		forn (i, 3)
			cnt[i] = 0;
			
		forn (j, (1 << n))
			cnt[ a[j] ]++;
			
		if (cnt[0] == r && cnt[1] == p && cnt[2] == s)
			updateAns();
	}
	
	if (ans != "")
		printf ("%s\n", ans.c_str());
	else	
		puts("IMPOSSIBLE");
}

int main()
{
#ifdef SU2_PROJ
	assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	cout << setprecision(25) << fixed;
	cerr << setprecision(10) << fixed;

	srand(int(time(NULL)));
	
	int testCnt;
	assert(scanf ("%d", &testCnt) == 1);

	forn (test, testCnt)
	{
		assert(read());
		solve(test);
	}

#ifdef SU2_PROJ
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}
