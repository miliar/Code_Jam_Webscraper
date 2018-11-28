#include <iostream>
#include <set>
#include <vector>
using namespace std;

// Problem A. Magic Trick

int main () {
	int T;
	int answer;
	int card;
	vector<set<int>> row_arrangement(2, set<int>());
	set<int> same;
	set<int>::iterator it;

	cin >> T;
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << (i + 1) << ": ";
		same.clear();
		for (int round = 0; round < 2; ++round) {
			row_arrangement[round].clear();
			cin >> answer;
			--answer;
			for (int j = 0; j < 4; ++j) {
				for (int k = 0; k < 4; ++k) {
					cin >> card;
					if (j == answer) {
						row_arrangement[round].insert(card);
					}
				}
			}
		}
		for (it = row_arrangement[0].begin(); it != row_arrangement[0].end(); ++it) {
			if (row_arrangement[1].find(*it) != row_arrangement[1].end()) {
				same.insert(*it);
			}
		}
		if (same.size() == 1) {
			cout << *same.begin() << endl;
		} else if (same.size() > 1) {
			cout << "Bad magician!" << endl;
		} else {
			cout << "Volunteer cheated!" << endl;
		}
	}

	return 0;
}
