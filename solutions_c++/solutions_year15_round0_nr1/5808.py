/*
 * a.cpp
 *
 *  Created on: 11-Apr-2015
 *      Author: akshay
 */




#include <iostream>

using namespace std;

int main() {
	int t;
	char s[1002];

	cin >> t;

	for(int tc=0; tc<t; tc++) {
		int smax;
		cin >> smax;
		cin >> s;

		cerr << smax << "\t"<< s << endl;

		int stack = 0;
		int invite = 0;
		int shy = -1;
		for(int i=0; i<=smax; i++) {
			shy = s[i] - '0';
			if(shy == 0) {
				if(stack == 0)
					invite++;
				else
					stack--;
			} else {
				stack += (shy - 1);
			}
		}

		cout << "Case #" << (tc + 1) << ": " << invite << endl;
	}

	return 0;
}
