#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <queue>
#include <cmath>

using namespace std;

const string order = "RSP";

void change_order(string &str) {
	int len = 1;
	int str_len = str.size();
	while (len < str_len) {
		int idx1 = 0;
		int idx2 = len;

		while (idx2 < str_len) {
			if (str.substr(idx1, len) > str.substr(idx2, len)) {
				for (int i = 0; i < len; i++) {
					swap(str[idx1 + i], str[idx2 + i]);
				}
			}
			idx1 = idx2 + len;
			idx2 = idx1 + len;
		}

		len *= 2;
	}

}

void dfs(string &str, int pos, char hand) {
	str[pos] = hand;

	if (pos * 2 + 1 < str.size()) {
		char h1, h2;
		switch (hand) {
			case 'R': h1 = 'R'; h2 = 'S'; break;
			case 'P': h1 = 'P'; h2 = 'R'; break;
			case 'S': h1 = 'P'; h2 = 'S'; break;
			default: break;
		}

		dfs(str, pos * 2, h1);
		dfs(str, pos * 2 + 1, h2);
	}
}

string solve(int n, int r, int p, int s) {
	for (int i = 0; i < order.size(); i++) {
		string ret(pow(2, n + 1), '?');
		dfs(ret, 1, order[i]);
		ret = ret.substr(pow(2, n));
		if (count(ret.begin(), ret.end(), 'R') == r &&
		    count(ret.begin(), ret.end(), 'S') == s &&
		    count(ret.begin(), ret.end(), 'P') == p
		) {
			// cout << ret << endl;
			change_order(ret);
			// cout << ret << endl;
			return ret;
		}
	}

	return "IMPOSSIBLE";
}

int main() {
	int t, n, r, p, s;
	cin >> t;
	vector<string> ans(t);

	for (int i = 0; i < t; i++) {
		cin >> n >> r >> p >> s;
		ans[i] = solve(n, r, p, s);
	}

	for (int i = 0; i < t; i++) {
		printf("Case #%d: %s\n", i + 1, ans[i].c_str());
	}
	return 0;
}
