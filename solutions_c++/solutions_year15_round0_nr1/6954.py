#include <iostream>

using namespace std;

int main() {
	int T, c, d, j, a, k, tmp;
	char p;
	
	cin >> T;
	
	for (int i = 1; i <= T; i++) {
		c = 0;
		a = 0;
		
		cin >> d;
		
		for (j = 0; j < (d+1); j++) {
			cin >> p;
			k = p-'0';
			
			if (k>0) {
				if (j <= c)
					c += k;
				else {
					tmp = j-c;
					c += tmp+k;
					a += tmp;
				}
			}
		}
		
		cout << "Case #" << i << ": " << a << "\n";
	}
	
	return 0;
}
