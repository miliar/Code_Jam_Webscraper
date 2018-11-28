#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <sstream>

using namespace std;

int main() {
	int number = 0;
	
	string str = "";
	while (true) {
		getline(cin, str);

		stringstream stream(str);
		if (stream >> number)
			break;
	}

	for(int l = 0; l < number; l++) {
		if(l != 0)
			cout << endl;

		int row, column;
		cin >> row >> column;

		int ** matrix, ** actualMatrix;
		matrix = new int*[row];
		actualMatrix = new int*[row];
		for(int i = 0; i < row; i++) {
			matrix[i] = new int[column];
			actualMatrix[i] = new int[column];
			for(int j = 0; j < column; j++) {
				cin >> matrix[i][j];
				actualMatrix[i][j] = 100;
			}
		}

		int findMax(int **, int, int, int);
		int max = 0;
		for(int i = 0; i < row; i++) {
			max = findMax(matrix, column, i, 0);
			for(int j = 0; j < column; j++) {
				actualMatrix[i][j] = max;
			}
		}
		for(int i = 0; i < column; i++) {
			max = findMax(matrix, row, i, 1);
			for(int j = 0; j < row; j++) {
				if(actualMatrix[j][i] > max)
					actualMatrix[j][i] = max;
			}
		}
		int i, j;
		for(i = 0; i < row; i++) {
			for(j = 0; j < column; j++) {
				if(matrix[i][j] != actualMatrix[i][j]) {
					break;
				}
			}
			if(j < column)
				break;
		}
		if(i < row) {
			cout << "Case #" << l + 1 << ": NO";
		} else {
			cout << "Case #" << l + 1 << ": YES";
		}
	}

	return 0;
}

int findMax(int ** matrix, int c, int a, int b) {
	int max = 0;
	if(b == 0) {
		for(int i = 0; i < c; i++) {
			if(matrix[a][i] > max) {
				max = matrix[a][i];
			}
		}
	} else {
		for(int i = 0; i < c; i++) {
			if(matrix[i][a] > max) {
				max = matrix[i][a];
			}
		}
	}
	return max;
}