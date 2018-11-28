#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

bool chk(const string &s) {
	for(const auto &c : s) {
		if (c == '-')
			return false;
	}
	return true;
}

int solve(string &s) {
	int ret = 0;

	while(!chk(s)) {
		if (s[0] == '-') {
			for(auto &c : s) {
				if(c != '-') 
					break;
				c = '+';
			}
		}
		else {
			for(auto &c : s) {
				if(c != '+') 
					break;
				c = '-';
			}
		}

		ret++;
	}

	return ret;
}

int main() {

	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++) {
		string s;
		cin>>s;
		printf("Case #%d: ", tc);

		int ans = solve(s);
		printf("%d\n", ans);
	}

	return 0;
}