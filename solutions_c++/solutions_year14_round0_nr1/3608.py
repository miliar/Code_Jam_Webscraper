#include <iostream>
#include <vector>

using namespace std;

int res(vector<int> &a, vector<int> &b) {
	int r = 0;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if (a[i] == b[j]) {
				if (r == 0) r = a[i];
				else return -1;
			}
		}
	}

	return r;
}

int main() {
	int T;
	cin >> T;
	for (int cn = 1; cn <= T; ++cn) {
		int i1;
		cin >> i1;
		vector<int> arr1(4);
		for (int i = 1; i <= 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (i == i1) {
					cin >> arr1[j];
				}
				else {
					int nn;
					cin >> nn;
				}
			}
		}

		int i2;
		cin >> i2;
		vector<int> arr2(4);
		for (int i = 1; i <= 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (i == i2) {
					cin >> arr2[j];
				}
				else {
					int nn;
					cin >> nn;
				}
			}
		}

		int r = res(arr1, arr2);
		cout << "Case #" << cn << ": ";
		if (r > 0) cout << r;
		else cout << ((r == 0) ? "Volunteer cheated!" : "Bad magician!");
		cout << endl;
	}
}