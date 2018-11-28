#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <fstream>

using namespace std;

int main() {

	freopen("test.txt", "rt", stdin);
	freopen("A-small-attempt0.in.out", "wt", stdout);
	int tc = 0, arr1[4][4], arr2[4][4], q1 = 0, q2 = 0, Case = 1;

	cin >> tc;

	while (tc--) {

		cin >> q1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> arr1[i][j];
			}
		}
		cin >> q2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> arr2[i][j];
			}
		}
		int match = 0, ret = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (arr1[q1 - 1][i] == arr2[q2 - 1][j]) {
					match++;
					ret = arr1[q1 - 1][i];
				}
			}
		}
		cout << "Case #" << Case++ << ": ";
		if (match == 1) {
			cout << ret;
		} else if (match > 1) {
			cout << "Bad magician!";
		} else {
			cout << "Volunteer cheated!";
		}
		cout << endl;
	}

	return 0;
}
//By : mohamed waleed
