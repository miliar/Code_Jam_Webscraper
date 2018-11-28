#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

int t, i, l, ans, j;
string s;

int main() {
	//freopen("./b.in", "r", stdin);
	//freopen("./b.out", "w", stdout);
	scanf("%d", &t);
	for (i = 1; i <= t; ++i) {
		cin >> s;
		l = s.length();
		ans = 1;
		for (j = 0; j < l - 1; j++)
			if (((s[j] == '-') && (s[j + 1] == '+'))
				|| ((s[j] == '+') && (s[j + 1] == '-')))
				ans++;
		if (s[l - 1] == '+') ans--;
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
