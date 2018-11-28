#include <iostream>
using namespace std;

#define NUMCOLS 4
#define NUMROWS 4 

void getRow(int row[NUMCOLS]);
int getAnswer(int row1[NUMCOLS], int row2[NUMCOLS]);
void printRow(int row[NUMCOLS]);

int main() {
	int numTestCases;
	int row1[NUMCOLS];
	int row2[NUMCOLS];
	int ans;

	// reading in number of test cases
	cin >> numTestCases;

	for (int i = 0; i < numTestCases; ++i) {
		getRow(row1);
		getRow(row2);	
		ans = getAnswer(row1, row2);
		cout << "Case #" << i + 1 << ": ";
		if (ans == -1) {
			//volunteer cheated
			cout << "Volunteer cheated!\n";
		} else if (ans == -2) {
			// multiple solutions;
			cout << "Bad Magician!\n";
		} else {
			cout << ans << '\n';
		}
	}
}

void getRow(int row[NUMCOLS]) {
	int rowNum, tempInt;
	// reading in first card arrangement
	cin >> rowNum;
	// skips until correct row
	for (int j = NUMCOLS; j < rowNum * NUMCOLS; ++j) {
		cin >> tempInt;
	}
	// reading in row and store in array
	for (int j = 0; j < NUMCOLS; ++j) {
		cin >> row[j];
	}
	// skips until end
	for (int j = 0; j < (NUMROWS - rowNum) * NUMCOLS; ++j) {
		cin >> tempInt;	
	}
}

int getAnswer(int row1[NUMCOLS], int row2[NUMCOLS]) {
	int numAns = 0, ans = 0;
	for (int i = 0; i < NUMCOLS; ++i) {
		for (int j = 0; j < NUMCOLS; ++j) {
			if (row1[i] == row2[j]) {
				++numAns;
				ans = row1[i];
			}
		}
	}
	if (numAns == 0) {
		// volunteer cheated
		return -1;
	} else if (numAns == 1) {
		// answer
		return ans;
	} else {
		// multiple solutions
		return -2;
	}
}

void printRow(int row[NUMCOLS]) {
	for (int i = 0; i < NUMCOLS; ++i) {
		cout << row[i] << '\t';
	}
	cout << '\n';
}
