#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main() {
	int numTest;

	cin >> numTest;

	for (int i=0; i<numTest; i++) {
		int rowId, row2Id;
		std::set<int> row[4], row2[4];

		cin >> rowId;

		for (int j=0; j<4; j++) {
			int c1, c2, c3, c4;
			cin >> c1 >> c2 >> c3 >> c4;
			row[j].insert(c1);
			row[j].insert(c2);
			row[j].insert(c3);
			row[j].insert(c4);
		}

		cin >> row2Id;

		for (int j=0; j<4; j++) {
			int c1, c2, c3, c4;
			cin >> c1 >> c2 >> c3 >> c4;
			row2[j].insert(c1);
			row2[j].insert(c2);
			row2[j].insert(c3);
			row2[j].insert(c4);
		}

		std::set<int>::iterator it;
		std::set<int> s1 = row[rowId-1], s2 = row2[row2Id-1];

		std::set<int> intersect;
		std::set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),
			std::inserter(intersect,intersect.begin()));

		if (intersect.size() == 1) {
			printf("Case #%i: %i\n", i+1, *(intersect.begin()));
		} else if (intersect.size() > 1) {
			printf("Case #%i: Bad magician!\n", i+1);
		} else {
			printf("Case #%i: Volunteer cheated!\n", i+1);
		}
	}
}