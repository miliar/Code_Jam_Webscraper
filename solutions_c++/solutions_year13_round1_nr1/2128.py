#include <iostream>

using namespace std;

//const double PI = atan(1)*4; 

int main() {
	
	int T;
	cin >> T;

	for (int caso=1; caso<=T; caso++) {
		long long int r, t, amount = 0, count = 0;
		cin >> r >> t;
		while (amount < t) {
			amount += (2*r)+(4*(count+1))-3;
			if (amount <= t)
				count++;
		}

		cout << "Case #" << caso << ": " << count << endl;
	}
}