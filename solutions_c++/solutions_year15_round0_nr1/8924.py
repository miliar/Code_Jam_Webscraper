//============================================================================
// Name        : StandingOvation.cpp
// Author      : Xuanchen Tang
// Version     :
// Copyright   : 
// Description : Google Code Jam, Qualification Round 2015, Problem A. Standing Ovation
//============================================================================

#include <iostream>
#include <string>
using namespace std;

int main() {
	int caseNumber;
	cin >> caseNumber;

	int Smax;
	string S;
	int friends;
	int audiences;
	for (int i = 0; i < caseNumber; ++i) {
		friends = 0;
		audiences = 0;
		cin >> Smax >> S;
		for (int j = 0; j <= Smax; ++j) {
			if (audiences < j) {
				++friends;
				++audiences;
			}
			audiences += S[j] - '0';
		}
		cout << "Case #" << i + 1 << ": " << friends << endl;
	}

	return 0;
}
