#include <iostream>
using namespace std;
int main() {
	int T, t;
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		int L, X;
		scanf("%d", &L);
		scanf("%d", &X);
		string s;
		string sl;
		cin >> s;
		sl = "";
		for (int i = 0; i < X; i++) {
			sl += s;
		}
		// 1 -> 0
		// i -> 1
		// j -> 2
		// k -> 3
		int mul[5][5];
		mul[1][1] = 1; mul[1][2] = 2; mul[1][3] = 3; mul[1][4] = 4;
		mul[2][1] = 2; mul[2][2] = -1; mul[2][3] = 4; mul[2][4] = -3;
		mul[3][1] = 3; mul[3][2] = -4; mul[3][3] = -1; mul[3][4] = 2;
		mul[4][1] = 4; mul[4][2] = 3; mul[4][3] = -2; mul[4][4] = -1;
		int cmap[300];
		cmap['i'] = 2;
		cmap['j'] = 3;
		cmap['k'] = 4;
		int prev = 1;
		int cur = 1;
		int sign = 1;
		int N = L * X;
		for (int i = 0; i < N; i++) {
			prev = cur;
			if (prev < 0) {
				sign = -1;
			} else {
				sign = 1;
			}
			cur = sign * mul[sign * prev][cmap[sl[i]]];
		}
		if (cur == -1) {
			int i_pos = 0;
			bool found = false;
			cur = 1;
			while (i_pos < N && cur != 2) {
				prev = cur;
				if (prev < 0) {
					sign = -1;
				} else {
					sign = 1;
				}
				cur = sign * mul[sign * prev][cmap[sl[i_pos]]];
				//printf("cur = %d\n", cur);
				i_pos++;
			}
			i_pos--;
			if (i_pos < N) {
				int k_pos = N - 1;
				cur = 1;
				sign = 1;
				while (k_pos > i_pos && cur != 4) {
					prev = cur;
					if (prev < 0) {
						sign = -1;
					} else {
						sign = 1;
					}
					cur = sign * mul[cmap[sl[k_pos]]][sign * prev];
					k_pos--;
				}
				if (k_pos > i_pos) {
					found = true;
				}
			}
			if (found) {
				printf("Case #%d: YES\n", t);
			} else {
				printf("Case #%d: NO\n", t);
			}
		} else {
			printf("Case #%d: NO\n", t);
		}
	}
	return 0;
}