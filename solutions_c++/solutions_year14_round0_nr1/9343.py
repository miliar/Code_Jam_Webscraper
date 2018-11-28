#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int a, b;
		int x[16], y[16];
		cin >> a;
		for (int j = 0; j < 16; ++j) {
			cin >> x[j];
		}
		cin >> b;
		for (int j = 0; j < 16; ++j) {
			cin >> y[j];
		}
		int n = -1;
		bool done = false;
		for (int j = 0; j < 4 && !done; ++j) {
			for (int k = 0; k < 4 && !done; ++k) {
				if (x[j + (a - 1) * 4] == y[k + (b - 1) * 4]) {
					if (n == -1) {
						n =  y[k + (b - 1) * 4];
					} else {
						done = true;
					}
				}
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (done) {
			cout << "Bad magician!" << endl;
		} else if (n == -1) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << n << endl;
		} 
	}
	return 0;
}