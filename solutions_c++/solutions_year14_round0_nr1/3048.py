#include <cstdio>

int A[5];

int main() {
	int N;
	scanf("%d", &N);
	for (int C = 1; C <= N; C++) {
		int P, Q, count = 0, num = -1;
		scanf("%d", &P);
		for (int i = 1; i <= 4; i++) {
			if (i != P) for (int j = 1; j <= 4; j++) scanf("%*d");
			else for (int j = 1; j <= 4; j++) scanf("%d", A+j);
		}
		scanf("%d", &Q);
		for (int i = 1; i <= 4; i++) {
			if (i != Q) for (int j = 1; j <= 4; j++) scanf("%*d");
			else
				for (int j = 1; j <= 4; j++) {
					int t;
					scanf("%d", &t);
					for (int k = 1; k <= 4; k++) {
						if (t == A[k]) {
							count++;
							num = t;
						}
					}
				}
		}

		printf("Case #%d: ", C);
		if (count == 0) printf("Volunteer cheated!\n");
		else if (count > 1) printf("Bad magician!\n");
		else printf("%d\n", num);

	}
	return 0;
}
