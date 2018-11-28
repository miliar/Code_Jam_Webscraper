#include <iostream>
#include <string>

using namespace std;

int main() {
	int t, T;
	string str;
	int count[26] = {0};
	int num[10] = {0};

	cin >> T;
	t = 1;

	while (t <= T) {
		// clear
		for (int i = 0; i < 26; i ++) {
			count[i] = 0;
		}
		for (int i = 0; i < 10; i ++) {
			num[i] = 0;
		}

		// input
		cin >> str;

		// handle
		for (int i = 0; i < str.size(); i ++) {
			count[str[i] - 'A'] ++;
		}
		while (count['Z' - 'A'] > 0) {
			num[0] ++;
			count['Z' - 'A'] --;
			count['E' - 'A'] --;
			count['R' - 'A'] --;
			count['O' - 'A'] --;
		}
		while (count['X' - 'A'] > 0) {
			num[6] ++;
			count['S' - 'A'] --;
			count['I' - 'A'] --;
			count['X' - 'A'] --;
		}
		while (count['W' - 'A'] > 0) {
			num[2] ++;
			count['T' - 'A'] --;
			count['W' - 'A'] --;
			count['O' - 'A'] --;
		}
		while (count['U' - 'A'] > 0) {
			num[4] ++;
			count['F' - 'A'] --;
			count['O' - 'A'] --;
			count['U' - 'A'] --;
			count['R' - 'A'] --;
		}
		while (count['R' - 'A'] > 0) {
			num[3] ++;
			count['T' - 'A'] --;
			count['H' - 'A'] --;
			count['R' - 'A'] --;
			count['E' - 'A'] --;
			count['E' - 'A'] --;
		}
		while (count['S' - 'A'] > 0) {
			num[7] ++;
			count['S' - 'A'] --;
			count['E' - 'A'] --;
			count['V' - 'A'] --;
			count['E' - 'A'] --;
			count['N' - 'A'] --;
		}
		while (count['V' - 'A'] > 0) {
			num[5] ++;
			count['F' - 'A'] --;
			count['I' - 'A'] --;
			count['V' - 'A'] --;
			count['E' - 'A'] --;
		}
		while (count['O' - 'A'] > 0) {
			num[1] ++;
			count['O' - 'A'] --;
			count['N' - 'A'] --;
			count['E' - 'A'] --;
		}
		while (count['N' - 'A'] > 0) {
			num[9] ++;
			count['N' - 'A'] --;
			count['I' - 'A'] --;
			count['N' - 'A'] --;
			count['E' - 'A'] --;
		}
		while (count['I' - 'A'] > 0) {
			num[8] ++;
			count['E' - 'A'] --;
			count['I' - 'A'] --;
			count['G' - 'A'] --;
			count['H' - 'A'] --;
			count['T' - 'A'] --;
		}

		// output
		cout << "Case #" << t++ << ": ";
		for (int i = 0; i < 10; i ++) {
			for (int j = 0; j < num[i]; j ++) {
				cout << i;
			}
		}
		cout << endl;
	}
	return 0;
}
