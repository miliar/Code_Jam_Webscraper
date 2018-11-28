#include <bits/stdc++.h>
using namespace std;

#ifdef WIN32
    #define lld "%I64d"
#else
    #define lld "%lld"
#endif

#define mp make_pair
#define pb push_back
#define put(x) { cout << #x << " = "; cout << (x) << endl; }

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef double db;
typedef pair<pair<int, int>, pair<int, int> > pp;

const int M = 5000;
const int Q = 1e9 + 7;
const int N = 12;

struct sost {
	int n;
	int P, R, S;
	int win;
	sost() {}
	sost(int _n, int p, int r, int s, int w) : n(_n), P(p), R(r), S(s), win(w) {}
};

int winner(int a, int b) {
	if (a > b) swap(a, b);
	if (a == 0 && b == 1) return 0;
	if (a == 1 && b == 2) return 1;
	if (a == 0 && b == 2) return 2;
	assert(0);
}

vector<sost> g[N];
map<pp, bool> kek;
map<pp, pp> le;
map<pp, pp> ri;




string gen(pair<pair<int, int>, pair<int, int> > x) {
	int xn = x.first.first, xp = x.first.second, xr = x.second.first, xk = x.second.second;
	if (xn == 0) {
		if (xp)
			return "P";
		if (xr)
			return "R";
		return "S";
	}
	return gen(le[x]) + gen(ri[x]);
}
int main(){
    srand(time(NULL));
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	g[0].pb(sost(0, 1, 0, 0, 0));
	g[0].pb(sost(0, 0, 1, 0, 1));
	g[0].pb(sost(0, 0, 0, 1, 2));
	for (int i = 0; i < N; i++) {
		map<pair<pair<int, int>, int>, bool> used;
		for (sost& s1 : g[i]) {
			for (sost& s2 : g[i]) {
				if (s1.win == s2.win) continue;
				pair<pair<int, int>, int> ppx = mp(mp(s1.P + s2.P, s1.R + s2.R), winner(s1.win, s2.win));
				if (used[ppx]) continue;
				used[ppx] = true;
				sost ss = sost(i+ 1, s1.P + s2.P, s1.R + s2.R, s1.S + s2.S, winner(s1.win, s2.win));
				pp k = mp(mp(i + 1, s1.P + s2.P), mp(s1.R + s2.R, winner(s1.win, s2.win)));
				kek[k] = true;
				le[k] = mp(mp(i, s1.P), mp(s1.R, s1.win));
				ri[k] = mp(mp(i, s2.P), mp(s2.R, s2.win));
				g[i + 1].pb(ss);
			}
		}
	}
	int T;
	cin >> T;
	for (int it = 1; it <= T; it++) {
		int n, r, p, s;            
		string ans;
		bool ok;
		sost a1;
		cin >> n >> r >> p >> s;
		ans = "IMPOSSIBLE";
		for (int i = 0; i < 3; i++) {
			pp ppx = mp(mp(n, p), mp(r, i));
			if (kek[ppx])
				ans = gen(mp(mp(n, p), mp(r, i)));
		 }
		cout << "Case #" << it << ": " << ans << endl;	
	}

    return 0;
}   