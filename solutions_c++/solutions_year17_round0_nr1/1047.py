#include <bits/stdc++.h>
using namespace std;

const int N = 1010;
char s[N];

bool AllPlus(char s[]) {
	for (int i = 0; s[i] != '\0'; i++) {
		if (s[i] == '-') return false;
	}
	return true;
}

int main() {
	int T; scanf("%d", &T);
	for (int kk = 1; kk <= T; kk++) {
		int k, ans = 0;
		scanf("%s%d", s, &k);
		int n = strlen(s);
		for (int i = 0; i + k <= n; i++) {
			if (s[i] == '-') {
				ans++;
				for (int j = 0; j < k; j++) {
					s[i+j] = s[i+j] == '-' ? '+' : '-';
				}
			}
		}
		printf("Case #%d: ", kk);
		if (AllPlus(s)) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}