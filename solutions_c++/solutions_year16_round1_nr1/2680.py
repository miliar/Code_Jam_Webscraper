#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

string solve(string s) {
	string cur = "";
	cur += s[0];
	for (int i = 1; i < s.size(); i++) {
		if (s[i] >= cur[0]) {
			string cur0 = cur;
			cur = "";
			cur += s[i];
			cur += cur0;
		}
		else cur += s[i];
	}
	return cur;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int ctest = 1; ctest <= t; ctest++) {
		char s[1005];
		scanf(" %s", s);

		printf("Case #%d: ", ctest);
		printf("%s\n", solve(string(s)).c_str());
	}
	return 0;
}
