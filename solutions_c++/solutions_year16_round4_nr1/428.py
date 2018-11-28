#include <bits/stdc++.h>

const int MAXN = 10001;

int T, n, r, p, s, answer[23][MAXN], o[MAXN];

bool dfs(int h) {
	if (h == n) {
		int cnt[3];
		memset(cnt, 0, sizeof(cnt));
		for (int i = (1 << n); i < (1 << n + 1); i++) {
			cnt[answer[h][i]]++;
		}
		if (cnt[0] == r && cnt[1] == p && cnt[2] == s) {
			return true;
		}
		return false;
	}
	for (int i = (1 << h); i < (1 << h + 1); i++) {
		answer[h + 1][i << 1] = answer[h][i];
		answer[h + 1][i << 1 ^ 1] = (answer[h][i] + 2) % 3;
	}
	return dfs(h + 1);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int cs = 1; cs <= T; cs++) {
		printf("Case #%d: ", cs);
		scanf("%d%d%d%d", &n, &r, &p, &s);
		bool flag = false;
		std::string output;
		for (int i = 0; i < 3; i++) {
			answer[0][1] = i;
			if (dfs(0)) {
				for (int i = n, step = 2; i >= 1; i--, step <<= 1) {
					for (int j = (1 << n); j < (1 << n) + (1 << n); j += step) {
						int should = 2;
						for (int k = 0; k < step / 2; k++) {
							if ("RPS"[answer[n][j + k]] > "RPS"[answer[n][j + k + step / 2]]) {
								should = true;
								break;
							}
							if ("RPS"[answer[n][j + k]] < "RPS"[answer[n][j + k + step / 2]]) {
								should = false;
								break;
							}
						}
						if (should == 1) {
							for (int k = 0; k < step / 2; k++) {
								std::swap(answer[n][j + k], answer[n][j + step / 2 + k]);
							}
						}
					}
				}
				std::string tmp = "";
				for (int i = (1 << n); i < (1 << n + 1); i++) {
					tmp = tmp + "RPS"[answer[n][i]];
				}
				if (!flag) output = tmp;
				else output = std::min(output, tmp);
				flag = true;
			}
		}
		if (!flag) {
			puts("IMPOSSIBLE");
		} else std::cout << output << std::endl;
	}
	return 0;
}
