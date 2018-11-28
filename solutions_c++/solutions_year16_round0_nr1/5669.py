/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

void upd(bool have[], int x) {
	while (x) have[x % 10] = true, x /= 10;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	unordered_map<int, int> ans;
	int i, j;
	for (i = 1; i <= 1000000; ++i) {
		bool have[10] = {};
		for (j = 1; j <= 74; ++j) {
			upd(have, i * j);
			if (count(have, have + 10, true) == 10) {
				ans[i] = i * j;
				goto NXT;
			}
		}
		assert(false);
		NXT:;
	}

	int T, K = 1, n;
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		printf("Case #%d: ", K);
		++K;
		if (!n) printf("INSOMNIA\n");
		else printf("%d\n", ans[n]);
	}
	return 0;
}
