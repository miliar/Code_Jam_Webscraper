#include <iostream>
#include <set>

using namespace std;

int main() {
	int t;
	cin >> t;

	int table[4][4];

	for (int test = 0; test < t; test++) {
		set<int> firstNums, secondNums;

		for (int k = 0; k < 2; k++) {

			int row;
			cin >> row;
			row--;

			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					cin >> table[i][j];
				}
			}

			for (int i = 0; i < 4; i++) {
				(k ? secondNums : firstNums).insert(table[row][i]);
			}

		}	

		set<int> intersection;
		for (set<int>::iterator i = firstNums.begin(); i != firstNums.end(); i++) {
			if (secondNums.count(*i)) {
				intersection.insert(*i);
			}
		}

		cout << "Case #" << test + 1 << ": ";

		if (intersection.size() > 1) {
			cout << "Bad magician!";
		} else if (intersection.size() == 0) {
			cout << "Volunteer cheated!";
		} else {
			cout << *(intersection.begin());
		}

		cout << endl;
	}
}