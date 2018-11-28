#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int s[10010];
int x[1010];

int main() {
	int T, N, X;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		scanf(" %d %d", &N, &X);
		memset(x, 0, sizeof(x));
		int M = 0, m = 10000;
		for (int i = 0; i < N; i++) {
			scanf(" %d", &s[i]);
			x[s[i]]++;
			M = max(M, s[i]);
			m = min(m, s[i]);
		}

		int ans = 0;
		int p1 = m, p2 = M;
		while (p1 < p2) {
			if (p1 + p2 <= X) {
				int aux = min(x[p1], x[p2]);
				ans += aux;
				x[p1] -= aux;
				x[p2] -= aux;
			}
			else {
				ans += x[p2];
				x[p2]  = 0;
			}

			if (x[p1] == 0) {
				while (p1 < p2 && x[p1] == 0) {
					p1++;
				}
			}
			else {
				while (p1 < p2 && x[p2] == 0) {
					p2--;
				}
			}
		}
		if (p1 * 2 <= X) {
			ans += x[p1]/2 + x[p1] % 2;
		}
		else {
			ans += x[p1];
		}

		printf("Case #%d: %d\n", _42, ans);
	}
	return 0;
}
