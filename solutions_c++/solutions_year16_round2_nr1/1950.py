#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

int cs[26];
string num[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

int getNum(int n) {
	int ret = 100000;
	int c[26] = { 0 };
	for(int i = 0; i < num[n].size(); i++) {
		c[num[n][i] - 'A']++;
	}
	for(int i = 0; i < 26; i++) {
		if(c[i]) ret = min(ret, cs[i] / c[i]);
	}
	for(int i = 0; i < 26; i++) {
		if(c[i]) cs[i] -= c[i] * ret;
	}
	return ret;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int loop = 1; loop <= T; loop++) {
		fill(cs, cs + 26, 0);
		string s;
		cin >> s;
		for(char c : s) {
			cs[c - 'A']++;
		}
		string ans;
		int o[10] = { 0, 2, 4, 6, 8, 1, 3, 5, 7, 9 };
		for(int i : o) {
			int n = getNum(i);
			ans += string(n, char('0' + i));
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << loop << ": " << ans << endl;
	}

}