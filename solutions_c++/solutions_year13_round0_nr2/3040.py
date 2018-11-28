#include <cstdio>
#include <set>
#include <utility>

using namespace std;

int lawn[111][111];
int n, m;
set<int> h;

bool up(set<int>::iterator &it) {
	int t, i, j, cnt_r = 0, cnt_c = 0;
	int he = *it;
	it++;
	int nh = (it == h.end()) ? 100 : *it;
	it--;
	int ch_r[111], ch_c[111];
	for (i = 0; i < n; i++) {
		for (j = 1; j < m && lawn[i][j] == he && lawn[i][j] == lawn[i][j - 1]; j++);
		if (j == m) ch_r[cnt_r++] = i;
	}
	for (i = 0; i < m; i++) {
		for (j = 1; j < n && lawn[j][i] == he && lawn[j][i] == lawn[j - 1][i]; j++);
		if (j == n) ch_c[cnt_c++] = i;
	}
	if (!cnt_r && !cnt_c) return false;
	for (i = 0; i < cnt_r; i++) {
		t = ch_r[i];
		for (j = 0; j < m; j++) {
			lawn[t][j] = nh;
		}
	}
	for (i = 0; i < cnt_c; i++) {
		t = ch_c[i];
		for (j = 0; j < n; j++) {
			lawn[j][t] = nh;
		}
	}
	return true;
}

bool check() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (lawn[i][j] != 100) return false;
		}
	}
	return true;
}

int main() {
	int t, T, i, j;
	bool can;
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		h.clear();
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++) {
				scanf("%d", &lawn[i][j]);
				h.insert(lawn[i][j]);
			}
		}
		can = true;
		for (set<int>::iterator it = h.begin(); it != h.end(); it++) {
			if (!up(it)) {
				can = false;
				break;
			}
		}
		if (!can) puts("NO");
		else if (!check()) puts("NO");
		else puts("YES");
	}
	return 0;
}
