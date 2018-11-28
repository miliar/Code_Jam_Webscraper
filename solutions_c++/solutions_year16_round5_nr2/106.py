#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

const int nn = 14000;
typedef vector<int> vi;

int rand15() {
	return rand() & ((1<<15) - 1);
}

int rand30() {
	return (rand15() << 15) + rand15();
}

vector< int > g[128];
string sym;

vector<string> gen(int r) {
	if (g[r].size() == 0) {
		return vector<string>(1, string(1, sym[r-1]));
	} else {
		vector<int> code;

		vector< vector<string> > d;
		for (int i = 0; i < g[r].size(); ++i) {
			d.push_back(gen(g[r][i]));
			for (int j = 0; j < d[i][0].size(); ++j)
				code.push_back(i);
		}
		
		vector<string> res;
		for (int z = 0; z < nn; ++z) {
			random_shuffle(code.begin(), code.end());
			vector<string> dd;
			for (int i = 0; i < d.size(); ++i)
				dd.push_back(d[i][rand30() % d[i].size()]);
			vector<int> dc(dd.size());
			string rr;
			if (r != 0) rr += sym[r - 1];
			for (int i = 0; i < code.size(); ++i) {
				rr += dd[code[i]][dc[code[i]]++];
			}
			res.push_back(rr);
		}

		return res;
	}
}

void solve() {
	int n;
	cin >> n;
	for (int i = 0; i < 128; ++i) g[i].clear();

	for (int i = 1; i <= n; ++i) {
		int x; cin >> x;
		g[x].push_back(i);
	}
	cin >> sym;

	int m;
	cin >> m;

	vector<string> r = gen(0);

	vector<double> res(m);
	for (int i = 0; i < m; ++i) {
		string key; cin >> key;
		for (int j = 0; j < r.size(); ++j) { 
			bool ok = true;
			for (int st = 0; ok && st + key.length() <= n; ++st) {
				if (r[j].substr(st, key.length()) == key)
					ok = false;
			}
			if (ok)
				res[i] += 1.0 / r.size();
		}
	}


	static int test_id;
	cout << "Case #" << ++test_id << ":";
	cout << fixed;
	cout.precision(2);
	for (int i = 0; i < m; ++i) {
		cout << ' ' << fabs(1 - res[i]);
	}
	cout << endl;

	cerr << "Case #" << test_id << ' ' << clock() << "\n";
}

int main() {
	int t; cin >> t;
	while (t --> 0)
		solve();
	return 0;
}
