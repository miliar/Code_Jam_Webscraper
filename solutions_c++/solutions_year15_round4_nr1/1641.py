#include <iostream>
#include <utility>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

int MV = 10;

int code(pair<int, int> a) {
	return (a.first) * MV + a.second;
}

int dsu_init(int n, vector<int> &p) {
	p.clear();
	srand(time(NULL));

	for (int i = 0; i < n; ++i) {
		p.push_back(i);
	}
	return 1;
}

int dsu_get (int v, vector<int> &p) {
	return (v == p[v]) ? v : (p[v] = dsu_get(p[v], p));
}

void dsu_unite (int a, int b, vector<int> &p) {
	a = dsu_get(a, p);
	b = dsu_get(b, p);
	if (rand() & 1)
		swap (a, b);
	if (a != b)
		p[a] = b;
}

int dsu_count(vector<int> &p) {
	int n = p.size();
	vector<int> vis(n, 0);
	int counter = 0;
	for (int i = 0; i < n; ++i) {
		if ( !vis[dsu_get(i, p)] ) {
			vis[dsu_get(i, p)] = 1;
			++counter;
		}
	}
	return counter;
}

string g[200];
vector< pair<int, int> > edges;

int main() {
	int T;
	cin >> T;
	for (int testnum = 1; testnum <= T; ++testnum) {
		int r, c;
		int ans = 0;
		int not_empty = 0;
		edges.clear();
		cin >> r >> c;
		MV = c;
		for (int i = 0; i < r; ++i)
		{
			cin >> g[i];
		}
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
//				cerr << "L " << i << " " << r << " " << j << " " << c << endl;
				pair<int, int> from(i, j), d;
				if (g[i][j] == '.') continue;
				++not_empty;
				if (g[i][j] == '<') d = make_pair(0, -1);
				if (g[i][j] == '>') d = make_pair(0, 1);
				if (g[i][j] == '^') d = make_pair(-1, 0);
				if (g[i][j] == 'v') d = make_pair(1, 0);
				pair<int, int> to(from);
				to.first += d.first;
				to.second += d.second;
				while ( (to.first >= 0) && (to.first < r) &&
						(to.second >= 0) && (to.second < c) &&
						(g[to.first][to.second] == '.') ) {
					to.first += d.first;
					to.second += d.second;
				}
				if ( (to.first >= 0) && (to.first < r) &&
					(to.second >= 0) && (to.second < c) ) {
					edges.push_back( make_pair( code(from), code(to) ) );
//					cerr << "(" << from.first << " ; " << from.second << ")->(" << to.first << " ; " << to.second << ")\n";
				}

			}
		vector<int> p;
		dsu_init(r * c, p);
//cerr << "OK - " << edges.size() << "\n";
		for (int i = 0; i < edges.size(); ++i) {
			if (dsu_get(edges[i].first, p) == dsu_get(edges[i].second, p)) {
				--ans;
//cerr << "LAL\n";
			}
			else {
				dsu_unite(edges[i].first, edges[i].second, p);
//cerr << "NAL " << edges[i].first << " - " << edges[i].second << "\n";
			}
		}

		for (int i = 0; i < r; ++i) {
			int counter = 0;
			for (int j = 0; j < c; ++j) {
				if (g[i][j] != '.') {
					++counter;
				}
			}
			if (counter != 1) continue;
			int j = 0;
			while (g[i][j] == '.') ++j;
			counter = 0;
			for (int h = 0; h < r; ++h) {
				if (g[h][j] != '.') {
					++counter;
				}
			}
			if (counter == 1) {
				ans = -1e9;
				break;
			}
		}

//cerr << "C = " << dsu_count(p);
		if (ans != -1e9) ans += dsu_count(p) - r * c + not_empty;
		if (!not_empty) ans = 0;

		cout << "Case #" << testnum << ": ";
		if (ans == -1e9) cout << "IMPOSSIBLE\n";
		else cout << ans << "\n";
	}
	return 0;
}
