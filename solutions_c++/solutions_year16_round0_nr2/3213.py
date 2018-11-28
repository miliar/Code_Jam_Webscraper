#include <bits/stdc++.h>

using namespace std;

int T;
char S[110];
char c[2] = {'-', '+'};

int main() {
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		scanf("%s", S);
		printf("Case #%d: ", tt);
		int t = 0;
		int ans = 0;
		for (int i = strlen(S) - 1; i >= 0; i--) {
			if (c[t] == S[i]) {
				ans++;
				t = 1 - t;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
