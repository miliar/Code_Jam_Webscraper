//g++ --std=c++14 -Wall -Wno-sign-compare -Os -march=native
#include <iostream>
#include <iterator>
#include <algorithm>
#include <limits>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <iomanip>
#include <cmath>
using namespace std;

void gcjmain() {
	string S;
	cin >> S;
	int working = S.length();
	while (S[working-1] == '+') working--;
	int flips = 0;
	while (working) {
		if (S.front() == '+') {
			int count = 0;
			while (S[count] == '+') S[count++] = '-';
		} else {
			int count = 0;
			while (S[count] == '-') count++;
			reverse(S.begin(), S.begin() + working);
			for (int i = 0; i < working; i++) {
				if (S[i] == '+') S[i] = '-';
				else S[i] = '+';
			}
			working -= count;
		}
		flips++;
	}
	cout << flips << endl;
}

int main() {
	int T;
	cin >> T;
	for(int t = 1; t < T+1; t++) {
		cerr << "Case: " << t << '/' << T << endl;
		cout << "Case #" << t << ": ";
		gcjmain();
	}
}
