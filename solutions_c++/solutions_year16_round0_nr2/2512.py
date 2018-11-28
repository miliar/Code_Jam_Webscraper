#include <bits/stdc++.h>

const int MAXN = 10001;

int T, n;
char s[MAXN];

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	std::cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		printf("Case #%d: ", cs);
		scanf("%s", s + 1);
		int length = strlen(s + 1), flag = 0, answer = 0;
		for (int i = length; i >= 1; i--) {
			if ((s[i] == '-') ^ flag) {
				flag ^= 1;
				answer++;
			}
		}
		printf("%d\n", answer);
	}
	return 0;
}
