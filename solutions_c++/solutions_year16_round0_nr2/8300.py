#include <iostream>
#include <string>
using namespace std;

void flip(string str, int pos) {
	
}

int main() {
	// declare variables
	int t;
	string str;
	
	// input test cases
	cin >> t;
	
	// loop for test cases
	for ( int i = 1; i <= t; i++ ) {
		// inputs
		cin >> str;
		
		int pos = str.length()-1;
		int count = 0;
		
		
		
		while(pos >= 0) {
			
			//cout << "pos: " << pos << endl; // testing
			
			//cout << "str: " << str << endl;// testing 			
			
			if (str[pos] == '-') {
				count++;
				
				//flip(str, pos);	
				for (int k = pos; k >= 0; k--) {
					if ( str[k] == '-' ) {
						str[k] = '+';
					} 
					else {
						str[k] = '-';
					}
				}
	
			}
			pos--;
		}
		
		// print ith test case result
		cout << "Case #" << i << ": " << count <<endl;
	}
	
	return 0;
} 