#if 1
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

bool fair(int i) {
	stringstream ss;
	ss << i;
	string s = ss.str();
	string t = s;
	reverse(s.begin(), s.end());
	return t == s;
}

void solve(istream &in, ostream &out) {

	bitset<1001> fairs, fairAndSquares;

	for (int i = 1; i <= 1000; ++i)
		if (fair(i)) {
			fairs[i] = true;
			int square = i * i;
			if (square <= 1000)
				if (fair(square))
					fairAndSquares[square] = true;
		}

	int T;
	in >> T;

	for (int t = 1; t <= T; ++t) {
		int A, B;
		in >> A >> B;
		int c = 0;
		for (int i = A; i <= B; ++i)
			if (fairAndSquares[i])
				++c;

		out << "Case #" << t << ": " << c << endl;
	}
}

int main() {
	solve(cin, cout);
	return 0;
}
#endif
