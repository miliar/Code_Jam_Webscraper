#include <iostream>

using namespace std;

int main() {

	int cases; cin >> cases >> ws;

	for (int c = 0; c < cases; c++) {
		int original;
		int complexity;
		int clean;
		cin >> original >> complexity >> clean >> ws;

		//SMALL CASE
		cout << "Case #" << (c+1) << ":";

		if (original ==1) {
			cout << " " << "1\n";
		}
		else if (complexity == 1) {
			for (int i = 1; i <= original; i++) {
				cout << " " << i;
			}	
			cout << "\n";
		}
		else {
			for (int i = 2; i <= original; i++) {
				cout << " " << i;
			}
			cout << "\n";
		}
		

	}

	return 0;
}
