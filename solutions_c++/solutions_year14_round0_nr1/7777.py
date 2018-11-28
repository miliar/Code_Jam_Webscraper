#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {

	int answerRow, answerCol;
	int firstGrid[5][5], secondGrid[5][5];

	int numTest, num = 1;
	cin >> numTest;
	while (numTest--) {
		cin >> answerRow;
		for (int row = 1; row <= 4; row++) {
			for (int col = 1; col <= 4; col++) {
				cin >> firstGrid[row][col];
			}
		}
		cin >> answerCol;
		for (int row = 1; row <= 4; row++) {
			for (int col = 1; col <= 4; col++) {
				cin >> secondGrid[row][col];
			}
		}

		int numFound = 0, card;
		for (int i = 1; i <= 4; i++) {
			int tempCard = firstGrid[answerRow][i];
			for (int row = 1; row <= 4; row++) {
				if (secondGrid[answerCol][row] == tempCard) {
					numFound++;
					card = tempCard;
				}
			}
		}

		if (numFound == 0)
			cout << "Case #" << num++ << ": " << "Volunteer cheated!" << endl;
		else if (numFound == 1)
			cout << "Case #" << num++ << ": " << card << endl;
		else
			cout << "Case #" << num++ << ": " << "Bad magician!" << endl;
	}

	return 0;
}
