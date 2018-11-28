#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

vector<int64_t> par, sal;
vector<vector<int>> ch;
vector<char> is;

int n, sz;
int64_t d;

bool bysal(int a, int b) {
	return sal[a] < sal[b];
}

void add(int r, int64_t mon) {
	//E("add", r, mon);
	assert(!is[r]);
	is[r] = true;
	++sz;
	for (int c: ch[r]) if (mon <= sal[c] && sal[c] <= mon + d) {
		add(c, mon);
	}
}

void del(int l) {
	//E("del", l);
	assert(is[l]);
	for (int c: ch[l]) if (is[c]) {
		del(c);
	}
	is[l] = false;
	--sz;
}

void solve() {
	cin >> n >> d;
	par.resize(n);
	sal.resize(n);
	int64_t s0, as, cs, rs;
	cin >> s0 >> as >> cs >> rs;
	int64_t m0, am, cm, rm;
	cin >> m0 >> am >> cm >> rm;
	par[0] = m0;
	sal[0] = s0;
	for (int i = 1; i < n; ++i) {
		par[i] = (par[i-1] * am + cm) % rm;
		sal[i] = (sal[i-1] * as + cs) % rs;
	}
	par[0] = -1;
	ch.assign(n, vector<int>{});
	for (int i = 1; i < n; ++i) {
		par[i] %= i;
		ch[par[i]].emplace_back(i);
	}
	vector<int> ids(n);
	iota(all(ids), 0);
	sort(all(ids), bysal);
	for (int i = 0; i < n; ++i) {
		int v = ids[i];
		//E(v, par[v], sal[v]);
	}
	int best = 0;
	int pl = 0, pr = 0;
	is.assign(n, false);
	sz = 0;
	for (; pl < n; ++pl) {
		while (pr < n && sal[ids[pl]] + d >= sal[ids[pr]]) {
			int r = ids[pr];
			if (!is[r] && (r == 0 || is[par[r]])) {
				add(r, sal[ids[pl]]);
			}
			++pr;
		}
		best = max(best, sz);
		int l = ids[pl];
		if (is[l])
			del(l);
	}
	assert(sz == 0);
	cout << best;
}

int main() {
	int tcase;
	cin >> tcase;
	for (int t = 0; t < tcase; ++t) {
		cout << "Case #" << (t + 1) << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}
