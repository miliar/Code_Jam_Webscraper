#include <stdio.h>

int cases, kejs;
int i, j, n, cnt;
char a[100][200];
int ai[100], aip[100];
char b[100][200];

int abs(int a) {
	if (a < 0) return -a;
	return a;
}

int main() {
    scanf("%d", &cases);
    for (kejs = 1; kejs <= cases; kejs++) {
        printf("Case #%d: ", kejs);
				scanf("%d", &n);
				for (i = 0; i < n; i++) {
					scanf("%s", a[i]);
					ai[i] = 0;
					aip[i] = -1;
					while(a[i][ai[i]] == a[i][ai[i]+1]) ai[i]++;
				}
				cnt = 0;
				for (;;) {
					for (i = 1; i < n; i++) {
						if (a[i][ai[i]] != a[i-1][ai[i-1]]) break;
					}
					if (i < n) {
						printf("Fegla Won\n");
						break;
					}
					if (a[0][ai[0]] == '\0') {
						printf("%d\n", cnt);
						break;
					}
					int m = 300;
					for (j = 1; j <= 100; j++) {
						int q = 0;
						for (i = 0; i < n; i++) {
							q += abs(ai[i] - aip[i] - j);
						}
						if (q < m) m = q;
					}
					cnt += m;
					for (i = 0; i < n; i++) {
						aip[i] = ai[i];
						ai[i]++;
						if (a[i][ai[i]]) {
							while(a[i][ai[i]] == a[i][ai[i]+1]) ai[i]++;
						}
					}
				}
    }
    return 0;
}
