#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;
typedef unsigned long long uint64;

int main (int argc, char *argv[]) {
	
	size_t T, count = 1;
	string line;
	
	// get T
	getline(cin, line);
	stringstream(line) >> T;

	// Helpful variables
	long double C, F, X;
	long double t;
	long double R;

	// get all cases and process it
	for(size_t count = 1; count <= T; count++) {
		// get N, M
		getline(cin, line);
		stringstream(line) >> C >> F >> X;
		
		// init case
		t = 0;
		R = 2;

		while (1) {
			if ((C/R + X/(R+F)) < (X/R)) {
				t += C/R;
				R += F;
			} else {
				t += X/R;
				break;
			}
		}
		
		// print output
		cout.precision(12);
		cout << "Case #" << count << ": " << t;
		cout << endl;
		
		//cout << "===========" << endl;
	}
	
	return 0;
}