#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <stdio.h>

using namespace std;

int main(){
	
	int t;
	cin >> t;;
		
	for (int k = 0; k < t; k++) {
		string s;
		cin >> s;
		
		int r = 0;
		bool b = 1;
		for (int i = s.size() - 1; i >= 0; i--) {
			if ((s[i] == '-' && b) || (s[i] == '+' && !b)) {
				r++;
				b = !b;
			}
		}
		cout << "Case #" << k + 1 << ": " << r << endl;
	}
	
	return 0;
}
