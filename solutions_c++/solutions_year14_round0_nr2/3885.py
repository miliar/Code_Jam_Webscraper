//============================================================================
// Name        : CookieClickerAlpha.cpp
// Author      : Rumman
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, char ** argv) {
	freopen(argv[1], "r", stdin);
	int t;
	cin >> t;
	for(int ti=0; ti<t; ti++) {
		double c, f, x, r, t;
		t = 0.0;
		r = 2.0;
		cin >> c >> f >> x;

		while(x/r > c/r + x/(r+f)) {
			// build a farm
			t += c/r;
			r = r + f;
		}
		// no need to build a farm
		t += x/r;

		// Display output
		std::cout.precision(7);

		cout << fixed;
		cout << "Case #" << ti+1 << ": " << setprecision(7)<< t;
		cout << endl;
	}
	return 0;
}
