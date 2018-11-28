#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
void PR(vi &v) { trav(x, v) cout << x << ' '; cout << endl; }

struct UF {
	vi v;
	UF(int n) : v(n, -1) {}
	int find(int x) { return v[x] < 0 ? x : v[x] = find(v[x]); }
	void join(int a, int b) {
		a = find(a);
		b = find(b);
		if (a == b) return;
		if (-v[a] < -v[b]) swap(a, b);
		v[a] += v[b];
		v[b] = a;
	}
	bool same(int a, int b) { return find(a) == find(b); }
};

struct St {
	vector<pii> comps;
	int m, fullm, sum;
	map<ll, int> mem;
	int rec(int used, int l, int r) {
		if (l == 0 && used == fullm) return 0;
		if (l && l == r) return rec(used, 0, 0) + l*l;

		ll mind = (ll)used * (64 * 64) + l * 64 + r;
		auto it = mem.find(mind);
		if (it != mem.end()) return it->second;

		int ret = 1 << 29;
		if (l > r) {
			ret = rec(used, 0, 0) + l*l;
		}

		rep(i,0,m) {
			if (used & (1 << i)) continue;
			if (i && comps[i] == comps[i-1] && !(used & (1 << (i-1)))) continue;
			ret = min(ret, rec(used | (1 << i), l + comps[i].first, r + comps[i].second));
		}

		mem[mind] = ret;
		return ret;
	}
};

St parse() {
	int N;
	cin >> N;
	vector<string> board(N);
	rep(i,0,N) cin >> board[i];
	int sum = 0;
	rep(i,0,N) rep(j,0,N) sum += (board[i][j] == '1');
	UF uf(N*2);
	rep(i,0,N) rep(j,0,N) if (board[i][j] == '1') {
		uf.join(i, j+N);
	}

	vi seen(N);
	vector<pii> comps;
	rep(i,0,N) {
		if (seen[i]) continue;
		int l = 0, r = 0;
		rep(j,0,N) if (uf.same(i,j+N)) r++;
		rep(j,0,N) if (uf.same(i,j)) l++, seen[j] = 1;
// cerr << l << ' ' << r << endl;
		comps.emplace_back(l,r);
	}

	sort(all(comps));
	St st;
	st.sum = sum;
	st.comps = comps;
	st.m = sz(comps);
	st.fullm = (1 << st.m) -1;
	return st;
}

int solve(St& st) {
	int res = st.rec(0, 0, 0);
	res -= st.sum;
	return res;
}

int main() {
	cin.sync_with_stdio(false);
	cin.tie(0);
	int N;
	cin >> N;
	vector<St> sts(N);
	rep(i,0,N) sts[i] = parse();
	vi sols(N);
#pragma omp parallel for
	rep(i,0,N) sols[i] = solve(sts[i]);
	rep(i,0,N) {
		cout << "Case #" << i+1 << ": " << sols[i] << endl;
	}
}
