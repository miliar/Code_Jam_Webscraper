//============================================================================
// Name        : GoogleJam.cpp
// Author      : Marian Shymon
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

bool isJamcoin(string &str, vector<long long> &divisors) {

	for(int base = 2; base <= 10; base++) {
		long long num = stoll(str, 0, base);

		int square_root = (int) sqrt(num);
		bool found_div = false;
		for(long long i = 2; i < square_root; i++) {
			if (num%i == 0) {
				divisors.push_back(i);
				found_div = true;
				break;
			}
		}

		if (!found_div) {
			return false;
		}
	}

	return true;
}


int main() {

	int T;
	cin >> T;

	for(int t = 1; t <= T; t++) {
		int n, m;
		cin >> n >> m;

		cout << "Case #" << t << ":" << endl;

		int nn = n - 2;
		long max_num = 1 << nn;
		for(long num = 0; (num < max_num) && m; num++) {

			string str = "";

			for(int i = nn-1; i >= 0; i--) {
				char ch = (num & (1 << i))? '1' : '0';
				str.push_back(ch);
			}

			str = "1" + str + "1";
			vector<long long> divisors;

			if (isJamcoin(str, divisors)) {
				cout << str;

				for(int i = 0; i < divisors.size(); i++) {
					cout << " " << divisors[i];
				}

				cout << endl;

				--m;
			}
		}
	}

	return 0;
}
