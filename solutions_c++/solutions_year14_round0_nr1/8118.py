#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>
using namespace std;

int main() {
	int nt, it;

	cin >> nt;

	for (it = 1; it <= nt; it++) {
		set<int> r[2], u;
		int i, ja, j, k, t;

		for (i = 0; i < 2; i++) {
			cin >> ja;
			for (j = 0; j < 4; j++) {
				for (k = 0; k < 4; k++) {
					cin >> t;
					if (j + 1 == ja) r[i].insert(t);
				}
			}
		}

		set_intersection(r[0].begin(), r[0].end(), r[1].begin(), r[1].end(), std::inserter(u, u.begin()));

		cout << "Case #" << it << ": ";
		if (u.size() == 1) {
			cout << *u.begin();
		} else if (u.size() > 1) {
			cout << "Bad magician!";
		} else {
			cout << "Volunteer cheated!";
		}
		cout << '\n';
	}
}
