#include <cstdio>
#include <iostream>

using namespace std;

int main() {
	int T;
	int i;
	scanf("%d", &T);

	for (i = 0; i < T; ++i) { 
		int a1, a2;
		scanf("%d", &a1);
		int temp;
		int val[4];
		int j, k;

		for (j = 0; j < 4; ++j) {
			for (k = 0; k < 4; ++k) {
				scanf("%d", &temp);

				if (j + 1 == a1) {
					val[k] = temp;
				}
			}
		}

		scanf("%d", &a2);
		int ncand = 0;
		int cand;
		int l;
		for (j = 0; j < 4; ++j) {
			for (k = 0; k < 4; ++k) {
				scanf("%d", &temp);

				if (j + 1 == a2) {
					for (l = 0; l < 4; ++l) {
						if (val[l] == temp) {
							++ncand;
							cand = temp;
						}
					}
				}
			}
		}

		printf("Case #%d: ", i + 1);
		if (ncand == 1)
			printf("%d", cand);
		if (ncand > 1)
			printf("Bad magician!");
		if (ncand < 1)
			printf("Volunteer cheated!");

		printf("\n");
	}
	return 0;
}