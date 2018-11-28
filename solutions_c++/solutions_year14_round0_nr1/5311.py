#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define sz(a) (int)a.size()

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int used[17];
		memset(used, 0, sizeof used);

		for (int rep = 0; rep < 2; rep++) {
			int r;
			scanf("%d", &r);
			for (int i = 1; i <= 4; i++) {
				for (int j = 1; j <= 4; j++) {
					int x;
					scanf("%d", &x);
					if (r == i)
						used[x]++;
				}
			}
		}

		vector<int> ans;
		for (int i = 1; i <= 16; i++)
			if (used[i] == 2) ans.pb(i);

		printf("Case #%d: ", t);
		if (sz(ans) == 1) {
			printf("%d\n", ans[0]);
		} else
		if (sz(ans) > 1) {
			puts("Bad magician!");
		} else {
			puts("Volunteer cheated!");
		}
	}

	return 0;
}