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

const int N = 20 + 3;
int n;
vector<string> s[N];
string ss;

inline bool read()
{
	if (scanf ("%d", &n) != 1)
		return false;

	getline(cin, ss);

	forn (i, n)
	{
		s[i].clear();

		getline(cin, ss);

		stringstream e;
		e << ss;

		string cur;
		while (e >> cur)
		{
			s[i].pb(cur);
		}
	}

	return true;
}

map<string, int> name;
vector<int> a[N];

inline int getName (const string& s)
{
	if (!name.count(s))
	{
		int sz = sz(name);

		name[s] = sz;
	}

	return name[s];
}

const int M = 100 * 1000 + 13;
int eng[M], fr[M];

int cur = 0;

inline void addEng (int id)
{
	forn (i, sz(a[id]))
	{
		if (eng[ a[id][i] ] == 0 && fr[ a[id][i] ] > 0)
			cur++;

		eng[ a[id][i] ]++;
	}
}

inline void addFr (int id)
{
	forn (i, sz(a[id]))
	{
		if (fr[ a[id][i] ] == 0 && eng[ a[id][i] ] > 0)
			cur++;

		fr[ a[id][i] ]++;
	}
}

inline void delEng (int id)
{
	forn (i, sz(a[id]))
	{
		eng[ a[id][i] ]--;

		if (eng[ a[id][i] ] == 0 && fr[ a[id][i] ] > 0)
			cur--;
	}
}

inline void delFr (int id)
{
	forn (i, sz(a[id]))
	{
		fr[ a[id][i] ]--;

		if (fr[ a[id][i] ] == 0 && eng[ a[id][i] ] > 0)
			cur--;
	}
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);

	name.clear();
	forn (i, n)
	{
		a[i].clear();

		forn (j, sz(s[i]))
			a[i].pb(getName(s[i][j]));
	}

	memset(eng, 0, sizeof eng);
	memset(fr, 0, sizeof fr);
	cur = 0;

	addEng(0);
	addFr(1);

	int ans = INF;

	for (int mask = 0; mask < (1 << (n - 2)); mask++)
	{
		forn (i, n - 2)
			if ((mask >> i) & 1)
				addEng(2 + i);
			else
				addFr(2 + i);

		ans = min(ans, cur);

		forn (i, n - 2)
			if ((mask >> i) & 1)
				delEng(2 + i);
			else
				delFr(2 + i);
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
