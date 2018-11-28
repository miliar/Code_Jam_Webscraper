#pragma warning(disable:4996)
#include <stdio.h>

FILE *wfp;
int p[26];
char ans[2];

int main() {
	int ts, len, n;
	int tmp;
	double total;

	wfp = fopen("output.txt", "w");

#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#endif

	scanf("%d", &ts);

	for (int t = 1; t <= ts; t++) {
		total = 0;

		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			scanf("%d", &tmp);
			total += tmp;
			p[i] = tmp;
		}

		fprintf(wfp, "Case #%d: ", t);

		int flag;
		while (total > 0) {
			if ((int)total == 1) {
				printf("error %d\n", t);
			}
			else if ((int)total == 2) {
				for (int i = 0; i < n; i++) {
					if (p[i] > 0) {
						fprintf(wfp, "%c", i + 'A');
						p[i]--;
						total--;
						break;
					}
				}
				for (int i = 0; i < n; i++) {
					if (p[i] > 0) {
						fprintf(wfp, "%c ", i + 'A');
						p[i]--;
						total--;
						break;
					}
				}
			}

			for (int i = 0; i < n; i++) {
				if (p[i] > 0) {
					p[i]--;
					total--;
					for (flag = 0; flag < n; flag++) {
						if (p[flag] / (total) > 0.5)
							break;
					}
					if (flag != n) {
						p[i]++;
						total++;
					}
					else {
						fprintf(wfp, "%c ", i + 'A');
						break;
					}

					for (int i = 0; i < n - 1; i++) {
						for (int j = i + 1; j < n; j++) {
							if (p[i] > 0 && p[j] > 0) {
								p[i]--;
								p[j]--;
								total -= 2;
								for (flag = 0; flag < n; flag++) {
									if (p[flag] / (total) > 0.5)
										break;
								}
								if (flag != n) {
									p[i]++;
									p[j]++;
									total += 2;
								}
								else {
									fprintf(wfp, "%c%c ", i + 'A', j + 'A');
									break;
								}
							}
						}
					}

				}
			}
		}

		fprintf(wfp, "\n");

	}

	fclose(wfp);

	return 0;
}
