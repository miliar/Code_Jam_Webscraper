#include <bits/stdc++.h>
using namespace std;

int R, C, W;

int solve() {
	scanf("%d%d%d", &R, &C, &W);
	int r, c, w, ret = 0;
	r = R, c = C, w = W;
	for (int i = 0; i < r; i++) {
		c = C, w = W;
		while (w < c) {
			c -= w;
			ret++;
		}
	}
	if (w == c) {
		ret += r;
		ret += c - 1;
	}
	else ret += w;
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}

