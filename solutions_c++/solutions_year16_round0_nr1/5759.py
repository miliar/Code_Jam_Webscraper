#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool hasTen(stringstream& s) {
	for (char c = '0'; c <= '9'; c++) {
		if (s.str().find(c) == string::npos) {
			return false;
		}
	}
	return true;
}

int main() {

	int x;
	int i = 1;
	stringstream numbers;
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> x;
		if (x == 0) {
			cout << "Case #" << i++ << ": INSOMNIA" << endl;
			continue;
		}
		int z = 1;
		numbers << x;
		cout << "Case #" << i++ << ": ";

		while (!hasTen(numbers)) {
			numbers << x*(++z);
		}

		cout << x*z << endl;
		z = 1;
		numbers.str("");
	}

	return 0;
}