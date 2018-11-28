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

int main() {
	int ncases;
	string mystr;
	getline(cin, mystr);
	stringstream(mystr) >> ncases;

	REP (casenum,ncases) {
		///////////////////////////////////////////
		// Input
		int N, M;
		cin >> N >> M;
		vector<vector<int> > grid;
		vector<int> rowMax(N,0);
		vector<int> colMax(M,0);
		REP(i,N){
			vector<int> tmpv;
			REP(j,M){
				int tmp;
				cin >> tmp;
				tmpv.push_back(tmp);
				rowMax[i] = max(rowMax[i],tmp);
				colMax[j] = max(colMax[j],tmp);
			}
			grid.push_back(tmpv);
		}
		///////////////////////////////////////////
		string result = "YES";
		REP(i,N){
			REP(j,M){
				if (rowMax[i] > grid.at(i).at(j) && colMax[j] > grid.at(i).at(j)){
					result = "NO";
					break;
				}
			}
			if(result == "NO")
				break;
		}

		cout << "Case #" << casenum + 1 << ": " << result << endl;
	}

	return 0;
}
