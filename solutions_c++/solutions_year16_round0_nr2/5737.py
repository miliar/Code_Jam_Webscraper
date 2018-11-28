/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

const int MN = 101;

char s[MN];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, K = 1;
	scanf("%d", &T);
	while (T--) {
		scanf("%s", s);
		int n = strlen(s), i, cnt = 1;
		reverse(s, s + n);
		for (i = 0; i < n; ++i) if (s[i] == '-') break;

		printf("Case #%d: ", K);
		++K;
		if (i == n) {
			puts("0");
		} else {
			for (i = i + 1; i < n; ++i) {
				if (s[i] != s[i - 1]) ++cnt;
			}
			printf("%d\n", cnt);
		}
	}
	return 0;
}
