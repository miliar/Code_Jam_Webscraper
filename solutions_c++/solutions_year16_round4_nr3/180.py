#include "bits/stdc++.h"
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define bend(_x) (_x).begin(), (_x).end()
#define szof(_x) ((int) (_x).size())
#define TASK_NAME ""

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int MAXN = 405;

int n, m;
int dsu[MAXN];
int imp[MAXN];
int sz[MAXN];
vector<pair<int*, int>> events;
int neig[MAXN];

int get_root(int v) {
 	return v == dsu[v] ? v : get_root(dsu[v]);
}

int unite(int a, int b) {
	//cerr << "dsu: " << a << " " << b << endl;
	a = get_root(a);
	b = get_root(b);
	//cerr << a << " " << imp[a] << " " << b << " " << imp[b] << endl;
 	if (sz[a] < sz[b]) {
 	 	swap(a, b);
 	}
 	events.puba({&dsu[b], dsu[b]});
	dsu[b] = a;
	int ret = 0;
	if (imp[a] != -1 && imp[b] != -1) {
	 	if (neig[imp[a]] != imp[b]) {
	 	 	ret = 1;
	 	}
	} else {
	 	events.puba({&imp[a], imp[a]});
	 	imp[a] = max(imp[a], imp[b]);
	}
	if (sz[a] == sz[b]) {
	 	events.puba({&sz[a], sz[a]});
	 	sz[a] += 1;
	}
	return ret;
}

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};


int get(int x, int y, int d) {
 	return (x * m + y) * 4 + d;
}

vector<char> now;

int rec(int x, int y) {
	if (x == n) {
	 	//int tmp = get_root(get(0, 1, 0));
	 	//cerr << imp[tmp] << endl;
	 	/*
	 	for (auto c: now) {
	 	 	cerr << c;
	 	}
	 	cerr << endl;*/
	 	return 1;
	}
 	{
 	 	int mem = szof(events);
 	 	if (!unite(get(x, y, 0), get(x, y, 1)) && !unite(get(x, y, 2), get(x, y, 3))) {
 	 	 	now.puba('\\');
 	 	 	//cerr << "add " << x << " " << y << " \\" << endl;
 	 	 	int nx = x;
 	 	 	int ny = y + 1;
 	 	 	if (ny == m) {
 	 	 	 	++nx;
 	 	 	 	ny = 0;
 	 	 	}
 	 	 	if (rec(nx, ny)) {
 	 	 	 	return 1;
 	 	 	}
 	 	 	now.pop_back();
 	 	 	//cerr << "erase " << x << " " << y << " \\" << endl;
 	 	}
 	
 	    while (szof(events) > mem) {
     	 	auto tmp = events.back();
     	 	*tmp.ff = tmp.ss;
     	 	events.pop_back();
     	}
 	}
 	
 	{
 	 	int mem = szof(events);
 	 	if (!unite(get(x, y, 0), get(x, y, 3)) && !unite(get(x, y, 1), get(x, y, 2))) {
 	 	 	now.puba('/');
 	 	 	//cerr << "add " << x << " " << y << " /" << endl;
 	 	 	int nx = x;
 	 	 	int ny = y + 1;
 	 	 	if (ny == m) {
 	 	 	 	++nx;
 	 	 	 	ny = 0;
 	 	 	}
 	 	 	if (rec(nx, ny)) {
 	 	 	 	return 1;
 	 	 	}
 	 	 	now.pop_back();
 	 	 	//cerr << "erase " << x << " " << y << " /" << endl;
 	 	}
 	
 	    while (szof(events) > mem) {
     	 	auto tmp = events.back();
     	 	*tmp.ff = tmp.ss;
     	 	events.pop_back();
     	}
 	}
 	
 	return 0;
}

int solve() {
 	scanf("%d%d", &n, &m);

 	//cerr << get(0, 1, 3) << endl;

 	for (int i = 0; i < n * m * 4; ++i) {
 	 	dsu[i] = i;
		imp[i] = -1;
		sz[i] = 1;
 	}

 	
 	for (int i = 0; i < (n + m); ++i) {
 	 	int a, b;
 	 	scanf("%d%d", &a, &b);
 	 	--a; --b;
 	 	neig[a] = b;
 	 	neig[b] = a;
 	}

 	for (int i = 0; i < m; ++i) {
 	 	imp[get(0, i, 0)] = i;
 	 	imp[get(n - 1, m - i - 1, 2)] = i + m + n;
 	}

 	for (int i = 0; i < n; ++i) {
 	 	imp[get(i, m - 1, 1)] = i + m;
 	 	imp[get(n - 1 - i, 0, 3)] = i + m + n + m;
 	}

 	for (int i = 0; i < n; ++i) {
 	 	for (int j = 0; j < m; ++j) {
 	 	 	for (int k = 0; k < 4; ++k) {
 	 	 	 	int nx = i + dx[k];
 	 	 	 	int ny = j + dy[k];
 	 	 	 	if (0 <= nx && nx < n && 0 <= ny && ny < m) {
 	 	 	 	 	unite(get(i, j, k), get(nx, ny, (k + 2) % 4));
 	 	 	 	}
 	 	 	}
 	 	}
 	}
 	
 	now.clear();
 	if (rec(0, 0)) {
 	 	for (int i = 0; i < n; ++i) {
 	 	 	for (int j = 0; j < m; ++j) {
 	 	 	 	//cerr << i * m + j << endl;
 	 	 	 	cout << now[i * m + j];
 	 	 	}
 	 	 	cout << "\n";
 	 	}
 	} else {
 	 	cout << "IMPOSSIBLE\n";
 	}
 	return 0;
}

int main() {
	//freopen(TASK_NAME ".in", "r", stdin);
	//freopen(TASK_NAME ".out", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; ++i) {
	 	cout << "Case #" << i + 1 << ": \n";
	 	solve();
	}

	return 0;
}