#include <bits/stdc++.h> 

using namespace std;
 
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(x) (int) ((x).size()) 
#define forn(i, n) for (int i = 0; (i) < (n); ++i)
#define fornr(i, n) for (int i = (n) - 1; (i) >= 0; --i)
#define forab(i, a, b) for (int i = (a); (i) < (b); ++i)
#define forba(i, a, b) for (int i = (b) - 1; (i) >= (a); --i)
#define forit(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(), (c).end() 

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) static_cast<void>(0)   
#endif

#ifdef _WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
typedef vector <int> vi;
typedef pair <int, int> pii;

#define FNAME ""

const int MAX_N = 505;

double dp[MAX_N][MAX_N], a[MAX_N];
vector<double> v;

double calc(vector<double> v) {
 	int n = sz(v);
 	dp[0][0] = 1;
 	forn (i, n) {
 	    forn (j, 2 * n + 5)
 	    	dp[i + 1][j] = 0;
 	 	forn (j, i + 2) {
 	        double s = 0;
 	        if (j != 0)
 	        	s = dp[i][j - 1];
 			dp[i + 1][j] = s * v[i] + dp[i][j] * (1 - v[i]);
 			//printf("dp[%d][%d] = %.20f\n", i + 1, j, dp[i + 1][j]);
 	 	}
 	}
 	return dp[n][n / 2];
}

int main() {
#ifdef LOCAL    
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout); 
#endif    
	
	int t;
	scanf("%d", &t);
	forn (tt, t) {
		int n, k;
		scanf("%d%d", &n, &k);
		forn (i, n)
			scanf("%lf", &a[i]);
		sort(a, a + n);
		double ans = 0;
		forn (i, k + 1) {
		    v.clear();
			forn (j, i)
				v.pb(a[j]);
			forn (j, k - i)
				v.pb(a[n - 1 - j]);
			sort(all(v));
    		ans = max(ans, calc(v));
		}	
		printf("Case #%d: %.20f\n", tt + 1, ans);
	}	

	return 0;
}