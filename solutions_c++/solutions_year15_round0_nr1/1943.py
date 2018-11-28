#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1000;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T, N;
	char s[MAXN+1];
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &N);
		scanf("%s", s);
		int ans = 0;
		int got = 0;
		for (int i = 0; i <= N; i++) {
			int c = s[i] - '0';
			if (c == 0)
				continue;
			if (i > got) {
				ans += i - got;
				got += i - got;
			}
			got += c;
		}
		printf("Case #%d: %d\n", t, ans);
	}
}
