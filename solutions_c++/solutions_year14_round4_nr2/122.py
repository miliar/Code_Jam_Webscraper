#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <cmath>
#include <iostream>
using namespace std;
const int maxn = 1000;
int n;
int a[maxn];

void init() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	return;
}

int calc() {
	int rank[maxn];
	memset(rank, 0, sizeof(rank));
	int pos[maxn];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (a[j] >= a[i]) {
				continue;
			}
			rank[i]++;
		}
		pos[rank[i]] = i;
	}

	int inv[maxn];
	memset(inv, 0, sizeof(inv));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (rank[j] >= rank[i]) {
				continue;
			}
			inv[rank[i]]++;
		}
	}

	int best[maxn][maxn];
	memset(best, 0xff, sizeof(best));
	best[0][0] = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			int rem = i - j;
			if (best[j + 1][rem] == -1) {
				best[j + 1][rem] = best[j][rem] + abs(pos[j + rem] - inv[j + rem]);
			}
			best[j + 1][rem] = min(best[j + 1][rem], best[j][rem] + abs(pos[j + rem] - inv[j + rem]));

			if (best[j][rem + 1] == -1) {
				best[j][rem + 1] = best[j][rem] + abs(pos[j + rem] - inv[j + rem] - n + rem + j + 1);
			}
			best[j][rem + 1] = min(best[j][rem + 1], best[j][rem] + abs(pos[j + rem] - inv[j + rem] - n + rem + j + 1));
		}
	}

	int ans = -1;
	for (int i = 0; i <= n; i++) {
		if (ans == -1) {
			ans = best[i][n - i];
		}
		ans = min(ans, best[i][n-i]);
	}
	return ans;
}

int main() {
	int tcase;
	scanf("%d", &tcase);
	for (int i = 1; i <= tcase; i++) {
		init();
		printf("Case #%d: %d\n", i, calc());
	}
	return 0;
}