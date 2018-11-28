#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ofstream myfile("D-small-attempt1.txt");
	ifstream target("D-small-attempt1.in");
	int T;
	int K, C, S;
	target >> T;
	for (int i = 1; i <= T; i++) {
		target >> K >> C >> S;
		cout << K << ' ' << C << ' ' << S << endl;
		if (C == 1) {
			if (K > S) {
				myfile << "Case #" << i << ": IMPOSSIBLE" << endl;
				continue;
			} else if (K == S) {
				myfile << "Case #" << i << ": ";
				for (int temp = 1; temp < K; temp++) {
					myfile << temp << ' ';
				}
				myfile << K << endl;
				continue;
			}
		} else {
			if (K == S) {
				myfile << "Case #" << i << ": ";
				for (int temp = 1; temp < K; temp++)
					myfile << temp << ' ';
				myfile << K << endl;
			} else {
				int ele = K * K;
				bool odd = false;
				if (K % 2 == 1) {
					K += 1;
					odd = true;
				}
				if (K/2 > S) {
					cout << "Case #" << i << ": IMPOSSIBLE" << endl;
					continue;
				} else {
					cout << "Case #" << i << ": ";
					int offset = 2, mult = 0;
					for (int temp = 1; temp < K / 2; temp++) {
						cout << mult * K + offset << ' ';
						mult += 2;
						offset += 2;
					}
					if (!odd)
						cout << mult * K + offset - 1 << endl;
					else
						cout << mult * K + offset << endl;
				}
			}
		}
	}
	return 0;
}
/*
		} else if (S + 1 < K) {
			myfile << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
			continue;
		}

		myfile << "Case #" << i + 1 << ": ";
		for (int j = 2; j <= K; j++) {
			myfile << j << ' ';
		}
		myfile << endl;
	}
	return 0;
} */
