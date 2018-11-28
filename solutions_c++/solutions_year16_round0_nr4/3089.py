#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int numberOfCases;
	cin >> numberOfCases;
	for (int i = 1; i <= numberOfCases; i++) {
		int initial, students;
		int dump;
		cin >> initial >> dump;
		cin >> students;
		cout << "Case #" << i << ":";
			if (students < initial) {
			cout << " IMPOSSIBLE" << endl;
			}
			else {
				for (int k = 1; k <= initial; k++) {
					cout << " " << k;
				}
				cout << endl;
			}
	}

}