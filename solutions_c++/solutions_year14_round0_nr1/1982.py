#include <iostream>

using namespace std;

#define CARD_MATRIX_SIZE 4

int main()
{
	int testCases;
	cin >> testCases;

	for (int i=0; i<testCases; i++) {

		//First answer
		int firstAnswer;
		cin >> firstAnswer;

		int firstCardMatrix[CARD_MATRIX_SIZE][CARD_MATRIX_SIZE];

		for (int j=0; j<CARD_MATRIX_SIZE; j++) {
			for (int k=0; k<CARD_MATRIX_SIZE; k++) {
				cin >> firstCardMatrix[j][k];
			}
		}

		//Second answer
		int secondAnswer;
		cin >> secondAnswer;

		int secondCardMatrix[CARD_MATRIX_SIZE][CARD_MATRIX_SIZE];

		for (int j=0; j<CARD_MATRIX_SIZE; j++) {
			for (int k=0; k<CARD_MATRIX_SIZE; k++) {
				cin >> secondCardMatrix[j][k];
			}
		}

		//Calculate
		int solution = -1;
		string output;
		for (int j=0; j<CARD_MATRIX_SIZE && solution != -2; j++) {
			for (int k=0; k<CARD_MATRIX_SIZE; k++) {
				if (firstCardMatrix[firstAnswer - 1][j] == secondCardMatrix[secondAnswer - 1][k]) {
					if (solution == -1) {
						solution = firstCardMatrix[firstAnswer - 1][j];
					}
					else {
						solution = -2;
						break;
					}
				}
			}
		}

		cout << "Case #" << i + 1 << ": ";
		if (solution == -1) {
			cout << "Volunteer cheated!";
		}
		else if (solution == -2) {
			cout << "Bad magician!";
		}
		else {
			cout << solution;
		}
		cout << endl;

	}

	return 0;
}