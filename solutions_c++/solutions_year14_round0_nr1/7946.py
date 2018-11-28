#include <cstdio>
#include <cstring>

const int MAX_NUMBER = 16;

int matrix_1[MAX_NUMBER][MAX_NUMBER];
int matrix_2[MAX_NUMBER][MAX_NUMBER];

int main() {
	int test_case;
	scanf("%d", &test_case);
	int case_number = 1;
	while (test_case--) {
		int row_1, row_2;
		scanf("%d", &row_1);
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				scanf("%d", &matrix_1[i][j]);
			}
		}
		scanf("%d", &row_2);
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				scanf("%d", &matrix_2[i][j]);
			}
		}
		int ans = 0;
		int number;
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				if (matrix_1[row_1][i] == matrix_2[row_2][j]) {
					ans++;
					number = matrix_1[row_1][i];
					break;
				}
			}
		}
		if (ans == 0) {
			printf("Case #%d: Volunteer cheated!\n", case_number);
		}
		else if (ans == 1) {
			printf("Case #%d: %d\n", case_number, number);
		}
		else {
			printf("Case #%d: Bad magician!\n", case_number);
		}
		case_number++;
	}
	return 0;
}