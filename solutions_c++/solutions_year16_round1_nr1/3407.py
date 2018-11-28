#include <bits/stdc++.h>

using namespace std;

#ifdef LOCAL
#include "delete_this.hpp"
#define t(...) debug(#__VA_ARGS__, __VA_ARGS__);
#else
#define t(...)
#endif

void huehue() {
	string s;
	cin >> s;
	int sz = s.size();
	string ans = "";
	ans += s[0];
	char lst = s[0];
	for (int i = 1; i <= sz - 1; ++i) {
		if (s[i] >= ans[0]) {
			ans = s[i] + ans;
		} else {
			ans += s[i];
		}
	}
	cout << ans << "\n";
}

int main() {
	int ntc;
	scanf(" %d", &ntc);
	for (int itc = 0; itc <= ntc - 1; ++itc) {
		printf("Case #%d: ", itc + 1);
		huehue();
	}
	return 0;
}
