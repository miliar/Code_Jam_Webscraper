//--------------------------------------------------------------------------------------------------------------------------------------
// Constants

//--------------------------------------------------------------------------------------------------------------------------------------
// Include

#include <iostream> 
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

//--------------------------------------------------------------------------------------------------------------------------------------
// Variables

//--------------------------------------------------------------------------------------------------------------------------------------
// Functions

void xuly(void);
string numberToString(int m);

//--------------------------------------------------------------------------------------------------------------------------------------
// Main programs

int main() {
   
	xuly();
	return 0;
}

//--------------------------------------------------------------------------------------------------------------------------------------
// Solution

void xuly() {

	int T;
	long p;   
	
    cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> p;
		
		if (p == 0) cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		else {	
			int s[10];
			for (int j = 0; j < 10; j++) {
				s[j] = 0;
			}
			
			int k = 1;
			long n = 1;			
			
			while (true) {
    			n = p * k;
    			
    			string num = numberToString(n);
				for (int t = 0; t < num.size(); t++) {
					s[num[t] - '0'] = 1;
				}
				
				bool valid = true;
				for (int t = 0; t < 10; t++) {
					if (s[t] == 0) {
						valid = false;
						break;
					}
				}
				
				if (valid) break;
				
				k++;
			}
			
			cout << "Case #" << i << ": " << n << endl;
		}
	}
}

string numberToString(int m) {
	ostringstream ss;
    ss << m;
    return ss.str();
}

