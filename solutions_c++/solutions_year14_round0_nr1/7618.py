#include <cstdio>

#include <algorithm>

using namespace std;

void Solve() {
	int A, B;

	int arr1[4], arr2[4];
	scanf("%d", &A);
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) {
			int d;
			scanf("%d", &d);
			if (i == A - 1) arr1[j] = d;
		}
	scanf("%d", &B);
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) {
			int d;
			scanf("%d", &d);
			if (i == B - 1) arr2[j] = d;
		}
	int res = -1;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (arr1[i] == arr2[j]) {
				if (res != -1) {
					printf("Bad magician!\n");
					return;
				}
				res = arr1[i];
			}
	if (res == -1) printf("Volunteer cheated!\n");
	else printf("%d\n", res);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		Solve();
	}
	return 0;
}
