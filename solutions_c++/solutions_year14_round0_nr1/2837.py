#include <iostream>
#include <string>

using namespace std;

void GetData(int *answer, int *arrange) {
	cin >> *answer;
	int _;

	for (int j = 0; j < (*answer - 1) * 4 ; j++) {
		cin >> _;
	}
	for (int j = 0; j < 4; j++) {
		cin >> *(arrange + j);
	}
	for (int j = *answer * 4; j < 16; j++) {
		cin >> _;
	}
}

bool find(int arrange[4], int toFind) {
	for (int i = 0; i < 4; i++) {
		if (arrange[i] == toFind) {
			return true;
		}
	}
	return false;
}

void HandleCase(int caseCount) {
	for (int i = 1; i <= caseCount; i++) {
		int answer1 = 0, answer2 = 0;
		int arrange1[4] = {0};
		int arrange2[4] = {0};
		GetData(&answer1, arrange1);
		GetData(&answer2, arrange2);
		int existCount = 0;
		int star = 0;
		for (int j = 0; j < 4; j++) {
			if (find(arrange2, arrange1[j])) {
				existCount++;
				star = arrange1[j];
			}
		}
		if (existCount == 1) {
			cout << "Case #" << i << ": " << star <<endl;
		} else {
			string out;
			if (existCount == 0) {
				out = "Volunteer cheated!";
			} else {
				out = "Bad magician!";
			} 
			cout << "Case #" << i << ": " << out <<endl;
		}
	}
}

int main() {
	int caseCount = 0;
	cin >> caseCount;
	HandleCase(caseCount);
}
