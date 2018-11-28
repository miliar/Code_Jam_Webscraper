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
		double C,F,X;
		getline (cin, mystr);
		stringstream(mystr) >> C >> F >> X;
		///////////////////////////////////////////
		double ii = 1.0, R = 2.0; // Base Rate
		double t = C / R, result = X / R;
		while (1){
			double T,  // T - total time;
					tF; // tF - time to Farm
			T = t + X / (R + ii*F);
			tF = C / (R + ii*F);
			t += tF;
			if (result < T){
				break;
			}
			else {
				result = T;
				++ii;
			}
		}


		cout << "Case #" << casenum + 1 << ": " << setprecision(7) << fixed << result << endl;
	}

	return 0;
}
