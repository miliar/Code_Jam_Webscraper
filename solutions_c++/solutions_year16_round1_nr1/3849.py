#include <iostream>
#include <string>
using namespace std;

int main() {
	// declare variables
	int t;
	string s;
	string y;
	
	// input test cases
	cin >> t;
	
	// loop for test cases
	for ( int i = 1; i <= t; i++ ) {
		
		// inputs
		cin >> s;
		
		y = s[0];
		
		int len = s.length();
		
		char largest = s[0];
		int pos = 0;
		
		for ( int j = 1; j < len; j++ ) {
			if (s[j] >= largest) {
				// push to front of y
				largest = s[j];
				y.insert(0, 1, s[j]);
			}
			else {
				// push to last of y
				y.push_back(s[j]);
			}
		}
		
		// print ith test case result
		cout << "Case #" << i << ": " << y <<endl;
	}
	
	return 0;
} 