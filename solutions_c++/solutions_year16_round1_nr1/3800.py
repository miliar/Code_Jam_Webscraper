//============================================================================
// Name        : 1A.cpp
// Author      : Le Trong Giap
// Version     : 1.0
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

void solveProblem(string S, int testNumber) {
	int size = S.size();
    string r;

	for (int i = 0; i < S.size(); i++) {
		if (i == 0) {
			r =  S.substr (0,1);
			continue;

		}
		string s1 = r+ S.substr (i,1);
		string s2 = S.substr (i,1) + r;
		if (s1.compare(s2) >= 0)
			r = s1;
		else
			r = s2;

	}
	cout << "Case #" << testNumber << ": " << r << endl;
}
int main() {
	int T;
	string s;
	cin >> T;
	//cout << T << endl;

	for (int i = 0; i < T; i++) {
		cin >> s;
		solveProblem(s, i+1);
	}
	return 0;
}
