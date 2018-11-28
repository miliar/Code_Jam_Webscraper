#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;


string calc(int n, string s) {
	for(int i = 0; i < n; i++) {
		string ss;
		for(int j = 0; j < s.size(); j++) {
			if(s[j] == 'R') ss += "RS";
			else if(s[j] == 'P') ss += "PR";
			else ss += "PS";
		}
		s = ss;
	}

	for(int i = 0; i < n; i++) {
		int num = 1 << i;
		for(int j = 0; j < s.size() / num / 2; j++) {
			string s1 = s.substr(2 * num*j, num), s2 = s.substr(2 * num * j + num, num);
			if(s1 > s2) {
				for(int k = 0; k < num; k++) {
					swap(s[2 * num * j + k], s[2 * num * j + num + k]);
				}
			}
		}
	}
	return s;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int loop = 1; loop <= T; loop++) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;

		string ss[3] = { "R", "P", "S" };

		string ans = "Z";
		for(int i = 0; i < 3; i++) {
			string res = calc(n, ss[i]);
			if(count(res.begin(), res.end(), 'R') != r) continue;
			if(count(res.begin(), res.end(), 'P') != p) continue;
			if(count(res.begin(), res.end(), 'S') != s) continue;
			//cout << res << endl;
			ans = min(ans, res);
		}

		cout << "Case #" << loop << ": ";
		if(ans == "Z") {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			cout << ans << endl;
		}

	}
}