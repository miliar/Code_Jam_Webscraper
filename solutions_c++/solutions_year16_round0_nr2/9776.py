#include<iostream>
using namespace std;

int decode(char *input) {
	int count = 0;
	char last = '+';
	for (int i = strlen(input) - 1; i >= 0; i--) {
		if (input[i] == last) {
			continue;
		}
		last = input[i];
		count++;
	}
	return count;
}

int main() {
	int T, maxlen = 0;
	int record[128];
	char input[128];
	
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> input;
		record[t] = decode(input);
	}

	for (int i = 0; i < T; i++) {
		cout << "case #" << i + 1 << ": " << record[i] << endl;
	}
	//system("pause");
	return 0;
}