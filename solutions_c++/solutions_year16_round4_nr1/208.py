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

const char* ALPHA = "RPS";
int b[3], lose[3], cnt[3], m;
string s[3];

void calc(int depth, int cur) {
 	if (depth == 0) {
 		cnt[cur]++;
 		return;
 	}
 	calc(depth - 1, cur);
 	forn (j, 3)
 		if (lose[j] == cur)
 			calc(depth - 1, j);
}

string print(int depth, int cur) {
 	if (depth == 0) {
 		string s0 = "";
 		s0.pb(ALPHA[cur]);
 		return s0;
 	}
 	int a = cur, b = 0;
 	forn (j, 3)
 		if (lose[j] == cur)
 			b = j;
 	string s1 = print(depth - 1, a), s2 = print(depth - 1, b);
 	if (s1 > s2)
		swap(s1, s2);
	return s1 + s2;
}

int main() {
#ifdef LOCAL    
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout); 
#endif    
	
	int t;
	scanf("%d", &t);
	lose[0] = 1, lose[1] = 2, lose[2] = 0;
	forn (tt, t) {
		int n;
		scanf("%d%d%d%d", &n, &b[0], &b[1], &b[2]);
		printf("Case #%d: ", tt + 1);
		bool was = 0;
		forn (j, 3)
			s[j] = "";
		m = 0;
		forn (j, 3) {
			forn (g, 3)
				cnt[g] = 0;
			cnt[j] = 1;
			int l = 0;
			forn (g, 3)
				if (lose[g] == j)
					l = g;
			forn (i, n)
				calc(i, l);			
			bool ok = 1;
			forn (j, 3)
				if (cnt[j] != b[j])
					ok = 0;
			if (ok) {
				s[m++] = print(n, j);
				was = 1;
			}
		}
		if (!was)
			puts("IMPOSSIBLE");
		else {
			sort(s, s + m);
			cout << s[0] << endl;
		}
	}	

	return 0;
}