#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool check(string str) {
	for (int i = 0; i < str.size(); ++i) {
		if (str[i] == '-') return 0;
	}
	return 1;
}

int time, ans = 0;
vector<int> v;

int main() {
//	freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	long long t, T, i, j, d, p, m, sum, ans;
	string s;
	cin >> T;

	for (t = 0; t < T; ++t) {
		ans = 0;
		cin >> s;
		while (!check(s)) {
			i = 0;
			while (s[0] == s[i]) i++;
			for (j = 0; j < i; ++j) {
				if (s[j] == '-') s[j] = '+'; else s[j] = '-';
			}
			ans++;
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}