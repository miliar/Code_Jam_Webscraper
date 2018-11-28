#include <bits/stdc++.h>

using namespace std;

#define long long long

const int M = 1000100;
const int INF = 12345678;

int n;
int d;

long S0, As, Cs, Rs;
long M0, Am, Cm, Rm;

long s[M], m[M];
vector<int> g[M];
vector<int> e;
int tin[M], tout[M], tim;
int ts[4 * M], te[4 * M];

void ini() {
	for (int i = 0; i < 4 * n + 4; ++i)
		ts[i] = te[i] = -INF;
}

void upd(int *tree, int v, int l, int r, int le, int re, int val) {
	if (l == le && r == re) {
		tree[v] = max(tree[v], val);
		return;
	}
	int m = (l + r) / 2;
	if (le < m)
		upd(tree, 2 * v, l, m, le, min(re, m), val);
	if (m < re)
		upd(tree, 2 * v + 1, m, r, max(le, m), re, val);
	//tree[v] = max(tree[v], max(tree[2 * v + 1], tree[2 * v]));
}

int get(int *tree, int v, int l, int r, int pos) {
	if (l + 1 == r)
		return tree[v];
	int m = (l + r) / 2;
	if (pos < m)
		return max(tree[v], get(tree, 2 * v, l, m, pos));
	else
		return max(tree[v], get(tree, 2 * v + 1, m, r, pos));
}

void read() {
	cin >> n >> d;
	cin >> S0 >> As >> Cs >> Rs;
	cin >> M0 >> Am >> Cm >> Rm;

	s[0] = S0;
	m[0] = M0;
	for (int i = 1; i < n; ++i) {
		s[i] = (s[i - 1] * As + Cs) % Rs;
		m[i] = (m[i - 1] * Am + Cm) % Rm;
	}

	for (int i = 0; i < n; ++i)
		g[i].clear();

	for (int i = 1; i < n; ++i) {
		g[m[i] % i].push_back(i);
	}

	e.clear();
	tim = 0;
}

void dfs(int v) {
	e.push_back(v);
	tin[v] = tim;
	++tim;
	for (int to : g[v])
		dfs(to);
	tout[v] = tim;
}

void kill() {
	dfs(0);
	ini();
	//cerr << "\n";
	for (int i = 0; i < n; ++i) {
		int st = s[i];
		int se = s[i] + d;
		//cerr << i << ": " << tin[i] << " " << tout[i] << "\n";
		upd(ts, 1, 0, n, tin[i], tout[i], st);
		upd(te, 1, 0, n, tin[i], tout[i], -se);
		//cerr << "get " << get(ts, 1, 0, n, tin[i]) << " " << -get(te, 1, 0, n, tin[i]) << "\n";
	}

	vector<pair<int, int>> seg;
	//cerr << "\n";
	for (int i = 0; i < n; ++i) {
		int st = get(ts, 1, 0, n, tin[i]);
		int se = -get(te, 1, 0, n, tin[i]);
		if (st <= se) {
			seg.emplace_back(st, 1);
			seg.emplace_back(se + 1, -1);
		}
		//cerr << i << ": " << st << " - " << se << "\n";
	}


	sort(seg.begin(), seg.end());
	int ans = 0, cur = 0;
	for (int i = 0, j = 0; i < (int) seg.size(); ++i) {
		while (j < (int) seg.size() && seg[i].first == seg[j].first) {
			cur += seg[j].second;
			++j;
		}
		ans = max(ans, cur);
	}

	cout << ans << "\n";
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		read();
		kill();
		cerr << "Test #" << i << " done.\n";
	}
	return 0;
}