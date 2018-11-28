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
//const ld PI = acosl(ld(-1));

int n;

inline bool read() {
	if (scanf("%d", &n) != 1)
		return false;
    return true;
}

const int N = 1000 + 13;
int cnt[N];

inline void solve(int test) {
	memset(cnt, 0, sizeof cnt);
	forn(i, n) {
		int x;
		assert(scanf("%d", &x) == 1);
		cnt[x]++;
	}
	int ans = 0;
	forn(i, N)
		if (cnt[i])
			ans = i;
	fore(i, 1, N - 1) {
		int add = 0;
		fore(j, i + 1, N - 1) {
			if (!cnt[j])
				continue;
			add += cnt[j] * ((j - 1) / i);
		}
		ans = min(ans, i + add);
	}
	printf("Case #%d: %d\n", test, ans);
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
	
    int n;
    assert(scanf("%d", &n) == 1);
    forn(i, n) {
	    assert(read());
    	solve(i + 1);
    }

#ifdef SU2_PROJ
    cerr << "TIME: " << clock() << endl;
#endif

    return 0;
}