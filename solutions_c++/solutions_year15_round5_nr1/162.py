#pragma comment (linker, "/STACK:128000000")
#include <iostream> 
#include <cstdio> 
#include <fstream>
#include <functional>
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <stack> 
#include <cmath> 
#include <algorithm> 
#include <cstring> 
#include <bitset> 
#include <ctime> 
#include <sstream>
#include <stack> 
#include <cassert> 
#include <list> 
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long li;
typedef long long i64;
typedef pair <int, int> pi;
typedef vector <int> vi;
typedef double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

//int timer = 0;
#define FILENAME ""

int main() {
    string s = FILENAME;
#ifdef YA
    //assert(!s.empty());
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //cerr<<FILENAME<<endl;
    //assert (s != "change me please");
    clock_t start = clock();
#else
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //freopen(FILENAME ".in", "r", stdin);
    //freopen(FILENAME ".out", "w", stdout); 
    cin.tie(0);
#endif
    cout.sync_with_stdio(0);
    cout.precision(10);
    cout << fixed;
    int t = 1;
    
	cin >> t;
    for (int i = 1; i <= t; ++i) {
        //++timer;
		cout << "Case #" << i << ": ";
        solve();
    }
#ifdef YA
    cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
    return 0;
}

int n, d;
vector <int> s, m;
vector <vector <int> > g;
vector <int> never;
vector <int> active;
//vector <int> unactive;
vector <int> added;
int ans = 0;
int cur = 0;

void recadd(int v) {
	if (!active[v]) {
		return;
	}
	added[v] = 1;
	++cur;
	for (int i = 0; i < g[v].size();++i) {
		int to = g[v][i];
		recadd(to);
	}
}

void add(int x) {
	if (never[x]) {
		return;
	}
	active[x] = 1;
	if (x == 0 || added[m[x]]) {
		recadd(x);
	}
}

void recdel(int v) {
	if (never[v]) {
		return;
	}
	
	if (added[v]) {
		--cur;
		added[v] = 0;
	}

	active[v] = 0;
	never[v] = 1;

	for (int i = 0; i < g[v].size(); ++i) {
		int to = g[v][i];
		recdel(to);
	}
}

void del(int x) {
	recdel(x);
}

void solve() {
	cin >> n >> d;
	
	ans = 0;
	cur = 0;

	never.clear();
	active.clear();
	added.clear();
	g.clear();

	g.resize(n);

	never.assign(n, 0);
	active.assign(n, 0);
	added.assign(n, 0);

	vector <int> cons[2];
	for (int i = 0; i < 2; ++i) {
		int st, A, C, R;
		cin >> st >> A >> C >> R;
		cons[i].push_back(st);
		for (int j = 1; j < n; ++j) {
			cons[i].push_back((cons[i].back() * A + C) % R);
		}
	}

	s = cons[0];
	m = cons[1];

	for (int i = 1; i < m.size(); ++i) {
		m[i] = m[i] % i;
		g[m[i]].push_back(i);
	}


	vector <pair <int, int> > order;

	for (int i = 0; i < n; ++i) {
		order.push_back(mp(s[i], i));
	}
	sort(order.begin(), order.end());

	int t = 0;
	while (t < n && order[t].first - order[0].first <= d) {
		add(order[t].second);
		++t;
	}
	ans = cur;

	int j = 0;
	while (t < n) {
		add(order[t].second);
		while (order[t].first - order[j].first > d) {
			del(order[j].second);
			++j;
		}
		ans = max(ans, cur);
		++t;
	}

	cout << ans << endl;
}