#include <bits/stdc++.h>

typedef long long LLONG;

inline void execState(int& state, LLONG value) {
	for (; value; value /= 10) {
		int v = value % 10;
		state |= 1 << v;
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t, n, tt = 0;
	scanf("%d", &t);
	for (; t--;) {
		char str[111];
		scanf("%s", str);
		int differ = 0;
		char lastchar = str[0];
		for (int i = 1; str[i]; ++i) {
			if (str[i] != str[i - 1]) ++differ;
			lastchar = str[i];
		}
		printf("Case #%d: ", ++tt);
		if (!differ) {
			printf("%d\n", '-' == lastchar);
		} else {
			++differ;
			differ -= '+' == lastchar;
			printf("%d\n", differ);
		}
	}
	return 0;
}
