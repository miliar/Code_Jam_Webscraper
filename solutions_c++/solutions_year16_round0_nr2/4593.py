#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <locale>
#include <stdlib.h> 
using namespace std;

int main() {
	
	int T, t;

	cin >> T;
	for (t = 0; t < T; t++) {
		
		int i, c = 0;
		bool prevp = false;
		bool prevm = false;
		string S;
		cin >> S;

		// Loop over input
		for (i = 0; i < S.length(); i++) {
			// cout << "####Checking (" << i << ") " << S[i] << endl;
			// cout << "prevp: " << prevp << endl << "prevm: " <<  prevm << endl;
			// cout << "c: " << c;
			if (S[i] == '-') {
				if (prevp == true && prevm == false) {
					c += 2;
				} else if (prevm == false) {
					c++;
				}
				prevm = true;
				prevp = false;
			} else if (S[i] == '+') {
				prevm = false;
				prevp = true;
			}
			// cout << " -> " << c << endl;
		}

		cout << "Case #" << t+1 << ": " << c << endl;
	}
}
