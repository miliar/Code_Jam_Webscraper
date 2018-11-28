#include <iostream>

using namespace std;
int m1[4][4];
int m2[4][4];
int r1;
int r2;

int magic(int* a, int* b) {
	int cnt = 0;
	int matched = -1;
	for(int i = 0 ; i < 4 ; i++) {
		for (int j = 0 ; j < 4 ; j++) {
		//cout << a[i] << " " << b[j] << endl;
			if (a[i] == b[j]) {
				matched = a[i];
				cnt++;
			}
		}
	}
	if (cnt == 1) {
		return matched;
	}
	if (cnt == 0) {
		return 0;
	}
	return -1;
}

int main() {
	int T;
	cin >> T;

	for (int t = 1 ; t <= T ; t++) {
		cin >> r1;
		for (int i = 0 ; i < 4 ; i++) {
			for (int j = 0 ; j < 4 ; j++) {
				cin >> m1[i][j];
			}
		}
		cin >> r2;
		for (int i = 0 ; i < 4 ; i++) {
			for (int j = 0 ; j < 4 ; j++) {
				cin >> m2[i][j];
			}
		}
		int res = magic(&m1[r1-1][0], &m2[r2-1][0]);
		//cout << res << endl;
		if (res > 0) {
			cout << "Case #" << t << ": " << res << endl;
		}  else {
			const char* str = (res == 0) ? ("Volunteer cheated!") : (res < 0 ? ("Bad magician!") : (""));
			cout << "Case #" << t << ": " << str << endl;
		}
	}
}
