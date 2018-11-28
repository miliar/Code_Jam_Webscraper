#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>

typedef unsigned int uint;

using namespace std;

void readArrangement(int cards[4][4]) {
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			cin >> cards[i][j];
}

string solve(int row1, int row2, int arr1[4][4], int arr2[4][4]) {
	int count = 0, number;

	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			if(arr1[row1][i] == arr2[row2][j]) {
				++count;
				number = arr1[row1][i];
			}

	if(count > 1)
		return "Bad magician!";

	if(count == 0)
		return "Volunteer cheated!";

	return to_string(number);
}

int main() {
	int cases, row1, row2;
	int arr1[4][4], arr2[4][4];

	cin >> cases;

	for(int i = 0; i < cases; ++i) {
		cout << "Case #" << i+1 << ": ";

		cin >> row1;
		--row1;
		readArrangement(arr1);
		cin >> row2;
		--row2;
		readArrangement(arr2);

		cout << solve(row1, row2, arr1, arr2) << endl;
	}

	return 0;
}
