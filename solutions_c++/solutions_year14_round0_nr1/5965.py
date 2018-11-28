#include <cstdio>
#include <iostream>
using namespace std;

int main(void) {
	int t, testCases;
	int i, j, firstRow, secondRow, valueToFind, matchCount, matchValue=0;
	int firstGrid[4][4], secondGrid[4][4];
	cin >> testCases;
	for (t=1; t<=testCases; t++) {
		cin >> firstRow;
		for (i=0; i<4; i++) for (j=0; j<4; j++) cin >> firstGrid[i][j];
		cin >> secondRow;
		for (i=0; i<4; i++) for (j=0; j<4; j++) cin >> secondGrid[i][j];
		firstRow--;
		secondRow--;
		
		matchCount = 0;
		for (i=0; i<4; i++) {
			valueToFind = firstGrid[firstRow][i];
			for (j=0; j<4; j++) if (valueToFind==secondGrid[secondRow][j]) {
				matchCount++;
				matchValue = valueToFind;
				break;
			}
		}
		
		printf("Case #%d: ", t);
		if (matchCount==1) printf("%d\n", matchValue);
		else if (matchCount==0) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
	
	
	return 0;
}