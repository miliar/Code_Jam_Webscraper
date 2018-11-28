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

const int N = 3e5 + 10;
const int INF = 2e9;


string s[N];

int main(){    
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	assert(freopen("in", "r", stdin));
	assert(freopen("out", "w", stdout));
	int t; cin >> t;
	forab(q, 1, t + 1) {
		string s; cin >> s;
		forn(i, sz(s))
			if (s[i] == '-') s[i] = 0;
			else s[i] = 1;
		int bad = 0, ans = 0;
		fornr(i, sz(s)) {
			if (s[i] == bad) {
				ans++;
				while (i >= 0 && s[i] == bad)
					i--;
				i++;
				bad = 1 - bad;			
			}
		}		
		cout << "Case #" << q <<": " << ans << '\n';
	}
	return 0;	
}
