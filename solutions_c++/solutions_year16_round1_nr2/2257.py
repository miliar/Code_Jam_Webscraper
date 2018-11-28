#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;
const int inf = 0x3f3f3f3f;

int list[128][64], q[128][64], mat[64][64];
vector<pair<int, int> > ac;
int n;
int main() {
	freopen("B-small-attempt5.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int _, cas = 1;
	scanf("%d", &_);
	while (_--) {
		printf("Case #%d: ", cas);
		++cas;
		ac.clear();

		memset(mat, -1, sizeof mat);
		int ans = -1;
		scanf("%d", &n);
		int m = 2 * n - 1;
		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < n; ++j) {
				scanf("%d", &list[i][j]);
				q[i][j] = list[i][j];
			}
		}
		for (int i = 0; i < n; ++i) {
			int mini = inf;
			int seq[2] = {-1, -1};
			for (int j = 0; j < m; ++j) {
				if (list[j][i] < mini) {
					mini = list[j][i];
					seq[0] = j;
				}
			}
			for (int j = 0; j < m; ++j) {
				if (list[j][i] == mini && j != seq[0]) {
					seq[1] = j;
				}
			}
			ac.push_back(make_pair(seq[0], seq[1]));
			if (seq[1] == -1) {
				ans = i;
			}
			for (int k = 0; k < n; ++k) {
				list[seq[0]][k] = inf;
				if (seq[1] >= 0) list[seq[1]][k] = inf;
			}
		}
		int maxs = (1 << n) - 1;
		for (int s = 0; s <= maxs; ++s) {
			bool flag = 1;
			for (int i = 0; i < n; ++i) {
				int num = -1;
				if (s & (1 << i)) {
					num = ac[i].first;
				} else {
					num = ac[i].second;
				}
				if (num == -1) {
					flag = 0;
					break;
				}
				for (int k = 0; k < n; ++k) {
					mat[i][k] = q[num][k];
				}
			}
			if (flag) {
				for (int i = 0; i < n; ++i) {
					int num = -1;
					if (s & (1 << i)) {
						num = ac[i].second;
					} else {
						num = ac[i].first;
					}
					if (num == -1) continue;

					for (int k = 0; k < n; ++k) {
						if (mat[k][i] != q[num][k]) {
							flag = 0;
							break;
						}
					}
				}
			}
			if (flag) break;
		}
		for (int k = 0; k < n; ++k) {
			printf("%d ", mat[k][ans]);
		}
		puts("");
	}
	return 0;
}