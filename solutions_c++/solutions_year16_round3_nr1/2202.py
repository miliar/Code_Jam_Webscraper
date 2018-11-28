#define CJ1C_A

#ifdef CJ1C_A
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

void findmax(int arr[], int N, int *max1, int *max2) {
	*max1 = 0;
	for (int i = 1; i < N; i++) {
		if (arr[i] >= arr[*max1])
			*max1 = i;
	}

	*max2 = 0;

	for (int i = 0; i < N; i++) {
		if (*max1 == i) {
			if (*max2 == 0 && *max1 == 0)
				*max2 = 1;
			continue;
		}
		if (arr[i] >= arr[*max2])
			*max2 = i;
	}
}

int main() {
	//freopen("in.txt", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		int N;
		scanf("%d\n", &N);

		int P[26] = { 0 };

		for (int j = 0; j < N; j++) {
			scanf("%d ", &P[j]);
			if (j == N - 1)
				scanf("\n");
		}

		//
		int max1, max2;

		while (true) {
			findmax(P, N, &max1, &max2);
			if (P[max1] == 0) {
				break;
			}

			if (P[max1] - P[max2] >= 2) {
				printf("%c%c ", 'A' + max1, 'A' + max1);
				P[max1] -= 2;
			}
			else {
				if (P[max2] == 0) {
					if (P[max1] == 1) {
						printf("%c ", 'A' + max1);
						P[max1] -= 1;
					}
				}
				else {
					int count = 0;

					for (int j = 0; j < N; j++) {
						if (P[j]==1)
							count++;
					}

					if (!(N>=3 && count==3)) {
						printf("%c%c ", 'A' + max1, 'A' + max2);
						P[max1] -= 1;
						P[max2] -= 1;
					}
					else {
						printf("%c ", 'A' + max1);
						P[max1] -= 1;
					}
				}
			}
		}
		//

		printf("\n");
	}

	return 0;
}

#endif