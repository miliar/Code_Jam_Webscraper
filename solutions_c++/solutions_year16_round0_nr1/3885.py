#include <iostream>
#include <string>

using namespace std;

int main() {
	int t, n;
	const long BIGNUM = 1000000000;
	cin >> t;
	for (int k = 1; k <= t; ++k) {
		cout << "Case #" << k << ": ";	
		cin >> n;
		bool b = 0;
		bool got[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		for (int j = 1; j < BIGNUM; ++j) {
			//cout << n*j << endl;
			for (auto c : to_string(n*j)) {
				got[c-'0'] = 1;
			}
			int c = 0;
			for (int j = 0; j < 10; ++j) c += got[j];
			if (c == 10) {
				cout << n*j << endl;
				b = 1;		
				break;	
			}	
		}
		if (!b) cout << "INSOMNIA" << endl;
		//cout << "---------------------------------" << endl;	
	}
}
