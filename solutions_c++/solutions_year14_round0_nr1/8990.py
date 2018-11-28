#include <iostream>

using namespace std;

void input(int arr[][4], int size);
int check(int arr1[][4], int hint1, int arr2[][4], int hint2, int size);
void print_answer(int flag, int case_num);

int main() {
	int T;	// Test case
	const int SIZE = 4;
	int arr1[SIZE][SIZE];
	int arr2[SIZE][SIZE];
	int hint_row1, hint_row2;
	int flag; // 2: incorrect, 3:cheated, otherwise: correct number

	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> hint_row1;
		input(arr1, SIZE);
		cin >> hint_row2;
		input(arr2, SIZE);
		flag = check(arr1, hint_row1-1, arr2, hint_row2-1, SIZE);
		print_answer(flag, i);
	}
}

void input(int arr[][4], int size) {
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			cin >> arr[i][j];
		}
	}
}

int check(int arr1[][4], int hint1, int arr2[][4], int hint2, int size) {
	int count = 0;
	int answer;

	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			if (arr1[hint1][i] == arr2[hint2][j]) {
				count++;
				if (count == 1) {
					answer = arr2[hint2][j];
				}
			}
		}
	}
	
	if (count == 1) {
		return answer;
	}
	else if (count >= 2) {
		return -1;
	}
	else {
		return -2;
	}
}

void print_answer(int flag, int case_num) {
	cout << "Case #" << case_num << ": ";
	if (flag == -1) {
		cout << "Bad magician!" << endl;
	}
	else if (flag == -2) {
		cout << "Volunteer cheated!" << endl;
	}
	else {
		cout << flag << endl;
	}
}
