#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn = 105;

char s[maxn][maxn];
char t[maxn][maxn];
int c[maxn][maxn];

int main() {
	int T, n;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%s", s[i]);
		int len = -1;
		bool ans = true;
		for (int i = 0; i < n; i++) {
			int k = 0;
			t[i][0] = s[i][0];
			c[i][0] = 1;
			for (int j = 1; s[i][j]; j++) {
				if (s[i][j-1] == s[i][j]) {
					c[i][k]++;
				} else {
					++k;
					t[i][k] = s[i][j];
					c[i][k] = 1;
				}
			}
			t[i][++k] = 0;
			if (len == -1) {
				len = k;
			} else if (len != k) {
				ans = false;
				break;
			}
		}
		
		for (int i = 1; i < n; i++) {
			if ( 0 != strcmp(t[0], t[i]) ) {
				ans = false;
				break;
			}
		}
		/*
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < len; j++) printf("%d ", c[i][j]);
			puts("");
		}
		*/

		printf("Case #%d: ", ca);
		if (ans) {
			int tot = 0;
			for (int k = 0; k < len; k++) {
				int sum = 0;
				for (int i = 0; i < n; i++) {
					sum += c[i][k];
				}
				int cnt = -1;
				for (int xt = sum / n; xt <= sum / n + 1; xt++) {
					int op = 0;
					for (int i = 0; i < n; i++) {
						op += abs(c[i][k] - xt);
					}
					if (cnt == -1 || cnt > op) cnt = op;
				}
			//	printf("%d:%d\n", k, cnt);
				tot += cnt;
			}
			printf("%d\n", tot);
		} else {
			printf("Fegla Won\n");
		}
	}
	return 0;
}
