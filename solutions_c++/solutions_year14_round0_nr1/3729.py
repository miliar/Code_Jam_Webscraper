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
		int r1[4], r2[4];
		int a, match, matches=0;
		getline(cin, mystr);
		stringstream(mystr) >> a;
		REP(i,4){
			getline(cin, mystr);
			if (a == i+1){
				stringstream(mystr) >> r1[0] >> r1[1] >> r1[2] >> r1[3];
			}
		}
		getline(cin, mystr);
		stringstream(mystr) >> a;
		REP(i,4){
			getline(cin,mystr);
			if (a == i+1){
				stringstream(mystr) >> r2[0] >> r2[1] >> r2[2] >> r2[3];
				REP(j,4){
					REP(k,4){
						if (r2[j] == r1[k]){
							match = r2[j];
							++matches;
						}
					}
				}
			}
		}
		///////////////////////////////////////////
		string result = " ";
		if (0 == matches)
			result += "Volunteer cheated!";
		else if (1 == matches){
			ostringstream tmp;
			tmp << match;
			result += tmp.str();
		}
		else
			result += "Bad magician!";

		cout << "Case #" << casenum + 1 << ":" << result << endl;
	}

	return 0;
}
