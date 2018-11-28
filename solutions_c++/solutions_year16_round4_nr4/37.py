#include <bits/stdc++.h>
using namespace std;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;
typedef set<string> ss;
typedef set<pii> spii;

const double pi = 2.0*acos(0.0);

int CASES;

void init() {
	assert(scanf("%d", &CASES) == 1);
}

int dprintf(const char *err, ...) { 
	if (debug) {
		va_list pvar;
		va_start(pvar, err);
		return vfprintf(stderr, err, pvar);
	}
	return 0;
}

int N;
string mat[100];

ll dfs(int u, ll seen) {
	if (seen & (1LL<<u)) return seen;
	seen |= 1LL<<u;
	if (u < N)
		for (int i = 0; i < N; ++i)
			if (mat[u][i] == '1') seen = dfs(i+N, seen);
	if (u >= N)
		for (int i = 0; i < N; ++i)
			if (mat[i][u-N] == '1') seen = dfs(i, seen);
	return seen;
}

int hw(ll x) { return x ? (x&1)+hw(x/2) : 0; }

const int oo = 1<<20;

vpii comp;

map<int, int> best[26][26][26][26];

int Best(int v1, int v2, int f1, int f2, int rem) {
	dprintf("go %d %d %d %d %d\n", v1, v2, f1, f2, rem);
	if (v1 == v2 && v1 > 0) return v1*v2 + Best(0, 0, f1, f2, rem);
	if (!rem && !f1 && !f2) {
		return v1 == v2 && v1 == 0 ? 0 : oo;
	}
	int &res = best[v1][v2][f1][f2][rem];
	if (res == 0) {
		res = oo;
		if (f1 > 0 && f2 > 0)
			res = min(res, 1+Best(v1, v2, f1-1, f2-1, rem));
		if (f1 > 0 && v2 > v1)
			res = min(res, Best(v1+1, v2, f1-1, f2, rem));
		if (f2 > 0 && v1 > v2)
			res = min(res, Best(v1, v2+1, f1, f2-1, rem));
		for (int i = 0; i < comp.size(); ++i)
			if (rem & (1<<i)) {
				res = min(res, Best(v1 + comp[i].first, v2 + comp[i].second, f1, f2,
									rem & ~(1<<i)));
			}
		dprintf("opt v1 %d v2 %d f1 %d f2 %d rem %d = %d\n",
				v1, v2, f1, f2, rem, res);
		++res;
	}
	return res-1;
}

void solve(int P) {
	cin >> N;
	int existing = 0;
	for (int i = 0; i < N; ++i) {
		cin >> mat[i];
		for (int j = 0; j < N; ++j)
			existing += mat[i][j] == '1';
	}
	ll all = 0;
	int free1 = 0, free2 = 0;
	comp.clear();
	dprintf("\n");
	dprintf("find comps N %d\n", N);
	for (int i = 0; i < 2*N; ++i)
		if (!(all & (1LL<<i))) {
			dprintf("start %d\n", i);
			ll c = dfs(i, 0);
			all |= c;
			int w = hw(c);
			dprintf("comp %lld %lld wt %d\n", c >> N, c - (c>>N)<<N, w);
			if (w > 1) {
				comp.push_back(pii(hw(c >> N), w - hw(c>>N)));
				dprintf("  %d %d\n", comp.back().first, comp.back().second);
			}
			else if (i < N)
				++free2;
			else
				++free1;
		}
	dprintf("%lld %lld\n", all, (1LL<<(2*N))-1);
	assert(all == (1LL<<(2*N))-1);
	int s1 = 0, s2 = 0;
	for (int i = 0; i < comp.size(); ++i) {
		s1 += comp[i].first;
		s2 += comp[i].first;
	}
	for (int i = 0; i < 26; ++i)
		for (int j= 0; j < 26; ++j)
			for (int k = 0; k < 26; ++k)
				for (int l = 0; l < 26; ++l)
					best[i][j][k][l].clear();
	dprintf("find opt\n");
	int opt = Best(0, 0, free1, free2, (1<<comp.size())-1);
	printf("Case #%d: %d\n", P, opt-existing);
}

int main(void) {
	init();
	for (int i = 1; i <= CASES; ++i) {
		solve(i);
		fflush(stdout);
		fflush(stderr);
	}
	return 0;
}
