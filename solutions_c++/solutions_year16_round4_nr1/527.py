//A-small

#include <iostream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int T, n, p, r, s;
string ans;

string work(char a) {
	if (a == 'P')
		return "PR";
	if (a == 'S')
		return "PS";
	return "RS";
}

string makeLeast(string s) {
	if (s.size() == 1) {
		return s;
	}
	string l(s.begin(), s.begin() + s.size() / 2),
		   r(s.begin() + s.size() / 2, s.end());
	l = makeLeast(l);
	r = makeLeast(r);
	return min(l + r, r + l);
}

int main() {
	cin >> T;
	for (int _ = 1; _ <= T; ++_) {
		cin >> n >> r >> p >> s;
		ans = "IMPOSSIBLE";
		for (int i = 0; i < 3; ++i) {
			string tmp = "";
			bool flag = true;
			tmp = tmp + "PRS"[i];
			while ((int) tmp.size() < (1 << n)) {
				string nxt = "";
				for (auto cur : tmp) {
					nxt += work(cur);
				}
				map<char, int> cnt;
				for (auto cur : nxt) {
					++cnt[cur];
				}
				if (cnt['P'] > p || cnt['R'] > r || cnt['S'] > s) {
					flag = false;
					break;
				}
				tmp = nxt;
			}
			if (flag) {
				ans = tmp;
				break;
			}
		}
		if (ans != "IMPOSSIBLE")
			ans = makeLeast(ans);
		cout << "Case #" << _  << ": " << (ans) << endl;
	}
	return 0;
}
