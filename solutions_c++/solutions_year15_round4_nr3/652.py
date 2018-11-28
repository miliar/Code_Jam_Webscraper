#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <unordered_set>
#include <sstream>
#include <algorithm>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++) {
		int n;
		cin >> n;
		string s;
		getline(cin, s);
		vector <vector <string> > lines;
		for (int i = 0; i < n; i++) {
			getline(cin, s);
			istringstream iss(s);
			vector <string> now;
			while (iss) {
				string cur;
				iss >> cur;
				now.push_back(cur);
			}
			now.pop_back();
			lines.push_back(now);
		}
		unordered_set <string> eng, fr;
		for (int i = 0; i < lines[0].size(); i++)
			eng.insert(lines[0][i]);
		for (int i = 0; i < lines[1].size(); i++)
			fr.insert(lines[1][i]);
		int common = 0;
		for (auto it : eng) {
			if (fr.count(it))
				common++;
		}
		int ans = 1e9;
		unordered_set <string> nfr, neng;
		for (int mask = 0; mask < (1 << (n - 2)); mask++) {
			nfr.clear();
			neng.clear();
			for (int i = 0; i < n - 2; i++) {
				int now = i + 2;
				if (mask & (1 << i)) {
					for (int j = 0; j < lines[now].size(); j++) {
						if (!eng.count(lines[now][j]))
							neng.insert(lines[now][j]);
					}
				}
				else {
					for (int j = 0; j < lines[now].size(); j++) {
						if (!fr.count(lines[now][j]))
							nfr.insert(lines[now][j]);
					}
				}
			}

			int cur = common;
			for (auto it : neng) {
				if (fr.count(it) || nfr.count(it))
					cur++;
			}
			for (auto it : nfr) {
				if (eng.count(it))
					cur++;
			}
			
			ans = min(ans, cur);
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}

	return 0;
}