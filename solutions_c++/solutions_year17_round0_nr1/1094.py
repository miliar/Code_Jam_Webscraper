#include<bits/stdc++.h>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i < int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
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

mt19937 mt(time(NULL));

const int N = 1000 + 3;
int n, k;
char s[N];

inline bool read()
{
	if (scanf ("%s%d", s, &k) != 2)
		return false;
		
	n = int(strlen(s));

	return true;
}

int r[N];

inline void solve(int test)
{
	printf ("Case #%d: ", test + 1);
	
	memset(r, 0, sizeof r);
	
	int ans = 0;
	
	int cur = 0;
	forn (i, n) {
		cur ^= r[i];
		int c = (s[i] == '+');
		if (!(c ^ cur)) {
			cur ^= 1;
			if (i + k > n) {
				puts("IMPOSSIBLE");
				return;
			}

			ans++;
			r[i + k] ^= 1;
		}
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
	
	int testCnt;
	assert(scanf ("%d", &testCnt) == 1);

	forn (test, testCnt) {
		assert(read());
		solve(test);
	}

#ifdef SU2_PROJ
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}
