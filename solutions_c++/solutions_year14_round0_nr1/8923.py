#include <iostream>
#include <fstream>
using namespace std;

int main() {
//	cout << "start" << endl; // prints Hello World!

	ifstream in("input.txt");
	ofstream out("output.txt");


	int T;
	in >> T;

	int buff[4];
	int row1[4];
	int row2[4];
	int r1, r2;
	for (int x = 1; x <= T; x++) {
		in >> r1;
		//cout << "going" << endl;
		for (int r = 1; r <= 4; r++) {
			if (r != r1) {
				for (int i = 0; i < 4; i++) {
					in >> buff[i];
				}
			} else {
				for (int i = 0; i < 4; i++) {
					in >> row1[i];
				}
			}
		}

		in >> r2;
		for (int r = 1; r <= 4; r++) {
			if (r != r2) {
				for (int i = 0; i < 4; i++) {
					in >> buff[i];
				}
			} else {
				for (int i = 0; i < 4; i++) {
					in >> row2[i];
				}
			}
		}

		int coinc = 0;
		int ans = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (row1[i] == row2[j]) {
					coinc++;
					ans = row1[i];
				}
			}
		}

		out << "Case #" << x << ": ";
		if (coinc == 0) {
			out << "Volunteer cheated!" << endl;
		} else if (coinc > 1) {
			out << "Bad magician!" << endl;
		} else if (coinc == 1) {
			out << ans << endl;
		}
	}

	in.close();
	out.close();

//	cout << "finish" << endl;
	return 0;
}
