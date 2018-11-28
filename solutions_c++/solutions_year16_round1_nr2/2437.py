#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
#include <queue>
using namespace std;

#define NN 64
int t, N;
vector<vector<int>> Q;
vector<vector<int>> R;
vector<int> A;
int G[NN][NN];

bool solve(int d) {
	if (d == N*2) return true;
	int C[NN][NN];
	memcpy(C, G, sizeof(C));
	int r = d/2;
	// try to set row, column
	for (int j = 0; j < N; ++j) {
		if ((G[r][j] != 0 && R[d][j] != 0 && G[r][j] != R[d][j]) || (G[j][r] != 0 && R[d+1][j] != 0 && G[j][r] != R[d+1][j])) goto fail_1;
		if (R[d][j] != 0) {
			G[r][j] = R[d][j];
		}
		if (R[d+1][j] != 0) {
			G[j][r] = R[d+1][j];
		}
	}
	if (solve(d+2)) {
		if (R[d][0] == 0) {
			for (int j = 0; j < N; ++j) {
				A.push_back(G[r][j]);
			}
		}
		if (R[d+1][0] == 0) {
			for (int j = 0; j < N; ++j) {
				A.push_back(G[j][r]);
			}
		}
		return true;
	}
fail_1:
	memcpy(G, C, sizeof(C));
	// try to set column, row
	for (int j = 0; j < N; ++j) {
		if ((G[r][j] != 0 && R[d+1][j] != 0 && G[r][j] != R[d+1][j]) || (G[j][r] != 0 && R[d][j] != 0 && G[j][r] != R[d][j])) goto fail_2;
		if (R[d+1][j] != 0) {
			G[r][j] = R[d+1][j];
		}
		if (R[d][j] != 0) {
			G[j][r] = R[d][j];
		}
	}
	if (solve(d+2)) {
		if (R[d+1][0] == 0) {
			for (int j = 0; j < N; ++j) {
				A.push_back(G[r][j]);
			}
		}
		if (R[d][0] == 0) {
			for (int j = 0; j < N; ++j) {
				A.push_back(G[j][r]);
			}
		}
		return true;
	}
fail_2:
	memcpy(G, C, sizeof(C));
	return false;
}

int main() {
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%d", &N);
		Q.clear();
		Q.resize(2*N-1);
		R.clear();
		R.reserve(2*N);
		for (int i = 0; i < 2*N-1; ++i) {
			for (int j = 0; j < N; ++j) {
				int k;
				scanf("%d", &k);
				Q[i].push_back(k);
			}
		}
		for (int i = 0; i < N; ++i) {
			int mn = 9999;
			for (int j = 0; j < 2*N-1; ++j) {
				if (mn > Q[j][i]) {
					mn = Q[j][i];
				}
			}
			int cnt = 0;
			for (int j = 0; j < 2*N-1; ++j) {
				if (Q[j][i] == mn) {
					R.push_back(Q[j]);
					++cnt;
					fill(Q[j].begin(), Q[j].end(), 9999);
				}
			}
			if (cnt == 1) {
				R.emplace_back(N, 0);
			}
		}
#if 0
		for (int i = 0; i < int(R.size()); ++i) {
			for (int j = 0; j < N; ++j) {
				printf(" %d", R[i][j]);
			}
			printf("\n");
		}
#endif
		memset(G, 0, sizeof(G));
		A.clear();
		A.reserve(N);
		solve(0);
		printf("Case #%d:", ti+1);
		for (int j = 0; j < N; ++j) {
			printf(" %d", A[j]);
		}
		printf("\n");
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
