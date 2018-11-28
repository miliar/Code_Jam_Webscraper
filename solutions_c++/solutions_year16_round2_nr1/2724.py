#include <iostream>
#include <cstring>

using namespace std;

int intInput[9] = {0};
int result[10] = {0};

void resetData() {
	for (int i = 0; i < 9 ; i++)
		intInput[i] = 0;
	for (int i = 0; i < 10 ; i++)
		result[i] = 0;
}

int main() {
	int test_case = 0;
	cin >> test_case;
	
	string input = "";
	int charCount = 0;
	
	
	for (int i = 1; i <= test_case; i++) {
		input.clear();
		resetData();
		cin >> input;
		
		for (int j = 0; j < input.length(); j ++) {
			// ZERO Z
			if (input[j] == 'Z') intInput[0]++;
			// ONE O
			if (input[j] == 'O') intInput[1]++;
			// TWO W
			if (input[j] == 'W') intInput[2]++;
			// THREE R
			if (input[j] == 'R') intInput[3]++;
			// FOUR U
			if (input[j] == 'U') intInput[4]++;
			// FIVE F
			if (input[j] == 'F') intInput[5]++;
			// SIX X
			if (input[j] == 'X') intInput[6]++;
			// SEVEN S
			if (input[j] == 'S') intInput[7]++;
			// EIGHT G
			if (input[j] == 'G') intInput[8]++;
		}
		
		// 0
		result[0] = intInput[0]; intInput[1] -= result[0]; intInput[3] -= result[0];
		// 2
		result[2] = intInput[2]; intInput[1] -= result[2];
		// 4
		result[4] = intInput[4]; intInput[1] -= result[4]; intInput[3] -= result[4]; intInput[5] -= result[4];
		// 6
		result[6] = intInput[6]; intInput[7] -= result[6];
		// 8
		result[8] = intInput[8];
		result[1] = intInput[1];
		result[3] = intInput[3];
		result[5] = intInput[5];
		result[7] = intInput[7];
		charCount = (result[1] + result[2] + result[6]) * 3 + (result[0] + result[4] + result[5]) * 4 + (result[3] + result[7] + result[8]) * 5;
		result[9] = (input.length() - charCount) / 4;
		
		cout << "Case #" << i << ": ";
		for (int j = 0; j < 10; j++) {
			for (int z = 0; z < result[j]; z++) {
				cout << j;
			}
		}
		cout << endl;
	}
	
	return 0;
}
