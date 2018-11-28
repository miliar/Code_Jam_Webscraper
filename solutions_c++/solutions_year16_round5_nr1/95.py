#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <istream>
#include <map>
#include <numeric>
#include <ostream>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>


using namespace std;


// Powered by caide (code generator, tester, and library code inliner)

// variable definition here

string s;
int n;
void initialize(std::istream &in) {
	// initialize variables here
	in >> s;
	n = s.length();
}

void solve_case(std::ostream &out) {
	// solve the case here
	int ediff = 0, odiff = 0;
	for (int i = 0; i < n; i += 2) {
		if (s[i] == 'C')
			ediff++;
	}
	for (int i = 1; i < n; i += 2) {
		if (s[i] == 'C')
			odiff++;
	}
	out << 5 * (n - abs(ediff - odiff)) << endl;
}

void solve(std::istream& in, std::ostream& out) {
    out << std::setprecision(12);

	int T;
	in >> T;
	for (int t = 1; t <= T; t++) {
		cerr << "Case #" << t << " running" << endl;

		initialize(in);
		out << "Case #" << t << ": ";
		solve_case(out);

		cerr << "Case #" << t << " done" << endl;
	}
}


#include <fstream>


int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);


    istream& in = cin;


    ostream& out = cout;

    solve(in, out);
    return 0;
}


