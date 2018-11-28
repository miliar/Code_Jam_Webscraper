#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){
	int T;
	int currentCase = 0;
	scanf("%d", &T);
	while(T--) {
		currentCase++;
		int r1;
		scanf("%d", &r1);
		int firstArrangement[4][4];
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				scanf("%d", &firstArrangement[i][j]);
			}
		}
		int r2;
		scanf("%d", &r2);
		int secondArrangement[4][4];
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				scanf("%d", &secondArrangement[i][j]);
			}
		}
		int commonCount = 0, cardNumber;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				if(firstArrangement[r1-1][i] == secondArrangement[r2-1][j]) {
					commonCount++;
					cardNumber = firstArrangement[r1-1][i];
				}
			}
		}
		if(commonCount == 0) {
			printf("Case #%d: Volunteer cheated!\n", currentCase);
		} else if(commonCount == 1) {
			printf("Case #%d: %d\n", currentCase, cardNumber);
		} else if(commonCount > 1) {
			printf("Case #%d: Bad magician!\n", currentCase);
		}
	}
	return 0;
}