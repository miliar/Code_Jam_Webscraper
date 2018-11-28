#pragma warning(disable:4996)
#include <stdio.h>

int check[10];
int count;

int main() {
	int ts, k, c, s;
	FILE *wfp;
	unsigned long long tmp;
	int size;
	int l, r;

	wfp = fopen("output.txt", "w");

#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#endif

	scanf("%d", &ts);

	for (int t = 1; t <= ts; t++) {
		tmp = 1;
		scanf("%d %d %d", &k, &c, &s);

		fprintf(wfp, "Case #%d:", t);
		if (c == 1) {
			if (s >= k) {
				for (int i = 1; i <= k; i++) {
					fprintf(wfp, " %d", i);
				}
				fprintf(wfp, "\n");
			}
			else {
				fprintf(wfp, " IMPOSSIBLE\n");
			}
		}
		else {
			if (k <= 2) {
				if (s >= k)
					fprintf(wfp, " %d\n", k);
				else
					fprintf(wfp, " IMPOSSIBLE\n");
			}
			else if (k == 3) {
				if (s >= 2) {
					for (int i = 0; i < c; i++) {
						tmp *= k;
					}
					fprintf(wfp, " %d %I64u\n", 2, tmp - 1);
				}
				else {
					fprintf(wfp, " IMPOSSIBLE\n");
				}
			}
			else {
				for (int i = 0; i < c; i++) {
					tmp *= k;
				}

				if (k % 2 == 0) {
					l = (k - 2) / 2;
					r = l;
					if (s >= r + l) {
						for (int i = 0; i < l; i++)
							fprintf(wfp, " %d", i + 2);

						for (int i = r - 1; i >= 0; i--)
							fprintf(wfp, " %I64u", tmp - 1 - i);

						fprintf(wfp, "\n");
					}
					else {
						fprintf(wfp, " IMPOSSIBLE\n");
					}
				}
				else {
					l = ((k - 2) / 2) + 1;
					r = l - 1;
					if (s >= r + l) {
						for (int i = 0; i < l; i++)
							fprintf(wfp, " %d", i + 2);

						for (int i = r - 1; i >= 0; i--)
							fprintf(wfp, " %I64u", tmp - 1 - i);

						fprintf(wfp, "\n");
					}
					else {
						fprintf(wfp, " IMPOSSIBLE\n");
					}
				}
			}
		}
	}

	fclose(wfp);

	return 0;
}