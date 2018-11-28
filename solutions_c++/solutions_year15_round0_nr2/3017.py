#include <bits/stdc++.h>

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

const int N = 1000 + 13;
int n;
int a[N];

inline void gen ()
{
	n = rand() % 6 + 1;
	forn (i, n)
		a[i] = rand() % 9 + 1;

	cout << n << endl;
	forn (i, n)
		cout << a[i] << ' ';
	cout << endl;
}

inline bool read()
{
	//gen();
	//return true;

	if (scanf ("%d", &n) != 1)
		return false;

	forn (i, n)
		assert(scanf ("%d", &a[i]) == 1);

	return true;
}

int nans;
unordered_set<li> used;

void brute (vector<int> s, int cur = 0)
{
	if (sz(s) == 0)
	{
		nans = min(nans, cur);
		return;
	}

	sort(all(s));
	li hash = 0;
	forn (i, sz(s))
		hash = hash * 1009 + s[i];

	if (used.count(hash))
		return;

	used.insert(hash);

	nans = min(nans, cur + s[sz(s) - 1]);

	{
		vector<int> ns;
		forn (i, sz(s))
			if (s[i] > 1)
				ns.pb(s[i] - 1);

		brute(ns, cur + 1);
	}

	forn (i, sz(s))
		if (s[i] > 1)
		{
			vector<int> ns;
			forn (j, sz(s))
				if (i != j)
					ns.pb(s[j]);

			for (int j = 1; j <= s[i] / 2; j++)
			{
				ns.pb(j);
				ns.pb(s[i] - j);

				brute(ns, cur + 1);

				ns.pop_back();
				ns.pop_back();
			}
		}
}

inline int naive()
{
	vector<int> s;
	forn (i, n)
		s.pb(a[i]);

	used.clear();

	nans = INF;
	brute(s);

	return nans;
}

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);

	if (n == 0)
	{
		puts("0");
		return;
	}

	int ans = INF;

	fore (need, 1, 1000)
	{
		int cur = need;
		forn (i, n)
			cur += (a[i] - 1) / need;

		ans = min(ans, cur);
	}

	//assert(ans == naive());

	printf ("%d\n", ans);
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
	assert(scanf("%d", &testCnt) == 1);

	forn(test, testCnt)
	{
		assert(read());
		solve(test);
	}

#ifdef SU2_PROJ
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}
