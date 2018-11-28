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

const int N = 4;
int n;
char buf[10];
int a[N][N];

inline bool read()
{
	if (scanf ("%d", &n) != 1)
		return false;
		
	forn (i, n)
	{
		assert(scanf ("%s", buf) == 1);
		
		forn (j, n)
			a[i][j] = buf[j] - '0';
	}
	
	return true;
}

int ans = 0;
int p[N];
bool ok = 1;
int used[N];

void gen(int pos)
{
	if (pos == n)
		return;	
		
	if (!ok)
		return;
		
	int id = p[pos];
	
	int f = 0;
		
	forn (i, n)
	{
		if (!a[id][i])
			continue;
			
		if (used[i])
			continue;
			
		used[i] = 1;
		f = 1;
		
		gen(pos + 1);
		
		used[i] = 0;
	}
	
	if (!f)
	{
		ok = 0;
		return;
	}
}

inline bool check (int mask)
{
	forn (i, n)
		forn (j, n)
			a[i][j] = ((mask >> (i * n + j)) & 1);
			
	forn (i, n)
		p[i] = i;
	ok = 1;
		
	do
	{
		forn (i, n)
			used[i] = 0;

		gen(0);
		
		if (!ok)
			return false;
	}
	while (next_permutation(p, p + n));
	
	return true;	
}

inline void updateAns (int mask, int cnt)
{
	//cerr << mask << ' ' << cnt << endl;
	if (cnt < ans && check(mask))
		ans = cnt;
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);
	
	int smask = 0;
	forn (i, n)
		forn (j, n)
			if (a[i][j])
				smask |= (1 << (i * n + j));
				
	ans = INF;
				
	updateAns(smask, 0);
	
	int rmask = (smask ^ ((1 << (n * n)) - 1));
	
	for (int submask = rmask; submask; submask = (submask - 1) & rmask)
	{
		int curMask = smask | submask;
		
		int cnt = 0;
		forn (i, n * n)
			cnt += ((submask >> i) & 1);
		
		updateAns(curMask, cnt);
	}
	
	cout << ans << endl;
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
