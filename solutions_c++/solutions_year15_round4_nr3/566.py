#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <bitset>

using namespace std;

const int INF = ~0u >> 1;

int n, ans, cnt;
map<string, int> num;
vector< vector<string> > sten;
bitset<1200> bit[300];
int belong[300];

vector<string> get_sten() {
	string s;
	getline(cin, s);
	istringstream _s(s);
	vector<string> res;
	while (_s >> s) {
		res.push_back(s);
		if (!num[s]) {
			num[s] = ++cnt;
		}
		//cout << s << ",";
	}
	//cout << endl;
	return res;
}

void dfs(int dep) {
	if (dep < n) {
		if (dep == 0) {
			belong[dep] = 0;
			dfs(dep + 1);
			return ;
		}
		if (dep == 1) {
			belong[dep] = 1;
			dfs(dep + 1);
			return ;
		}
		dfs(dep + 1);
		belong[dep] = 1;
		dfs(dep + 1);
		belong[dep] = 0;
	} else {
		bitset<1200> ss[2], res;
		for (int i = 0; i < n; ++i) {
			ss[belong[i]] |= bit[i];
		}
		int tmp = 0;
		res = ss[0] & ss[1];
		for (int i = 0; i < 1200; ++i) {
			tmp += res[i];
			if (tmp > ans) {
				return;
			}
		}
		ans = min(ans, tmp);
	}
}

bitset<1200> make_bit(vector<int> a) {
	bitset<1200> res;
	for (auto s: a) {
		res[num[s] - 1] = 1;
	}
	return res;
}

int main() {
	int T, t;
	cin >> T;
	for (t = 1; t <= T; ++t) {
		cnt = 0;
		sten.clear();
		num.clear();
		cin >> n;
		string s;
		getline(cin, s);
		for (int i = 0; i < n; ++i) {
			sten.push_back(get_sten());
		}
		for (int i = 0; i < n; ++i) {
			bit[i] = make_bit(sten[i]);
		}
		ans = INF;
		dfs(0);
		printf("Case #%d: %d\n", t, ans);
		cerr << t << " done..." << endl;
	}
	return 0;
}
