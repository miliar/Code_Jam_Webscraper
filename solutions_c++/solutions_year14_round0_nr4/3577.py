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
#include <fstream>
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

const double INC = 0.000001;

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
		int N;
		vector<double> naomi, ken;
		getline(cin,mystr);
		stringstream (mystr) >> N;
		REP(i,N){
			double tmp;
			cin >> tmp;
			naomi.push_back(tmp);
		}
		getline(cin,mystr); // get newline
		REP(i,N){
			double tmp;
			cin >> tmp;
			ken.push_back(tmp);
		}
		getline(cin,mystr); // get newline
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());
		///////////////////////////////////////////

		int DW=0, W=0;
		{ // declare devious scope
			vector<double>::iterator itk = ken.begin();
			vector<double>::reverse_iterator ritk = ken.rbegin();
			for(vector<double>::iterator it = naomi.begin(); it < naomi.end();++it){
				if (*it < *itk) {
					++ritk;
				}
				else {
					++itk;
					++DW;
				}
			}
		}
		// Determine regular war
		for(vector<double>::iterator it = naomi.begin(); it < naomi.end();++it){
			for(vector<double>::iterator itk = ken.begin(); itk < ken.end();++itk){
				if (*it < *itk){
					ken.erase(itk);
					break;
				}
			}
		}
		W = ken.size();

		cout << "Case #" << casenum + 1 << ": " << DW << " " << W << endl;
	}

	return 0;
}
