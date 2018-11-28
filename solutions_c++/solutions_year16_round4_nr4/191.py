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

const int MAX_N = 30;

int p[MAX_N], a[MAX_N][MAX_N], a0[MAX_N][MAX_N], used[MAX_N];
char s[MAX_N];

bool go(int k, int n) {
 	if (k == n)
 		return 1;
 	bool was = 0;
   	forn (i, n)
 		if (!used[i] && a[p[k]][i]) {
 			used[i] = 1;
 			if (go(k + 1, n) == 0) {
 		        used[i] = 0;
 				return 0;
 			}
 			used[i] = 0;
 			was = 1;
 		}
	if (!was)
		return 0;
   	return 1;
}

int main() {
#ifdef LOCAL    
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout); 
#endif    
	
	int t;
	scanf("%d", &t);	
	forn (tt, t) {
		int n;
		scanf("%d\n", &n);
		forn (i, n) {
			gets(s);
			forn (j, n)
				a0[i][j] = s[j] - '0';
		}
		int ans = n * n;
		forn (mask, (1 << (n * n))) {
			//printf("%d\n", mask);
			forn (i, n)
				forn (j, n)
					a[i][j] = a0[i][j] | ((mask >> (i * n + j)) & 1);
			bool ok = 1;
			forn (i, n)
				p[i] = i;
			do {
            	ok &= go(0, n);
			} while (next_permutation(p, p + n));
			if (ok)
				ans = min(ans, __builtin_popcount(mask));
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	//printf("%.20f\n", clock() * 1. / CLOCKS_PER_SEC);
	return 0;
}