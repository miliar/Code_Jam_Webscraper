#include <iostream>

using namespace std;

int main() {
	
	int t;
	cin >> t;

	for(int cases = 1; cases <= t; cases++) {
		int digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int n;

		cin >> n;

		if(n==0) {
			cout << "Case #" << cases << ": INSOMNIA" << endl;
			continue;
		}

		int number = 0;
		int digitcount = 0; // zero distinct digits found so far

		while( digitcount < 10 ) {
			number += n;
			int examine = number;
			
			while(examine > 0) {
				int lsd = examine%10;
				if(digits[lsd] == 0) {
					digits[lsd] = 1;
					digitcount++;
				}
				examine /= 10;
			}
			
		}



		cout << "Case #" << cases << ": " << number << endl;
	}
}