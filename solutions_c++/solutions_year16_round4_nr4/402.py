#include <bits/stdc++.h>

const int MAXN = 20;

int T, n, pA[MAXN], pB[MAXN];
char a[MAXN][MAXN];
bool vY[MAXN];

int dfs(int x) {
	if (x == n + 1) {
		return true;
	}
	bool ret = true, flag = false;
	for (int i = 1; i <= n && ret; i++) {
		if (a[pA[x]][i] != '1' || vY[i]) {
			continue;
		}
		flag = true;
		vY[i] = true;
		if (!dfs(x + 1)) ret = false;
		vY[i] = false;
	}
	return ret && flag;
}

bool check() {
	for (int i = 1; i <= n; i++) pA[i] = i;
	do{
		std::fill(vY + 1, vY + n + 1, false);
		if (!dfs(1)) {
			return false;
		}
	}
	while (std::next_permutation(pA + 1, pA + n + 1));
	return true;
}

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);
	std::cin >> T;
	for (int cs = 1; cs <= T; cs++) {
		scanf("%d", &n);
		static std::vector<std::pair<int, int> > remain;
		remain.clear();
		for (int i = 1; i <= n; i++) {
			scanf("%s", a[i] + 1);
			for (int j = 1; j <= n; j++) {
				if (a[i][j] == '0') {
					remain.push_back(std::make_pair(i, j));
				}
			}
		}
		int answer = n * n;
		for (int i = 0; i < (1 << remain.size()); i++) {
			int cnt = 0;
			for (int j = 0; j < (remain.size()); j++) {
				if ((i >> j) & 1) {
					a[remain[j].first][remain[j].second] = '1';
					cnt++;
				}
			}
			if (check()) {
				answer = std::min(answer, cnt);
			}
			for (int j = 0; j < (remain.size()); j++) {
				if ((i >> j) & 1) {
					a[remain[j].first][remain[j].second] = '0';
				}
			}
		}
		printf("Case #%d: %d\n", cs, answer);
	}
	return 0;
}
