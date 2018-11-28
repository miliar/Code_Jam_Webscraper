#include<cstdlib>
#include<cstdio>
#include <iostream>
using namespace std;
int solveP1(int* fst, int* scnd) {
	int value = -1;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (fst[i] == scnd[j]) {
				if (value == -1) {
					value = fst[i];
				} else
					return -2;
			}
		}
	}
	return value;
}
int* getrow() {
	int* row = new int[4];
	int answer, card;
	cin >> answer;
	answer--;
	answer *= 4;
	for (int j = 0; j < 16; j++) {

		cin >> card;
		if (j >= answer && j < answer + 4) {
			row[j - answer] = card;
		}
	}
	return row;
}
int main() {
	freopen("A-small-attempt0.out", "wt", stdout);
	freopen("A-small-attempt0.in", "rt", stdin);
	int cases;
	cin >> cases;
	int* first;
	int* second;

	for (int i = 0; i < cases; i++) {
		first = getrow();
		second = getrow();
		int value = solveP1(first, second);
		switch (value) {
		case -1:
			cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
			break;
		case -2:
			cout << "Case #" << i + 1 << ": Bad magician!" << endl;
			break;
		default:
			cout << "Case #" << i + 1 << ": " << value << endl;
		}
	}
	return 0;
}

