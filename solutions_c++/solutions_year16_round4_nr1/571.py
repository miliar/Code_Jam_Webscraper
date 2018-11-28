#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>

using namespace std;
int ci[16][5000];
char s[4] = "PRS";
int num[4], inp[4];
char ans[5000];
void gao(int l, int r) {
	if (l == r) return;
	int mid = (l + r) >> 1;
	gao(l, mid), gao(mid + 1, r);
	bool flag = false;
	for (int i = 0; i < mid - l + 1; ++ i) {
		if (ans[l + i] > ans[mid + i + 1]) {
			flag = true;
			break;
		}
	}
	if (flag) {
		for (int i = 0; i < mid - l + 1; ++ i) {
			swap(ans[l + i], ans[mid + i + 1]);
		}
	}
}
int main() {
	int T, n;
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++ cas) {
		scanf("%d%d%d%d", &n, &inp[1], &inp[0], &inp[2]);
		num[0] = num[1] = num[2] = 0;
		printf("Case #%d: ", cas);
		ci[0][0] = 0;
		for (int i = 0; i < n; ++ i) {
			for (int j = 0; j < (1 << i); ++ j) {
				ci[i + 1][j << 1] = ci[i][j];
				ci[i + 1][j << 1 | 1] = ci[i][j] + 1;
				if (ci[i + 1][j << 1 | 1] == 3) {
					ci[i + 1][j << 1 | 1] = 2;
					ci[i + 1][j << 1] = 0;
				}
			}
		}
		for (int i = 0; i < (1 << n); ++ i) ++ num[ci[n][i]];
		int P[] = {0, 1, 2};
		bool flag;
		do {
			flag = true;
			for (int i = 0; i < 3; ++ i) {
				if (inp[P[i]] != num[i]) {
					flag = false;
					break;
				}
			}
			if (flag) {
				break;
			}
		} while (next_permutation(P, P + 3));
		if (flag) {
			
			for (int i = 0; i < (1 << n); ++ i) 
				ans[i] = s[P[ci[n][i]]];
			//for (int i = 0; i < (1 << n); ++ i) printf("%c", ans[i]);
			gao(0, (1 << n) - 1);
			for (int i = 0; i < (1 << n); ++ i) printf("%c", ans[i]);
			puts("");
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}