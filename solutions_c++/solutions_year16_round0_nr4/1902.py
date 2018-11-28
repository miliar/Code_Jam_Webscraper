#include <cmath>
#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		
		int k, c, s;
		cin >> k >> c >> s;
		
		if (s < k) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			long long p = 1;
			long long o = pow(k, c - 1);
			
			cout << p;
			for (int j = 0; j < k - 1; ++j) {
				p += o;
				cout << " " << p;
			}
			cout << endl;
		}
	}
	
	return 0;
}