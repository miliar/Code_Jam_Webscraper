#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>

using namespace std;

typedef long long ll;

stringstream ss;

#define DEBUG(A) cerr << "\tDEBUG: " << #A << " = " << A << "\n"

double C, F, X;

double timeRemaining(double z) { // z = cookies per second
	double ret = 0;
	double a, b;
	while ( true ) {
		a = X/z;
		b = (C/z + X/(z+F));
		if ( b < a ) {
			ret+=C/z;
			z = z+F;
		} else {
			return a+ret;
		}
	}
}

void testCase() {
	cin >> C >> F >> X;
	double tr = timeRemaining(2);
	ss << fixed << setprecision(9) << tr;
}

int main() {
	int t;
	cin >> t;
	for ( int i = 0 ; i < t ; i++ ) {
		ss << "Case #" << (i+1) << ": ";
		testCase();
		ss << endl;
	}
	cout << ss.str();
	return 0;
}

