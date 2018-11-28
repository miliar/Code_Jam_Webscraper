#include <iostream>
#include <string>
#include <stdio.h>
#include <cmath>
#include <bitset>
#include <cstdlib>

using namespace std;
int main() {

	int t;
	cin >> t;
	string s;
	int counter = 1;
	while (counter <= t) {
		cout << "Case #" << counter << ": ";

		cin >> s;
		bool str[s.length()];
		for (int k = 0; k < s.length() ; k++) {
				if(s[k] == '+') {
					str[k] = true;
				}
				else {
					str[k] = false;
				}
		}
		
		long long int flipCount = 0;
		for (int k = 0; k < s.length()-1 ; k++) {
			if (str[k] != str[k+1]) {
				flipCount = flipCount + 1;
			}
			
		}
		if (str[s.length()-1] == false)
			flipCount = flipCount + 1;
		cout << flipCount << endl;
		counter = counter + 1;
	}
}