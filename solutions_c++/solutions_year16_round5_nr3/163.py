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
//typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;
const ld PI = acosl(ld(-1));

struct pt
{
	int x;
	int y;
	int z;
	
	pt() {};
	pt(int x, int y, int z) : x(x), y(y), z(z) {}
};

const int N = 1000 + 13;
int n, s;
pt a[N], v[N];

inline bool read()
{
	if (scanf ("%d%d", &n, &s) != 2)
		return false;
		
	forn (i, n)
	{
		assert(scanf ("%d%d%d", &a[i].x, &a[i].y, &a[i].z) == 3);
		assert(scanf ("%d%d%d", &v[i].x, &v[i].y, &v[i].z) == 3);		
	}
	
	return true;
}

inline ld getDist (const pt& a, const pt& b)
{
	return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y) + sqr(a.z - b.z));
}

int used[N], q[N], head, tail;

inline bool f (ld maxD)
{
	head = tail = 0;
	forn (i, n)
		used[i] = 0;
		
	used[0] = 1;
	q[tail++] = 0;
	
	while (head != tail && !used[1])
	{
		int v = q[head++];
		
		forn (i, n)
		{
			if (used[i])
				continue;
				
			if (getDist(a[i], a[v]) > maxD + EPS)
				continue;
				
			used[i] = 1;
			q[tail++] = i;
		}
	}
	
	return used[1];
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);
	
	ld l = 0, r = 1e9;
	forn (it, 200)
	{
		ld mid = (l + r) / ld(2);
		
		if (f(mid))
			r = mid;
		else
			l = mid;
	}
	
	printf ("%.15f\n", double(r));
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
