#pragma comment(linker, "/stack:128000000")

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define x first
#define y second
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 8 + 1;
const int M = 4 + 1;
const int L = 10 + 3;

char buf[L];

int n, m;

string s[N];

inline bool read()
{
	if (scanf("%d%d", &n, &m) != 2)
		return false;

	forn(i, n)
	{
		assert(scanf("%s", buf) == 1);
		s[i] = string(buf);
	}

    return true;
}

vector<int> z[M];

int ANS, CNT;

int sz;

const int A = 26;

struct node
{
	int next[A];
};

const int SZ = N * L * 3;

node t[SZ];

inline void add(const string& s)
{
	int v = 0;

	forn(i, sz(s))
	{
		if (t[v].next[ s[i] - 'A' ] == -1)
		{
			t[v].next[ s[i] - 'A' ] = sz++;
		}

		v = t[v].next[ s[i] - 'A' ];
	}
}

inline int getAns()
{
	int ans = 0;

	forn(i, m)
	{
		forn(j, SZ)
			memset(t[j].next, -1, sizeof(t[j].next));

		sz = 1;

		forn(j, sz(z[i]))
			add(s[ z[i][j] ]);

		ans += sz;
	}

	return ans;
}

set< vector<int> > used;

inline void brute(int idx)
{
	if (idx == n)
	{
		bool ok = true;

		forn(i, m)
			if (sz(z[i]) == 0)
			{
				ok = false;			
				break;
			}

		if (!ok)
			return;

		int ans = getAns();

		if (ans >= ANS)
		{
			if (ans > ANS)
			{
				CNT = 0;
				//used.clear();
			}

			ANS = ans;

			/*vector<int> cur(n, 0);
			forn(i, m)
				forn(j, sz(z[i]))
					cur[ z[i][j] ] = i;

			used.insert(cur);*/
			CNT++;
		}

		return;
	}

	forn(i, m)
	{
		z[i].pb(idx);
		brute(idx + 1);
		z[i].pop_back();
	}
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	forn(i, m)
		z[i].clear();

	ANS = 0;
	CNT = 0;
	//used.clear();

	brute(0);

	//CNT = sz(used);

	cout << ANS << " " << CNT << endl;
}

int main()
{
#ifdef HP
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

	int testCnt;
	assert(scanf("%d", &testCnt) == 1);

	forn(test, testCnt)
	{
	    assert(read());
    	solve(test);
	}

    return 0;
}

