#include <fstream>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small.out");

	int T;
	in >> T;

	for (int x = 1; x <= T; x++) {
		int r1; int m1[4][4];
		in >> r1;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) in >> m1[i][j];

		int r2; int m2[4][4];
		in >> r2;
		for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) in >> m2[i][j];

		set<int> s1; for (int i = 0; i < 4; i++) s1.insert(m1[r1 - 1][i]);
		set<int> s2; for (int i = 0; i < 4; i++) s2.insert(m2[r2 - 1][i]);

		vector<int> v(8);
		vector<int>::iterator it = set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), v.begin());

		v.resize(it - v.begin());

		if (v.size() == 1) {
			out << "Case #" << x << ": " << v[0] << endl;
		} else if (v.size() == 0) {
			out << "Case #" << x << ": Volunteer cheated!" << endl;
		} else {
			out << "Case #" << x << ": Bad magician!" << endl;
		}
	}

	return 0;
}
