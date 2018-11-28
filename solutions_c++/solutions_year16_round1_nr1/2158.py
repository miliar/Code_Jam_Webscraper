//============================================================================
// Name        : 1a-a.cpp
// Author      : Long Pham
//============================================================================

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
	int T;
	string S;
	string w;

	cin >> T;

	for (int t = 0; t < T; t++) {
		cin >> S;
		int len = S.size();
		unsigned char first = 0;
		w = "";
		for (int i=0; i < len; i++) {
			if (S[i] >= first) {
				w.insert(0, 1, S[i]);
				first = S[i];
			} else {
				w.append(1, S[i]);
			}
		}
		cout << "Case #" << t+1 << ": " << w << endl;
	}
	return 0;
}
