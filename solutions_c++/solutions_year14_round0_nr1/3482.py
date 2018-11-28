#include <iostream>
#include <vector>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++) {
		int boardOld[16];
		int oldRow;
		cin >> oldRow;
		for (int j = 0; j < 16; j++) {
			cin >> boardOld[j];
		}
		int boardNew[16];
		int newRow;
		cin >> newRow;
		for (int j = 0; j < 16; j++) {
			cin >> boardNew[j];
		}
		int found = 0;
		int num = 0;
		for (int k = (oldRow*4)-4; k < (oldRow*4); k++) {
			for (int m = (newRow*4)-4; m < (newRow*4); m++) {
				if (boardOld[k] == boardNew[m]) {
					found++;
					num = boardNew[m];
				}
			}
		}
		if (found == 0)
			cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
		else if (found == 1) {
			cout << "Case #" << i+1 << ": " << num << endl;
		} else
			cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
	}
	return 0;
}