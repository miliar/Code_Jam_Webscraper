#include <bits/stdc++.h>
using namespace std;

int TC, N;
bool possible = 0, failable = 0;
char g[16][16], newg[16][16];
vector<int> p;
bool used[16];

void rec(int x, int check) {
	if (x == N - 1) {
		bool avail = 0, invalid = 0;
		for (int i = 0; i < N; i++) if (newg[check][i] == 1 && !used[i]) avail = 1;
		for (int i = 0; i < N - 1; i++) {
			int act_id = i;
			if (i >= check) act_id++;
			//printf("a: %d %d\n", act_id, p[i]);
			if (!newg[act_id][p[i]]) invalid = 1;
		}
		//printf("%d %d\n", avail, invalid);
		if (!avail && !invalid) failable = 1;
		if (avail && !invalid) possible = 1;
		return;
	}
	for (int i = 0; i < N; i++) {
		if (used[i]) continue;
		used[i] = 1;
		p.push_back(i);
		rec(x + 1, check);
		p.pop_back();
		used[i] = 0;
	}
}

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) scanf("%s", &g[i]);
		int ans = 1000000000;
		for (int j = 0; j < (1 << (N * N)); j++) {
			memset(newg, 0, sizeof(newg));
			for (int k = 0; k < N * N; k++) if (j & (1 << k)) newg[k/N][k%N] = 1;
			bool fail = 0;
			int cost = 0;
			for (int k = 0; k < N; k++) {
				for (int l = 0; l < N; l++) {
					if (g[k][l] == '1' && !newg[k][l]) fail = 1;
					if (g[k][l] == '0' && newg[k][l]) cost++;
				}
			}
			if (fail) continue;
			for (int k = 0; k < N; k++) {
				possible = 0;
				failable = 0;
				rec(0, k);
				if (failable || !possible) {
					fail = 1;
					//printf("failed!\n");
					break;
				}
			}
			if (!fail) ans = min(cost, ans);
		}
		printf("Case #%d: %d\n", tc, ans);
	}
}
