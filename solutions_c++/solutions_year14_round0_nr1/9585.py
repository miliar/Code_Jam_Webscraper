#include <iostream>
#include <set>

using namespace std;

int main() {
	int numCases;
	cin >> numCases;
	int cnt = 0;
	while (numCases --> 0) {
		cnt++;
		cout << "Case #" << cnt << ": ";
		set<int> vals;
		int row, tmp;
		cin >> row;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> tmp;
				if (row - 1 != i) continue;
				vals.insert(tmp);
			}
		}
		cin >> row;
		int res = -1;
		int nRes = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> tmp;
				if (row - 1 != i) continue;
				if (vals.count(tmp)) {
					nRes++;
					res = tmp;
				}
			}
		}
		if (nRes == 0) {
			cout << "Volunteer cheated!" << endl;
		} else if (nRes == 1) {
			cout << res << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}

