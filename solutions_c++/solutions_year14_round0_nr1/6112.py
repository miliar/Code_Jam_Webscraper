#include <iostream>
#include <cstdio>

#define CHEATED -5
#define MULTIPLE_POSSIBLE -6

int main(int argc, char** argv) {
	using namespace std;

	int numCases;
	cin >> numCases;

	for (int caseNum = 1; caseNum <= numCases; caseNum++) {
		int answerFirst;
		cin >> answerFirst;
		answerFirst -= 1;
		int layoutFirst[4][4];
		for (int row = 0; row < 4; row++) {
			scanf("%d %d %d %d",
				&layoutFirst[row][0],
				&layoutFirst[row][1],
				&layoutFirst[row][2],
				&layoutFirst[row][3]);
		}
		int answerSecond;
		cin >> answerSecond;
		answerSecond -= 1;
		int layoutSecond[4][4];
		for (int row = 0; row < 4; row++) {
			scanf("%d %d %d %d",
				&layoutSecond[row][0],
				&layoutSecond[row][1],
				&layoutSecond[row][2],
				&layoutSecond[row][3]);
		}
		cout << "Case #" << caseNum << ": ";
		int card = CHEATED;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (layoutFirst[answerFirst][i] ==
					layoutSecond[answerSecond][j]) {
					if (card == CHEATED) {
						card = layoutFirst[answerFirst][i];
					} else {
						card = MULTIPLE_POSSIBLE;
					}
				}
			}
		}
		if (card == MULTIPLE_POSSIBLE) {
			cout << "Bad magician!";
		} else if (card == CHEATED) {
			cout << "Volunteer cheated!";
		} else {
			cout << card;
		}
		cout << endl;
	}
	return 0;
}
