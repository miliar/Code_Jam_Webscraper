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

void absorb(vector<long long> &motes, long long &A){
	while (motes.size() && A > *motes.begin()){
		A += *motes.begin();
		motes.erase(motes.begin());
	}
}

int numMoves(long long num,long long &newA){
	int moves = 0;
	while(newA <= num){
		newA += newA-1;
		++moves;
	}
	return moves;
}

int main() {
	int ncases;
	string mystr;
	getline(cin, mystr);
	stringstream(mystr) >> ncases;

	REP (casenum,ncases) {
		///////////////////////////////////////////
		// Input
		long long A;
		int N;
		cin >> A >> N;
		vector<long long> motes;
		REP(i,N){
			long long tmp;
			cin >> tmp;
			motes.push_back(tmp);
		}
		///////////////////////////////////////////
		sort (motes.begin(), motes.end());
		long long result=0;
		while(motes.size()){
			absorb(motes,A);
			if(motes.size() == 0){
				break;
			}
			if(A == 1){
				result += motes.size();
				break;
			}
			long long newA = A;
			unsigned int NumMovesToAbsorb = numMoves(*motes.begin(),newA);
			if (NumMovesToAbsorb < motes.size()){
				result += NumMovesToAbsorb;
				A=newA;
				continue;
			}
			else{
				result += motes.size();
				break;
			}
		}

		cout << "Case #" << casenum + 1 << ": " << result << endl;
	}

	return 0;
}
