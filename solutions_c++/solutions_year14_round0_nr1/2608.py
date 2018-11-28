#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
		int row1; cin >> row1; --row1;
		vector<vector<int> > table1(4,vector<int>(4,0));
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> table1[i][j];
			}
		}
		int row2; cin >> row2; --row2;
		vector<vector<int> > table2(4,vector<int>(4,0));
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> table2[i][j];
			}
		}

		vector<bool> contained(17,false);
		for (int i = 0; i < 4; ++i) {
			contained[table1[row1][i]] = true;
		}

		int found = 0;
		int value;

		for (int i = 0; i < 4; ++i) {
			if (contained[table2[row2][i]]) {
				++found;
				value = table2[row2][i];
			}
		}

		cout << "Case #" << t << ": ";
		if (found == 1) {
			cout << value;	
		} else {
			cout << (found == 0 ? "Volunteer cheated!" : "Bad magician!");
		}
		cout << endl;
    }
}
