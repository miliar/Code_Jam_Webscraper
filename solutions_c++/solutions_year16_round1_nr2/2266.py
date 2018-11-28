#include <stdio.h>
#include <vector>
using namespace std;

int T;
int N, len;
int map[51][51];
vector< vector<int> > list;
bool chk[201];
bool fin;
vector<int> res;

void Solve(int pos, bool dir, bool pdir, int panelty) {
	int i, j;
	if (pos == N) {
		fin = true;
		return;
	}
	for (i = 0; i < len; i++) {
		if (!chk[i]) {
			bool err = false;
			if (!dir) {
				for (j = 0; j < pos; j++) {
					if (map[pos][j] != list[i][j]) {
						if (panelty == j && pdir) continue;
						err = true;
					}
				}
				if (!err) {
					for (j = pos; j < N; j++) map[pos][j] = list[i][j];
					if (panelty >= 0 && pdir) map[pos][panelty] = list[i][panelty];
					chk[i] = true;
					Solve(pos, !dir, pdir, panelty);
					chk[i] = false;
					if (fin) return;
					for (j = pos; j < N; j++) map[pos][j] = 0;
					if (panelty >= 0 && pdir) map[pos][panelty] = 0;
				}
			}
			else {
				for (j = 0; j <= pos; j++) {
					if (map[j][pos] != list[i][j]) {
						if (panelty == j && !pdir) continue;
						err = true;
					}
				}
				if (!err) {
					for (j = pos + 1; j < N; j++) map[j][pos] = list[i][j];
					if (panelty >= 0 && !pdir) map[panelty][pos] = list[i][panelty];
					chk[i] = true;
					Solve(pos + 1, !dir, pdir, panelty);
					chk[i] = false;
					if (fin) return;
					for (j = pos + 1; j < N; j++) map[j][pos] = 0;
					if (panelty >= 0 && !pdir) map[panelty][pos] = 0;
				}
			}
		}
	}
	if (panelty < 0) {
		if (!dir) Solve(pos, !dir, dir, pos);
		else Solve(pos + 1, !dir, dir, pos);
		if (fin) return;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, i, j, k;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d", &N);

		list.clear();
		list.resize(N * 2 - 1);
		len = list.size();
		for (i = 0; i < len; i++) {
			list[i].resize(N);
			for (j = 0; j < N; j++)
				scanf("%d", &list[i][j]);
		}
		for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++)
				map[i][j] = 0;
		}
		for (i = 0; i < len; i++) chk[i] = false;
		fin = false;
		res.clear();

		Solve(0, false, false, -1);

		for (i = 0; i < len; i++) chk[i] = false;
		for (i = 0; i < N; i++) {
			bool found = false;
			for (j = 0; j < len; j++) {
				if (!chk[j]) {
					bool err = false;
					for (k = 0; k < N; k++) {
						if (list[j][k] != map[i][k]) {
							err = true; break;
						}
					}
					if (!err) {
						chk[j] = true;
						found = true;
						break;
					}
				}
			}
			if (!found) {
				for (j = 0; j < N; j++) res.push_back(map[i][j]);
				break;
			}
		}
		for (i = 0; i < N; i++) {
			bool found = false;
			for (j = 0; j < len; j++) {
				if (!chk[j]) {
					bool err = false;
					for (k = 0; k < N; k++) {
						if (list[j][k] != map[k][i]) {
							err = true; break;
						}
					}
					if (!err) {
						chk[j] = true;
						found = true;
						break;
					}
				}
			}
			if (!found) {
				for (j = 0; j < N; j++) res.push_back(map[j][i]);
				break;
			}
		}
		printf("Case #%d: ", t);
		for (i = 0; i < N; i++) printf("%d ", res[i]);
		printf("\n");
	}
	return 0;
}
