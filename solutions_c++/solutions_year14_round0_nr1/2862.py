#include <cstdio>

using namespace std;

int main() {
	int testcases;
	int a1, a2, myans;
	int row1[4], row2[4];
	
	scanf("%d", &testcases);
	
	for(int t = 1; t <= testcases; t++) {
		scanf("%d", &a1);
		
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(i == (a1 - 1)) {
					scanf("%d", &row1[j]);
				}
				else {
					scanf("%*d");
				}
			}
		}
		
		scanf("%d", &a2);
		
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(i == (a2 - 1)) {
					scanf("%d", &row2[j]);
				}
				else {
					scanf("%*d");
				}
			}
		}
		
		myans = 0;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(row1[i] == row2[j]) {
					if(myans) {
						myans = -1;
						break;
					}
					else {
						myans = row1[i];
					}
				}
			}
		}
		
		printf("Case #%d: ", t);
		
		if(!myans) {
			printf("Volunteer cheated!\n");
		}
		else if(myans < 0) {
			printf("Bad magician!\n");
		}
		else {
			printf("%d\n", myans);
		}
	}

	return 0;
}