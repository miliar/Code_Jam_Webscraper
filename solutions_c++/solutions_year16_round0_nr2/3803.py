#include <iostream>

using namespace std;

int main() {
	int cases;

	cin >> cases;

	for (int i = 1; i <= cases; i++) {
		//string pancakes;
		char pancakes[102];
		int flips[101][2] = { 0 }; // is this all zeroed?
		// 0 = '-' 1 = '+'

		// read stack
		cin >> pancakes;
		int len = strlen(pancakes);
		//char* pc = pancakes.c_str();

		//cout << "length " << len << endl;
		//cout << "end char " << (int)pancakes[len - 1] << endl;


		for (int j = 1; j <= len; j++) {
			if (pancakes[j - 1] == '+') {
				flips[j][0] = flips[j - 1][1] + 1;
				flips[j][1] = flips[j - 1][1];
			}
			else if (pancakes[j - 1] == '-') {
				flips[j][0] = flips[j - 1][0];
				flips[j][1] = flips[j - 1][0] + 1;
			}
			else {
				cout << "DANGER DANGER" << endl;
				exit(1);
			}
		}

		cout << "Case #" << i << ": " << flips[len][1] << endl;
	}


	return 0;
}