#define FNAME ""

#undef __STRICT_ANSI__

#include <bits/stdc++.h> 

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define fst first
#define snd second
#define sz(x) (int)((x).size()) 
#define forn(i,n) for (int i = 0; (i) < (n); ++i)
#define fornr(i,n) for (int i = (int)(n) - 1; (i) >= 0; --i)
#define forab(i,a,b) for (int i = (a); (i) < (b); ++i)
#define forba(i,a,b) for (int i = (int)(b) - 1; (i) >= (a); --i)
#define forit(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(),(c).end()

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) static_cast<void>(0)   
#endif

#ifdef _WIN32
	#define I64 "%I64d"
	#define U64 "%I64u"
#else
	#define I64 "%lld"
	#define U64 "%llu"
#endif

typedef long long LL;
typedef unsigned long long ULL;
typedef double dbl;
typedef long double LD;
typedef unsigned int uint;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int N = 100;

double a[N], dp[N][N];

int main() {
	int t;
	cin >> t;
	forn(q, t) {
		memset(dp, 0, sizeof(dp));
		int n, k;
		cin >> n >> k;
		forn(i, n)
			cin >> a[i];
		double ans = 0;
		forn(mask, (1 << n)) {
			if (__builtin_popcount(mask) != k)
				continue;
			vector <double> p;
			p.pb(0.);
			forn(i, n) {
				if ((1 << i) & mask)
					p.pb(a[i]);
			}
			dp[0][0] = 1;
			forab(i, 1, k + 1) {
				forn(j, k + 1) {
					if (!j) {
						dp[i][j] = dp[i - 1][j] * (1 - p[i]);
					} else {
						dp[i][j] = dp[i - 1][j] * (1 - p[i]) + dp[i - 1][j - 1] * p[i];
					}
				}
			}
			ans = max(dp[k][k / 2], ans);
	//		cerr << ans << " " << mask << '\n';
		}
		cout.precision(15);
		cout << fixed << "Case #" << q + 1 << ": " << ans << '\n';
	}
	return 0;
}
