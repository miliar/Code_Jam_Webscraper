#include <iostream>

using namespace std;

int main() {
	int numCases;
	cin >> numCases;
	
	for (int i = 1; i <= numCases; i++) { 
		int cards[4][4];
		int newCards[4][4];
		int oRow, nRow;
		
		cin >> oRow;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				cin >> cards[j][k];
			}
		}
		
		cin >> nRow;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				cin >> newCards[j][k];
			}
		}
		
		int nFound = 0;
		int lastFound = -1;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (cards[oRow - 1][j] == newCards[nRow - 1][k]) {
					nFound++;
					lastFound = cards[oRow - 1][j];
					break;
				}
			}
		}
		
		cout << "Case #" << i << ": ";
		switch (nFound) {
			case 0:
				cout << "Volunteer cheated!" << endl;
				break;
			case 1:
				cout << lastFound << endl;
				break;
			default:
				cout << "Bad magician!" << endl;
				break;
		}
	}
	
	return 0;
}