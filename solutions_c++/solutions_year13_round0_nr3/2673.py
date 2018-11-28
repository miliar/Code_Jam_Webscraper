/*
 * main.cc
 *
 *  Created on: 12 Apr 2013
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
#include <set>
#include <map>
#include <stack>
// Math
#include <cmath>
#include <algorithm>
using namespace std;

#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define DREP(i,n) for (int i((n)-1); i >= 0; --i)

bool palindrome(long long num) {
	stringstream tmp;
	tmp << num;
	string snum = tmp.str();
	REP(i,snum.size()) {
		if (snum.at(i) != snum.at(snum.size() - 1 - i)) {
			return false;
		}
	}
	return true;
}

int main() {
	int ncases;
	string mystr;
	getline(cin, mystr);
	stringstream(mystr) >> ncases;

	REP (casenum,ncases) {
		///////////////////////////////////////////
		// Input
		string Astr, Bstr;
		cin >> Astr >> Bstr;
		///////////////////////////////////////////
		int result = 0;
		// short and 1st long only :(
		long long A, B;
		stringstream(Astr) >> A;
		stringstream(Bstr) >> B;
		long long Asqrt = (long long) ceil(sqrt((double) A));
		long long Bsqrt = (long long) sqrt((double) B);

		for (long long i = Asqrt; i <= Bsqrt; ++i) {
			if (palindrome(i) && palindrome(i * i)) {
				result++;
			}
		}

		cout << "Case #" << casenum + 1 << ": " << result << endl;
	}

	return 0;
}
