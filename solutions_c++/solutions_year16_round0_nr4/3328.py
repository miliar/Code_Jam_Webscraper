#include <cstdio>
using namespace std;

int table[110][110];

void init() {
	for (int i = 1, l = 1; i <= 100; i++) {
		for (int j = 1, val = 1; j <= 100; j += l, val++) {
			for (int k = 0; k < l && k + j <= 100; k++) {
				table[i][k + j] = val;
			}
		}
		if (l < 100)
			l <<= 1;
	}
}

unsigned long long a[120];

void runD() {
	freopen("d.out", "w", stdout);
	int t, k, c, s, cas = 0;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d%d", &k, &c, &s);
		if (s < table[c][k]) {
			printf("Case #%d: IMPOSSIBLE\n", ++cas);
		}
		else {
			for (int i = 0; i < k; i++) {
				a[i] = i;
			}
			/*
			unsigned long long ln = k;
			for (int v = 2; v <= c; v++) {
				int pre = table[v - 1][k];
				if (pre == 1) break;
				for (int i = 0, j = 0, cur = table[v][k]; i < cur; i++) {
					a[i] = a[j] * ln + a[j + 1];
					j += 1 + (pre - j > cur - i);
				}
				ln *= ln;
			}
			*/
			printf("Case #%d:", ++cas);
			for (int i = k - 1; i >= 0; i--) {
				printf(" %lld", a[i] + 1);
			}
			printf("\n");
		}
	}
}

int main() {
	init();
	runD();
	return 0;
}