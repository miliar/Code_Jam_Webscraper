#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int n;
	ifstream in("A--small-attempt0.in");
	cin.rdbuf(in.rdbuf());
	ofstream out("result.out");
	cout.rdbuf(out.rdbuf());
	cin >> n;
	for (int i = 0; i < n; i++) {
		int in1[4], in2[4];
		int r1, r2;
		int final;
		bool found = false;
		bool doubleFound = false;
		int tmp;
		int j = 0;
		cin >> r1;
		for (; j < (r1 - 1) * 4; j++) {
			cin >> tmp;
		}
		for (; j < r1 * 4; j++) {
			cin >> in1[j % 4];
		}
		for (;j < 16; j++) {
			cin >> tmp;
		}
		cin >> r2;
		for (j = 0; j < (r2 - 1) * 4; j++) {
			cin >> tmp;
		}
		for (; j < r2 * 4; j++) {
			cin >> in2[j % 4];
		}
		for (;j < 16; j++) {
			cin >> tmp;
		}
		for (j = 0; j < 4 && !doubleFound; j++) {
			for (int k = 0; k < 4; k++) {
				if (in2[k] == in1[j]) {
					if (found) {
						doubleFound = true;
					} else {
						final = in2[k];
						found = true;
					}
					break;
				}
			}
		}
		
		if (doubleFound) {
			cout << "Case #" << i + 1 << ": Bad magician!" << endl;
		} else if (found) {
			cout << "Case #" << i + 1 << ": " << final << endl;
		} else {
			cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
		}
	}
	return 0;
}
