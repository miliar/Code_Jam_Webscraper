#include <iostream>
#define ull unsigned long long

using namespace std;

int main() {
	ull t, n, m, ca = 1;
	cin >> t;
	while (t--) {
		cin >> n;
		ull b = 0, name = 0, cnt = 0;
		if (n != 0) {
			while (b != 1023) { 
				name = m = n*(++cnt);
				while (m > 0) {
					int d = m%10;
					b |= (1 << d);
					m /= 10;
				}
			}			
			cout << "Case #" << ca++ << ": " << name << endl;
		}
		else
			cout << "Case #" << ca++ << ": " << "INSOMNIA" << endl;
	}
}
