/*
 * main.cc
 *
 *  Created on: 26 Apr 2013
 *      Author: shuss
 *
 *  Compiler:
 *  	Minimalist GNU for Windows (MinGW)
 *  	www.mingw.org
 *  	"MinGW provides a complete Open Source programming tool set ..."
 */

// STL
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
// Data Structures
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
// Math
#include <cmath>
#include <algorithm>
using namespace std;

#define PI 3.1415926535897932384626433832795
#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define DREP(i,n) for (int i((n)-1); i >= 0; --i)

int main() {
	int ncases;
	string mystr;
	getline(cin, mystr);
	stringstream(mystr) >> ncases;

	REP (casenum,ncases) {
		///////////////////////////////////////////
		// Input
		long long r,t;
		cin >> r >> t;
		///////////////////////////////////////////
		// 1st case
		int result=0;
		long long a = 0;

		do {
			a += 2*r+1;
			r+=2;
			//cout << "a r: " << a << " " << r << endl;
			++result;
		} while (a <= t);

		cout << "Case #" << casenum + 1 << ": " << result-1 << endl;
	}

	return 0;
}
