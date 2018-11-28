#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <unordered_map>
#include <vector>
#include <set>
#include <unordered_set>
#include <cmath>
#include <list>
#include <boost/format.hpp>

// =================== SOME USEFULL DEFINES ======================================
#define fi first
#define se second
#define FOR(i, n) for(int i = 0; i < (n); ++i)
#define FoR(i, a, b) for(int i = (a); i < (b); ++i)
#define sqr(x) ((x)*(x))
#define pow2(x) (1 << (x))
#define btw(x, a, b) ((a <= x) && (x <= b))
#define hmap unordered_map
#define hset unordered_set
#define ll long long
#define ull unsigned long long
#define ld long double
// ===============================================================================

using namespace std;

istream& ioIN(int argc, const char **argv);
ostream& ioOUT(int argc, const char **argv);

bool cons(char c) {
	return (c != 'a') && (c != 'e') && (c != 'i') && (c != 'o') && (c != 'u');
}

int main(int argc, const char **argv) {
	istream &in = ioIN(argc, argv);
	ostream &out = ioOUT(argc, argv);

	int T;

	in >> T; //in.ignore();

	set<char> vvv;
	for (int tt = 1; tt <= T; ++tt) {
		string s;
		int n;

		in >> s >> n;

		vector<int> a(s.size() + 1);
		a[0] = 0;
		FOR (i, (int) s.size()) {
			a[i + 1] = a[i];
			if (cons(s[i])) a[i + 1]++;
		}

		int last = n - 1;
		int count = 0;
		FoR(i, n, (int) s.size() + 1) {
			if (a[i] - a[i - n] >= n) {
				int left = min(i - last, i - n + 1);
				int right = s.size() - i + 1;
				last = i;
				count += left * right;
			}
		}

		out << "Case #" << tt << ": " << count << endl;
	}

	return 0;
}

// ===============================================================================

istream& ioIN(int argc, const char **argv) {
	if (argc > 1)
		return *(new ifstream(argv[1]));
	return cin;
}

ostream& ioOUT(int argc, const char **argv) {
	if (argc > 2)
		return *(new ofstream(argv[2]));
	return cout;
}
