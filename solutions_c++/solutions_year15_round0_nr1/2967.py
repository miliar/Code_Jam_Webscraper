//============================================================================
// Name        : q1a.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>

using namespace std;

int main() {
	unsigned int T;
	unsigned int i, j, k, smax, count, friends, more;
	string sh;
	cin >> T;
	for (i = 0; i < T; i++) {
		cin >> smax >> sh;
		count = 0;
		friends = 0;
		for (j = 0; j <= smax; j++) {
			k = sh[j] - '0';
			more = (count < j)? j - count : 0;
			friends += more;
			count += k + more;
		}

		cout << "Case #" << i+1 << ": " << friends << endl;
	}
	return 0;
}
