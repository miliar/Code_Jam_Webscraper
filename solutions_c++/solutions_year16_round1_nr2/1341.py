# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <deque>
# include <vector>
# include <algorithm>
# include <set>

using namespace std;

int main() {
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int kase = 1; kase <= t; kase ++) {
		printf("Case #%d: ", kase);

		int n;
		scanf("%d", &n);

		int hash[2600];
		memset(hash, 0, sizeof(hash));
		set<int> s;
		s.clear();

		for (int i = 0; i < 2 * n - 1; i ++) {
			for (int j = 0; j < n; j ++) {
				int a;
				scanf("%d", &a);
				hash[a]++;

				s.insert(a);
			}
		}

		vector<int> ans;

		for (set<int>::iterator it = s.begin(); it != s.end(); it ++) {
			if (hash[*it] % 2 != 0) {
				ans.push_back(*it);
			}
		}

		sort(ans.begin(), ans.end());

		for (int i = 0; i < ans.size(); i ++) {
			printf("%d ", ans[i]);
		}

		printf("\n");
	}
}