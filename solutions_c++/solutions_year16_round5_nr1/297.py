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

const int MAX_N = 2e4 + 5;

char s[MAX_N];

inline short get(int ind1, int ind2) {
 	return 1 + (s[ind1] == s[ind2]);
}

int main() {
#ifdef LOCAL    
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout); 
#endif    
	
	int t;
	scanf("%d\n", &t);
	forn (tt, t) {
		gets(s);
		int n = strlen(s);
		int ans = 0;
		int k = n / 2;
		forn (i, k) {
			bool was = 0;
			forn (j, n - 1)				
				if (s[j] == s[j + 1]) {
				 	forab (g, j, n - 2)
				 		s[g] = s[g + 2];
				 	was = 1;
				 	break;
				}
			if (!was) {
				ans += (n / 2) * 5;
				break;
			}
			ans += 10;
			n -= 2;
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}	
	return 0;
}