//============================================================================
// Name        : Pogo.cpp
// Author      : swem
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int t = 0;
	cin >> t;
	for (int caseIdx = 1; caseIdx <= t; caseIdx++) {
		long long int x, y;
		cin >> x >> y;

		string answer;
		if (x < 0) {
			for (int i = 0; i < -x; i++) {
				answer += "EW";
			}
		} else {
			for (int i = 0; i < x; i++) {
				answer += "WE";
			}
		}
		if (y < 0) {
			for (int i = 0; i < -y; i++) {
				answer += "NS";
			}
		} else {
			for (int i = 0; i < y; i++) {
				answer += "SN";
			}
		}

		cout << "Case #" << caseIdx << ": " << answer << endl;
	}

	return 0;
}
