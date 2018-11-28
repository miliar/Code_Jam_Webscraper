#include <cstdio>
#include <vector>
using namespace std;

#define SIZE 4
#define CYCLE 2
int row[SIZE][2];

vector<int> result;

void input(int number) {
	int rowNumber, temp;
	scanf("%d", &rowNumber);
	for (int j = 0; j < SIZE; j++) {
		for (int k = 0; k < SIZE; k++) {
			scanf("%d", &temp);
			if (rowNumber == j + 1)
				row[k][number] = temp;
		}
	}
}



int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int Total = 0;
	scanf("%d", &Total);
	for (int i = 0; i < Total; i++) {
		result.clear();
		printf("Case #%d: ", i + 1);
		for (int j = 0; j < CYCLE; j++) {
			input(j);
		}
/*		for (int j = 0 ; j < SIZE; j++) {
			for (int k = 0; k < CYCLE; k++) {
				printf("%d ", row[j][k]);
			}
			puts("");
		}
*/		for (int j = 0 ; j < SIZE; j++) {
			for (int k = 0; k < SIZE; k++) {
				if (row[k][1] == row[j][0]) {
					result.push_back(row[k][1]);
				}
			}
		}
		if (1 == result.size()) {
			printf("%d\n", result[0]);	
		} else if (1 < result.size()) {
			printf("Bad magician!\n");
		} else {
			printf("Volunteer cheated!\n");
		}

	}
	return 0;
}
