#include <iostream>
#include <string>

using namespace std;




int main() {
	int T;
	long long r, t;
	cin >> T;
	for (int p = 1; p <= T; p++) {
		long c = 0;
		cin >> r >> t;
		//cout << r << t << endl;
		r++;
		while(1) {
			t -= (2* r - 1);
			if(t < 0)
				break;
			r+=2;
			c++;
		}

		cout << "Case #" << p << ": " << c << endl;
	}
}