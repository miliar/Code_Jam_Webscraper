#include <cstdio>
#include <vector>

using namespace std;

int calc(int v, vector<int>& coins) {
	// c=1 固定

	sort(coins.begin(), coins.end());

	// 作れない
	vector<int> notmake;

	int ans = 0;
	for (int i = 1; i <= v; i++) {
		if (i < coins[0]) {
			notmake.push_back(i);
			coins.push_back(i);
			sort(coins.begin(), coins.end());
			continue;
		}

		bool found = false;
		for (int j = 0; j < (1 << coins.size()); j++) {
			int x = 0;
			for (int k = 0; k < coins.size(); k++) {
				if (j & (1 << k)) {
					x += coins[k];
				}
			}

			if (x == i) { // 作ることができる
				found = true;
				break;
			}
		}

		if (!found) { // 作れない
			notmake.push_back(i);
			coins.push_back(i);
			sort(coins.begin(), coins.end());

		}
	}

	return notmake.size();
}

int main() {
	int ncases;
	scanf("%d", &ncases);

	for (int cc = 0; cc < ncases; cc++) {
		int C, D, V;
		scanf("%d %d %d", &C, &D, &V);

		vector<int> coins(D);
		for (int i = 0; i < D; i++)
			scanf("%d", &coins[i]);

		printf("Case #%d: %d\n", cc+1, calc(V, coins));


	}
}
