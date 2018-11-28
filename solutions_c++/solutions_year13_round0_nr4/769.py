#include <cstdio>
#include <algorithm>

int lex_soln[22];
int k, n;
int cur[202];
int chests[22][42];
int nkeys[22];
int required[22];

bool cache[1 << 22];

bool soln(int opened, int num_opened) {
	if (cache[opened]) return false;

	if (num_opened == n) {
		return true;
	} else {
		for (int i = 0; i < n; i++) {
			if (!(opened & (1 << i)) && cur[required[i]] > 0) {
				cur[required[i]]--;
				for (int j = 0; j < nkeys[i]; j++) {
					cur[chests[i][j]]++;
				}

				if (soln(opened | (1 << i), num_opened + 1)) {
					lex_soln[num_opened] = i + 1;
					return true;
				}

				cur[required[i]]++;
				for (int j = 0; j < nkeys[i]; j++) {
					cur[chests[i][j]]--;
				}
			}
		}

		cache[opened] = true;
		return false;
	}
}


void solve(int t) {
	scanf("%d %d", &k, &n);

	std::fill(cur, cur + 202, 0);
	std::fill(cache, cache + (1 << 22), false);

	for (int i = 0; i < k; i++) {
		int x; scanf("%d", &x);
		cur[x]++;
	}

	for (int i = 0; i < n; i++) {
		scanf("%d %d", &required[i], &nkeys[i]);

		std::fill(chests[i], chests[i] + 42, 0);
		for (int j = 0; j < nkeys[i]; j++) {
			scanf("%d", &chests[i][j]);
		}
	}

	printf("Case #%d: ", t);
	if (soln(0, 0)) {
		for (int i = 0; i < n; i++) {
			if (i) printf(" ");
			printf("%d", lex_soln[i]);
		}
		printf("\n");
	} else printf("IMPOSSIBLE\n");

/*
	for (int i = 0; i < n; i++) {
		printf("Chest %d\n", i);
		printf("Requires: key %d\n", required[i]);
		printf("Contains: %d keys\n", nkeys[i]);
		for (int j = 0; j < nkeys[i]; j++)
			if (chests[i][j]) printf("key %d\n", chests[i][j]);
	}*/
}

int main() {
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) solve(i);
}