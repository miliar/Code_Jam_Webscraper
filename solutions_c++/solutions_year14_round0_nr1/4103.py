

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <list>

#include <limits.h>


int main() {
	int T;
	
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++) {
	
		int row1;
		scanf("%d", &row1);
		row1--;
		int field1[4][4];
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &field1[i][j]);
			}
		}
		
		int row2;
		scanf("%d", &row2);
		row2--;
		int field2[4][4];
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &field2[i][j]);
			}
		}
		
		std::list<int> possibilities;
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (field1[row1][i] == field2[row2][j]) {
					possibilities.push_back(field1[row1][i]);
				}
			}
		}
		
		printf("Case #%d: ", t);
		if (possibilities.size() == 0) {
			printf("Volunteer cheated!\n");
		}
		else if (possibilities.size() == 1) {
			printf("%d\n", possibilities.front());
		}
		else {
			printf("Bad magician!\n");
		}
	}

}



