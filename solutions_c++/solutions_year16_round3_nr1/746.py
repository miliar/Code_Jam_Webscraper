/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

int a[30];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, K = 1;
	scanf("%d", &T);
	while (T--) {
		int n, i;
		scanf("%d", &n);

		vector<string> ans;

		for (i = 0; i < n; ++i) scanf("%d", a + i);

		while (true) {
			int sum = 0, cnt = 0;
			for (i = 0; i < n; ++i) sum += a[i];

			if (sum == 0) break;

			for (i = 0; i < n; ++i) if (a[i] == sum / 2) ++cnt;

			if (cnt == 0) {
				for (i = 0; i < n; ++i) {
					if (a[i]) {
						--a[i];
						ans.push_back(string(1, i + 'A'));
						break;
					}
				}
			} else if (cnt == 1) {
				for (i = 0; i < n; ++i) {
					if (a[i] == sum / 2) {
						--a[i];
						ans.push_back(string(1, i + 'A'));
						break;
					}
				}
			} else {
				if (sum % 2) {
					for (i = 0; i < n; ++i) {
						if (a[i] == 1) {
							--a[i];
							ans.push_back(string(1, i + 'A'));
							break;
						}
					}
				} else {
					ans.push_back("");
					for (i = 0; i < n; ++i) {
						if (a[i] == sum / 2) {
							--a[i];
							ans.back() += i + 'A';
						}
					}
				}
			}
		}

		printf("Case #%d:", K);
		++K;
		for (auto &x : ans) printf(" %s", x.c_str());
		puts("");
	}
	return 0;
}
