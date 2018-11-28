#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <tuple>
using namespace std;
typedef long long LL;
typedef function<int(int)> VALF;

#define pb push_back
#define mt make_tuple
#define SZ(V) ((int)((V).size()))
int N;

char dat[32][32];
bool used_p[32], used_m[32];
int p_count, m_count;
void dfs_p(int);
void dfs_m(int m) {
	if (used_m[m]) return;
	used_m[m] = true;
	m_count++;
	for (int p = 0; p < N; p++) {
		if (dat[p][m] == '1') {
			dfs_p(p);
		}
	}
}
void dfs_p(int p) {
	if (used_p[p]) return;
	used_p[p] = true;
	p_count++;
	for (int m = 0; m < N; m++) {
		if (dat[p][m] == '1') {
			dfs_m(m);
		}
	}
}
void update(int &dyn, int val) {
	if (dyn == -1) dyn = val;
	else {
		dyn = min(dyn, val);
	}
}
vector<pair<int, int> > pm;
int main() {
	//freopen("input.txt", "r", stdin);
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int T;
	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++) {
		pm.clear();
		scanf("%d", &N);
		int curr = 0;
		for (int i = 0; i < N; i++) {
			scanf("%s", dat[i]);
			used_p[i] = false;
			used_m[i] = false;
			for (int j = 0; j < N; j++) {
				if (dat[i][j] == '1') curr++;
			}
		}
		int remain_p = 0;
		int sol_pre = 0;
		for (int i = 0; i < N; i++) {
			if (!used_p[i]) {
				p_count = m_count = 0;
				dfs_p(i);
				if (p_count == m_count) {
					sol_pre += (p_count)* (p_count);
				}
				else if (m_count == 0) {
					remain_p++;
				}
				else {
					pm.push_back(make_pair(p_count, m_count));
				}
			}
		}
		int M = (int)pm.size();
		if (M > 0) {
			vector<int> cost;
			vector<int> need;
			cost.resize(1 << M);
			need.resize(1 << M);
			for (int i = 0; i < (1 << M); i++) {
				int p, m, cnt;
				p = m = 0;
				cnt = 0;
				for (int j = 0; j < M; j++) {
					if (i & (1 << j)) {
						p += pm[j].first;
						m += pm[j].second;
						cnt++;
					}
				}
				if (m > p) {
					need[i] = m - p;
				}
				else {
					need[i] = 0;
				}

				cost[i] = (p + need[i]) * (p + need[i]);
			}

			vector<vector<int> > dyn;
			dyn.resize(1 << M);
			for (int i = 0; i < (1 << M); i++) dyn[i].resize(remain_p + 1, -1);
			dyn[0][0] = 0;

			int mask = (1 << M) - 1;
			for (int i = 0; i < (1 << M); i++) {
				for (int j = 0; j <= remain_p; j++) {
					if (dyn[i][j] < 0) continue;

					if (j + 1 <= remain_p) {
						update(dyn[i][j + 1], dyn[i][j] + 1);
					}

					int r_mask = mask ^ i;
					for (int k = r_mask; k > 0; k = (k - 1)&r_mask) {
						int ti = i | k;
						int tj = j + need[k];
						if (tj > remain_p) continue;
						update(dyn[ti][tj], dyn[i][j] + cost[k]);
					}
				}
			}
			sol_pre += dyn[mask][remain_p];
		}
		else {
			sol_pre += remain_p;
		}
		printf("Case #%d: %d\n", tc, sol_pre - curr);
	}
	return 0;
}
