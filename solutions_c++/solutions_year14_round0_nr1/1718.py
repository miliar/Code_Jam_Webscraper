#include <iostream>

using namespace std;

int main() {
	int T; cin >> T;
	for (int t = 0; t < T; ++t) {
		int r1, r2;
		int data1[4];
		int data2[4];
		cin >> r1;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				int tmp; cin >> tmp;
				if (r1 - 1 == i) {
					data1[j] = tmp;
				}
			}
		}
		cin >> r2;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				int tmp; cin >> tmp;
				if (r2 - 1 == i) {
					data2[j] = tmp;
				}
			}
		}
		int ans = 0;
		int ret = 0;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (data1[i] == data2[j]) {
					ans++;
					ret = data1[i];
				}
			}
		}
		if (ans == 0) {
			cout << "Case #" << t + 1 << ": Volunteer cheated!" << endl;
		}
		else if (ans == 1) {
			cout << "Case #" << t + 1 << ": " << ret << endl;
		}
		else {
			cout << "Case #" << t + 1 << ": Bad magician!" << endl;
		}
	}
}