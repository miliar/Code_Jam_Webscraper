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

const int N = 12;

int a[1 << N];

string ans(vector <string> vp, vector <string> vs, vector <string> vr) {
	vector <string> newp, news, newr;
	int p = sz(vp), s = sz(vs), r = sz(vr);	
	if (p + s + r == 1) {
		if (p)
			return vp[0];
		if (s)
			return vs[0];
		if (r)
			return vr[0];
		assert(0);
	}
//	cerr << "new : " << p << " " << r << " " <<s << '\n';
	int pr = 0, ps = 0, rs = 0;
	if (s > r)
		ps = s - r, p -= ps, s = r;
	else if (r > s) 
		pr = r - s, p -= pr, r = s;
//	cerr << p << " " << r << " " << s << '\n';
	if (p & 1 || p > r + s || p < 0) {
		return "IMPOSSIBLE";	
	} 		
	p /= 2;
	pr += p, ps += p;
	r -= p, s -= p;
	rs = r;
//	cerr << "pr " << pr << " " << ps << " " << rs << '\n';
	forn(i, pr) {
		newp.pb(min(vp.back() + vr.back(), vr.back() + vp.back()));
		vr.pop_back();
		vp.pop_back();	
	}
	forn(i, ps) {
		news.pb(min(vp.back() + vs.back(), vs.back() + vp.back()));
		vs.pop_back();
		vp.pop_back();	
	}
	forn(i, rs) {
		newr.pb(min(vs.back() + vr.back(), vr.back() + vs.back()));
		vr.pop_back();
		vs.pop_back();	
	}
	sort(all(newr));
	reverse(all(newr));
	sort(all(news));
	reverse(all(news));
	sort(all(newp));
	reverse(all(newp));
//	cerr << sz(newp) << " " << sz(news) << " " << sz(newr) << '\n';
	return ans(newp, news, newr);
}

int main() {
	int t;
	cin >> t;
	forn(q, t) {
		int n, r, p, s; cin >> n >> r >> p >> s;
		vector <string> vr;
		forn(i, r)
			vr.pb("R");
		vector <string> vs;
		forn(i, s)
			vs.pb("S");
		vector <string> vp;
		forn(i, p)
			vp.pb("P");
		cout << "Case #" << q + 1 << ": " << ans(vp, vs, vr) << '\n';
	}
	return 0;
}
