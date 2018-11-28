/*
 * main.cpp
 *
 *  Created on: 12/04/2013
 *      Author: Eden
 */
#include <iostream>
#include <fstream>
using namespace std;

bool check(int** arr, int rows, int cols, int i, int j) {
	int val = arr[i][j];
	for (int k = 0; k < cols; k++) {
		if (arr[i][k] > val)
			break;
		if (k == cols - 1)
			return true;
	}
	for (int k = 0; k < rows; k++) {
		if (arr[k][j] > val)
			break;
		if (k == rows - 1)
			return true;
	}
	return false;
}

int main() {
	ifstream myfile("C:\\users\\eden\\B-large.in");
	ofstream output("C:\\users\\eden\\out.txt");
	if (!myfile || !output) {
		cout << "FAIL";
		return 0;
	}
	bool poss;
	int T, N, M;
	int** lawn;
	myfile >> T;
	for (int i = 1; i <= T; i++) {
		output << "Case #" << i << ": ";
		poss = true;
		myfile >> N >> M;
		lawn = new int *[N];
		for (int j = 0; j < N; j++) {
			lawn[j] = new int[M];
		}
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				myfile >> lawn[j][k];
			}
		}
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) {
				if (!check(lawn, N, M, j, k)) {
					poss = false;
					break;
				}
			}
			if (!poss)
				break;
		}
		for (int l = 0; l < N; l++) {
			delete[] lawn[l];
		}
		delete[] lawn;
		if (!poss) {
			output << "NO" << endl;
			continue;
		}
		output << "YES" << endl;
	}
	myfile.close();
	output.close();
	return 0;
}

