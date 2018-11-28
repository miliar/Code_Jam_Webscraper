#include <bits/stdc++.h>
using namespace std;

int T;
char s[1024];

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		scanf("%s", s + 1);
		int len = strlen(s + 1);
		int cnt = 0;
		int ans = 0;
		for (int i = 1; i <= len; ++i) {
			if (i == 0 || s[i] != s[i - 1])
				cnt ++;
			if (s[i] == '-')
				ans = cnt;
		}
		printf("%d\n", ans);
	}
	return 0;
}