#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");

	int T;
	in >> T;

	for (int i = 0; i < T; ++i) {
		int a1, a2;
		int g1[4][4], g2[4][4];

		in >> a1;
		--a1;
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				in >> g1[j][k];
			}
		}
		in >> a2;
		--a2;
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				in >> g2[j][k];
			}
		}

		vector<int> possible(4);
		sort(g1[a1], g1[a1] + 4);
		sort(g2[a2], g2[a2] + 4);
		auto it = set_intersection(g1[a1], g1[a1] + 4, g2[a2], g2[a2] + 4, possible.begin());
		possible.resize(it - possible.begin());

		out << "Case #" << i + 1 << ": ";
		if (!possible.size()) {
			out << "Volunteer cheated!" << endl;
		}
		else if (possible.size() == 1) {
			out << possible[0] << endl;
		}
		else {
			out << "Bad magician!" << endl;
		}
	}

	return 0;
}