#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>
#include <sstream>


typedef long long ll;
typedef long double ld;

using namespace std;

const int INF = 2000;

struct edge {
	int x, c, f;
};

int cnt;

map<string, int> mm;

vector<edge> ed;

vector<int> eds[10000];

int was[10000];

int n;

void make_edge(int a, int b, int c) {
	edge x;
	x.x = b;
	x.c = c;
	x.f = 0;
	eds[a].push_back(ed.size());
	ed.push_back(x);
	x.x = a;
	x.c = 0;
	eds[b].push_back(ed.size());
	ed.push_back(x);
}



int dfs(int v, int fl) {
	if (v == 1)
		return fl;
	was[v] = 1;
	for (int i = 0; i < (int)eds[v].size(); ++i) {
		int u = ed[eds[v][i]].x;
		int c = ed[eds[v][i]].c;
		int f = ed[eds[v][i]].f;
		if (c > f && !was[u]) {
			int k = dfs(u, min(fl, c - f));
			if (k) {
				ed[eds[v][i]].f += k;
				ed[eds[v][i] ^ 1].f -= k;
				return k;
			}
		}
	}
	return 0;
}

int solve() {
	mm.clear();
	cnt = 2;
	eds[0].clear();
	eds[1].clear();
	ed.clear();
	cin >> n;
	for (int i = 0; i < n; ++i) {
		string ss;
		scanf(" ");
		getline(cin, ss);
		istringstream in(ss);
		string s;
		vector<int> vv;
		while (in >> s) {
			if (mm.find(s) != mm.end())
				vv.push_back(mm[s]);
			else
				eds[(cnt - 1) * 2].clear(), eds[(cnt - 1) * 2 + 1].clear(), make_edge((cnt - 1) * 2, (cnt - 1) * 2 + 1, 1), mm[s] = cnt++, vv.push_back(cnt - 1);
		}
		sort(vv.begin(), vv.end());
		vv.resize(unique(vv.begin(), vv.end()) - vv.begin());
		if (i == 0) {
			for (int x: vv)
				make_edge(0, (x - 1) * 2, INF);
		}
		else if (i == 1) {
			for (int x: vv)
				make_edge((x - 1) * 2 + 1, 1, INF);
		}
		else {
			for (int j1 = 0; j1 < (int)vv.size(); ++j1)
				for (int j2 = 0; j2 < (int)vv.size(); ++j2)
					make_edge((vv[j2] - 1) * 2 + 1, (vv[j1] - 1) * 2, INF);
		}
	}
	int ans = 0;

	while (true) {
		memset(was, 0, sizeof(was));
		int k = dfs(0, INF);
		if (!k)
			break;
		ans += k;
	}

	return ans;
}


int main() {
	int tt = 1;
	scanf("%d", &tt);
	for (int i = 0; i < tt; ++i) {
		int ans = solve();
		cout << "Case #" << i + 1 << ": " << ans << "\n";
	}
	return 0;
}


