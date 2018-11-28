#include <fstream>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	int T;
	in >> T;

	for (int x = 1; x <= T; x++) {
		int r = 0;
		int sm; in >> sm;
		string s; in >> s;
		int t = 0;
		for (int i = 0; i < s.size(); i++) {
			int c = s[i] - '0';
			if (i > t) r += i - t, t += i - t;
			t += c;
		}
		out << "Case #" << x << ": " << r << endl;
	}

	return 0;
}
