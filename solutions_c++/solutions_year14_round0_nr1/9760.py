#include <cstdio>

using namespace std;

int main() {
	int test_cases;
	scanf("%d", &test_cases);
	for (int test = 1; test <= test_cases; test++) {
		int answer, cnt = 0, dev_null;
		int number_set1[4] = {0};
		int number_set2[4] = {0};
		scanf("%d", &answer);
		for (int i = 1; i <= 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (i == answer) {
					scanf("%d", &number_set1[j]);
				} else {
					scanf("%d", &dev_null);
				}
			}
		}
		scanf("%d", &answer);
		for (int i = 1; i <= 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (i == answer) {
					scanf("%d", &number_set2[j]);
				} else {
					scanf("%d", &dev_null);
				}
			}
		}

		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (number_set1[i] == number_set2[j]) {
					cnt++;
					answer = number_set1[i];
				}
			}
			if (cnt > 1) break;
		}
		if (cnt == 0) printf("Case #%d: Volunteer cheated!\n", test);
		else if (cnt == 1) printf("Case #%d: %d\n", test, answer);
		else if (cnt > 1) printf("Case #%d: Bad magician!\n", test);
	}
	return 0;
}