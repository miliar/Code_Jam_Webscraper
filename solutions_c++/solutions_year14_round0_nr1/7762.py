#include <stdio.h>


int T, n, a[17];

void readSet() {

	int line, tmp;
	scanf("%d", &line);

	for (int i = 1; i <= 4; i++) {
		for (int j = 1; j <= 4; j++) {
			scanf("%d", &tmp);
			if (i == line) {
				a[tmp]++;
			}
		}
	}
}

int main() {

	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);

	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		for (int i = 1; i <= 16; i++) {
			a[i] = 0;
		}

		readSet();
		readSet();

		int one = -1;
		for (int i = 1; i <= 16; i++) {
			if (a[i] == 2) {
				if (one == -1) {
					one = i;
				} else {
					one = -2;
					break;
				}
			}
		}

		printf("Case #%d: ", t);
		if (one == -2) {
			printf("Bad magician!\n");
		} else if (one == -1) {
			printf("Volunteer cheated!\n");
		} else {
			printf("%d\n", one);
		}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}