#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define sz(v) int(v.size())
typedef long long ll;
typedef pair<int,int> pii;

const int MAXn = 4;
const int MAXm = 8;
string s[MAXm];
vector<int> server[MAXn];
int m, n;

int best, best_cnt;

void bt(int ind) {
	if(ind == m) {
		int cnt = 0;
		for(int i = 0; i < n; i++) {
			set<string> st;
			for(int j = 0; j < (int)server[i].size(); j++) {
				string &str = s[server[i][j]];
				for(int j = 0; j <= (int)str.size(); j++)
					st.insert(str.substr(0, j));
			}
			cnt += st.size();
		}
		if(best == cnt) {
			best_cnt++;
		} else if(best < cnt) {
			best = cnt;
			best_cnt = 1;
		}
		return;
	}
	for(int i = 0; i < n; i++) {
		server[i].push_back(ind);
		bt(ind + 1);
		server[i].pop_back();
	}
}

int main() {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cin >> m >> n;
		for(int i = 0; i < m; i++)
			cin >> s[i];
		best = -1;
		best_cnt = 0;
		bt(0);
		cout << "Case #" << t << ": " << best << " " << best_cnt << endl;
	}
	return 0;
}
