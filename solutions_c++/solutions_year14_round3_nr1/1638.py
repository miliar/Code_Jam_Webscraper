#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <memory>
#include <numeric>

typedef int64_t INT;
typedef uint64_t UINT;

using namespace std;

UINT np2(UINT b) {
	UINT c = b;
	--c;
	c |= c >> 1;
	c |= c >> 2;
	c |= c >> 4;
	c |= c >> 8;
	c |= c >> 16;
	c |= c >> 32;
	++c;
	if (c == b) return b << 1;
	return c;
}

UINT gcd(UINT a, UINT b) {
	if (b < a) swap(a, b);
	if (a == 0) return b;
	if (a == 1) return 1;
	return gcd(b%a, a);
}

int solve(UINT P, UINT Q) {
	if (P >= Q/2) return 1;
	UINT nP = np2(P);
	return 1 + solve(1, Q / nP);
}

int main(int argc, char* argv[])
{
	ifstream input("C:/users/sebastien/Downloads/A-small-attempt0.in");
	//ifstream input("C:/users/sebastien/Downloads/example.in");
	ofstream output("C:/users/sebastien/Downloads/output.txt");

	output.precision(10);

	int T;
	input >> T;

	for (int test = 1; test <= T; ++test) {
		cout << "test " << test << "\n";
		output << "Case #" << test << ": ";

		string str;
		input >> str;
		UINT P, Q;
		int idx = str.find_first_of("/");
		P = atoi(str.substr(0, idx).c_str());
		Q = atoi(str.substr(idx+1, string::npos).c_str());
		cout << "P " << P << " Q " << Q << "\n";
		UINT d = gcd(P, Q);
		P /= d;
		Q /= d;
		if (Q != np2(Q) / 2 || Q > (UINT(1) << 40)) {
			output << "impossible";
		}
		else {
			output << solve(P, Q);
		}

		output << "\n";
	}
	output.close();

	{
		cout << "DONE\n";
		int _;
		cin >> _;
	}

	return 0;
}
