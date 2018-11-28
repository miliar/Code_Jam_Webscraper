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

typedef long long LL;
typedef unsigned long long ULL;
typedef double dbl;
typedef long double LD;
typedef unsigned int uint;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int N = 3e3 + 10;
const int INF = 2e9;

int a[N], used[N], marked[N], best[N];

int main(){    
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	assert(freopen("in", "r", stdin));
	assert(freopen("out", "w", stdout));
	int t;
	cin >> t;
	forn(q, t) {
		int n;
		cin >> n;
		forn(i, n) {
			marked[i] = 0;
			best[i] = 0;
			cin >> a[i];
			--a[i];
		}
		int ans = 0;
		forn(i, n) {
			forn(j, n)
				used[j] = 0;
			int len = 0, pos = i; 
			while (!used[pos]) {
				used[pos] = 1;
				len++;
				pos = a[pos];
			}
			if (pos == i) 
				ans = max(ans, len);
			if (len == 2) 
				marked[i] = marked[a[i]] = 1;
		}
		forn(i, n) {
			forn(j, n)
				used[j] = 0;
			int len = 0, pos = i; 
			while (!used[pos]) {
				used[pos] = 1;
				if (marked[pos]) {
					best[pos] = max(best[pos], len);
					break;
				}
				len++;
				pos = a[pos];
			}
		}
		int ans2 = 0;
		forn(i, n) {
			if (marked[i]) {
				ans2 += best[i] + 1;			
			}
		}
		assert(max(ans, ans2) <= n);
		cout << "Case #" << q + 1 << ": " << max(ans, ans2) << "\n";
	}
  
	return 0;	
}
