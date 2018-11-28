
#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main(void) {
	int cases;
	cin >> cases;
	cases++;
	for (int c=1; c < cases; c++) {
		set<int> row1;
		set<int> row2;
		set<int> intersection;
		int row;
		cin >> row;
		row--;
		for (int i=0; i < 4; i++) {
			for (int j=0; j < 4; j++) {
				int next;
				cin >> next;
				if (i == row) {
					row1.emplace(next);
				}
			}
		}
		cin >> row;
		row--;
		for (int i=0; i < 4; i++) {
			for (int j=0; j < 4; j++) {
				int next;
				cin >> next;
				if (i == row) {
					row2.emplace(next);
				}
			}
		}
		auto it = set_intersection(row1.begin(),row1.end(),row2.begin(),row2.end(),inserter(intersection,intersection.begin()));
		if (intersection.size() <= 0) {
			// cheater
			cout << "Case #" << c << ": " << "Volunteer cheated!" << endl;
		} else if (intersection.size() == 1) {
			// output it
			cout << "Case #" << c << ": " << *intersection.begin() << endl;
		} else {
			// bad magician
			cout << "Case #" << c << ": " << "Bad magician!" << endl;
		}
	}
	return 0;
}
