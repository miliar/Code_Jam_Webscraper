#include <iostream>
#include <cstring>
#include <set>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int I = 1; I <= t; I++) {
		set<int> valid;
		for (int i = 1; i < 17; i++) {
			valid.insert(i);
		}
		for (int i = 0; i < 2; i++) {
			int row;
			cin >> row;
			for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 4; k++) {
					int v; cin >> v;
					if (j + 1 != row) {
						valid.erase(v);
					}
				}
			}
		}
		if (valid.size() == 1) {
			cout << "Case #" << I << ": " << *valid.begin() << endl;
		} else if (valid.size() == 0) {
			cout << "Case #" << I << ": Volunteer cheated!" << endl;
		} else {
			cout << "Case #" << I << ": Bad magician!" << endl;
		}
	}

	return 0;
}