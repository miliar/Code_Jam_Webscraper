#include <cstdio>
#include <set>
#include <algorithm>
#include <vector>

const int GRID_SIZE = 4;

using namespace std;

set<int> currRow;
set<int> currRow2;

int main () {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		int row;
		scanf("%d", &row);
		// printf("~%d~\n",row);
		for (int i = 0; i < GRID_SIZE; i++) {
			for (int j = 0; j < GRID_SIZE; j++) {
				int num;
				scanf("%d", &num);
				if (i+1 == row) {
					currRow.insert(num);
				}
				// printf("[%d]", num);
			}
			// printf("\n");
		}
		// printf("--\n");


		int row2;
		scanf("%d", &row2);
		// printf("~%d~\n",row2);
		for (int i = 0; i < GRID_SIZE; i++) {
			for (int j = 0; j < GRID_SIZE; j++) {
				int num;
				scanf("%d", &num);
				if (i+1 == row2) {
					currRow2.insert(num);
				}
				// printf("[%d]", num);
			}
			// printf("\n");
		}
		// printf("--\n");

		vector<int> intersect;
		set_intersection(currRow.begin(), currRow.end(),
					     currRow2.begin(), currRow2.end(),
					     back_inserter(intersect));
		if (intersect.size() == 1) {
			printf("Case #%d: %d\n",t+1, intersect[0]);
		} else if (intersect.size() == 0) {
			printf("Case #%d: Volunteer cheated!\n",t+1);
		} else {
			printf("Case #%d: Bad magician!\n",t+1);
		}

		// for (set<int>::iterator it = intersect.begin(); it != intersect.end(); ++it) {
		// 	printf("[%d]", *it);
		// }
		currRow.clear();
		currRow2.clear();
	}



	return 0;
}