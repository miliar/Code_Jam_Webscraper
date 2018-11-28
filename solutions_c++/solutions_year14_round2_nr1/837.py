#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#define MAXN (1 << 7)
using namespace std;

int n;
string str[MAXN];

int am[MAXN][MAXN];

inline void read() {
	cin >> n;
	for (int i=0; i < n; ++i)
		cin >> str[i];
}

inline string calcForm(string &s) {
	string ans; ans.clear();

	ans += s[0];
	for (int i=1; i < s.size(); ++i)
		if (s[i] != s[i-1])
			ans += s[i];

	return ans;
}

inline void solve() {
	string form = calcForm(str[0]);

	for (int i=0; i < n; ++i) {
		string curForm = calcForm(str[i]);

		if (curForm != form) {
			puts("Fegla Won");
			return;
		}
	}

	memset(am, 0, sizeof am);

	for (int i=0; i < n; ++i) {
		int id = 0;
		am[i][0] ++;
		for (int j=1; j < str[i].size(); ++j) {
			if (str[i][j-1] != str[i][j])
				id ++;
			am[i][id] ++;
		}
	}

	int ans = 0;
	for (int i=0; i < form.size(); ++i) {
		int add = -1;
		for (int tot=1; tot <= 100; ++tot) {
			int sum = 0;
			for (int j=0; j < n; ++j)
				sum += abs(am[j][i] - tot);

			if (sum < add || add == -1)
				add = sum;
		}

		ans += add;
	}

	cout << ans << endl;
}

int main() {
	int brt;
	scanf("%d", &brt);

	for (int test=0; test < brt; ++test) {
		printf("Case #%d: ", test+1);
		read();
		solve();
	}
	return 0;
}