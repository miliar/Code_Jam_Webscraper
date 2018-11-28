//============================================================================
// Name        : A_2014.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

void init(bool *array);

int main() {
	int testCase;
	int a1, a2;
	int firstSquare[4][4], secondSquare[4][4];
	bool firstArray[17], secondArray[17];
	int count;
	int selectedNumber;
	cin >> testCase;
	for(int i = 1; i <= testCase; i++){
		cin >> a1;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				cin >> firstSquare[j][k];
			}
		}

		cin >> a2;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				cin >> secondSquare[j][k];
			}
		}

		init(firstArray);
		init(secondArray);

		for(int j = 0; j < 4; j++){
			firstArray[firstSquare[a1 - 1][j]] = true;
			secondArray[secondSquare[a2 - 1][j]] = true;
		}

		count = 0;

		for(int j = 0; j < 17; j++) {
			if((firstArray[j] == true) && (secondArray[j] == true)) {
				count++;
				selectedNumber = j;
			}
		}

		cout << "Case #" << i << ": ";
		if(count == 0){
			cout << "Volunteer cheated!" << endl;
		}
		else if (count == 1) {
			cout << selectedNumber << endl;
		}
		else {
			cout << "Bad magician!" << endl;
		}
	}

	return 0;
}

void init(bool *array) {
	for(int i = 0; i < 17; i++)
		array[i] = false;
}
