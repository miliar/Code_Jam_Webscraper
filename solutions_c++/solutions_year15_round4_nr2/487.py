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
typedef double ld;
typedef pair<int, int> pt;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9;
//const ld PI = acosl(ld(-1));

const int N = 2 + 3;
const int MAGIC = 300;

int n;
ld V;
ld C;

inline void readLd(ld& l) {
	double x;
	assert(scanf("%lf", &x) == 1);
	l = ld(x);
}

ld r[N];
ld c[N];

inline bool read() {
	assert(scanf("%d", &n) == 1);
	readLd(V);
	readLd(C);
	forn(i, n) {
		readLd(r[i]);
		readLd(c[i]);
	}
    return true;
}

inline ld f(ld v0) {
	return (v0 * c[0] + (V - v0) * c[1]) / V;
}

inline void solve(int test) {
	printf("Case #%d: ", test);
	if (n == 1) {
		if (abs(C - c[0]) < EPS) {
			printf("%.10f\n", V / r[0]);
			return;	
		}
		puts("IMPOSSIBLE");
		return;
	}
	if (abs(C - c[0]) < EPS && abs(C - c[1]) < EPS) {
		printf("%.10f\n", V / (r[0] + r[1]));
		return;
	}
	if (c[0] < c[1]) {
		swap(c[0], c[1]);
		swap(r[0], r[1]);
	}
	ld l = 0, r = V;
	forn(it, MAGIC) {
		ld m = (l + r) / 2;
		ld res = f(m);
		if (res > C)
			r = m;
		else
			l = m;
	}
	ld res = f(l);
	if (abs(res - C) > EPS) {
		puts("IMPOSSIBLE");
		return;
	}
//	cerr << l << " " << abs(res - C) << endl;
	printf("%.10f\n", max(l / ::r[0], (V - l) / ::r[1]));
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