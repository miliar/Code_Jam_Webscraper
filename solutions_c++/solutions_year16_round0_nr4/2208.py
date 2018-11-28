#include <iostream>
using namespace std;

int tc, s;
long long k, c;

int main() {
	int tc;
	cin >> tc;
	for(int z = 1; z <= tc; z++) {
		cin >> k >> c >> s;
		
		cout << "Case #" << z << ":";
		
		if(c == 1) {
			if(s < k)
				cout << " IMPOSSIBLE" << endl;
			else {
				for(int i = 1; i <= k; i++)
					cout << " " << i;
				cout << endl;
			}
		}
		else {
			if(s < (k + 1)/2)
				cout << " IMPOSSIBLE" << endl;
			else {
				long long x = 1;
				for(int i = 1; i < c; i++)
					x *= k;
				long long a = 0;
				for(int i = 0; i < k - 1; i += 2) {
					cout << " " << a + (i + 1 ) + 1;
					a += x + x;
				}
				if(k % 2 == 1)
					cout << " " << a + x;
				cout << endl;
			}	
		}
	}
}
