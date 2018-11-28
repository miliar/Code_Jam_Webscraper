#include <cstdio>

bool C[20];

int main() {
	int z;
	scanf("%d", &z);

	for (int j=1; j<=z; j++) {
		int result = 0;
		for (int i=1; i<=16; i++) C[i] = false;

		int chosen;

		scanf("%d", &chosen);

		for (int i=0; i<4; i++) {
			for (int l=0; l<4; l++) {
				int a;
				scanf("%d", &a);

				if (i+1==chosen) {
					C[a] = true;
				}
			}
		}

		scanf("%d", &chosen);

		for (int i=0; i<4; i++) {
			for (int l=0; l<4; l++) {
				int a;
				scanf("%d", &a);

				if (i+1 == chosen) {
					if (C[a]) {
						if (result == 0) result = a;
						else result = -1;
					}
				}
			}
		}

		printf("Case #%d: ", j);

		if (result == 0) printf("Volunteer cheated!\n");
		else if (result < 0) printf("Bad magician!\n");
		else printf("%d\n", result);
	}

	return 0;
}