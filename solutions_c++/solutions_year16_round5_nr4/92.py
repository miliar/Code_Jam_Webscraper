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
int n, l;
char str[128][128];
char no[128];

void initialize(std::istream &in) {
	// initialize variables here
	in >> n >> l;
	for (int i = 0; i < n; i++)
		in >> str[i];
	in >> no;
}

void solve_case(std::ostream &out) {
	// solve the case here
	for (int i = 0; no[i]; i++)
		assert(no[i] == '1');

	bool impossible = false;
	for (int i = 0; i < n; i++)
		if (strcmp(str[i], no) == 0)
			impossible = true;

	if (impossible) {
		out << "IMPOSSIBLE" << endl;
	}
	else {
		for (int i = 0; i < l; i++)
			out << "0?";
		out << " ";
		if (l > 1) {
			for (int i = 0; i < l - 1; i++)
				out << "1";
		}
		else {
			out << "0";
		}
		out << endl;
	}
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


