#include <iostream>
#include <vector>
#include "BigIntegerLibrary.hh"
using namespace std;

int main() {
	int t;
	cin >> t;
	
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ":" << endl;
		
		int n, j;
		cin >> n >> j;
		
		string s = "1";
		for (int l = 0; l < n - 2; ++l) {
			s += '0';
		}
		s += '1';
		
		while (j > 0) {
			vector<BigInteger> d(11, 1);
			
			for (int b = 2; b <= 10; ++b) {
				BigInteger k = 0;
				BigInteger p = 1;
				
				for (int l = n - 1; l >= 0; --l) {
					if (s[l] == '1') {
						k += p;
					}
					p *= b;
				}
				
				if (k % 2 == 0) {
					d[b] = 2;
				} else if (k % 3 == 0) {
					d[b] = 3;
				} else {
					BigInteger m = 5;
					while ((m <= 1000) && (d[b] == 1) && (m * m <= k)) {
						if (k % m == 0) {
							d[b] = m;
						} else if (k % (m + 2) == 0) {
							d[b] = m + 2;
						}
						m += 6;
					}
				}
				
				if (d[b] == 1) {
					break;
				}
			}
			
			if (d[10] != 1) {
				--j;
				
				cout << s;
				for (int b = 2; b <= 10; ++b) {
					cout << " " << d[b];
				}
				cout << endl;
			}
			
			int l = n - 2;
			while (s[l] == '1') {
				s[l] = '0';
				--l;
			}
			s[l] = '1';
		}
	}
	
	return 0;
}