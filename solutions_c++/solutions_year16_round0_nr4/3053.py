//============================================================================
// Name        : r1d.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int T, K, C, S;
	int i, j;

	cin >> T;

	for (i = 0; i < T; i++) {
		cin >> K >> C >> S;
		// we know K == S;

		cout << "Case #" << i + 1 << ":";
		for (j = 1; j <= K; j++) {
			cout << " " << j ;
		}
		cout << endl;
	}

	return 0;
}
