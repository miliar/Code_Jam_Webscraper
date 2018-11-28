#include <iostream>
using namespace std;
int main(){
	int n, t, i, a[10], l, c, x = 0, b = 0;
	cin >> t;
	for (i = 1; i <= t; i++) {
		for (int j = 0; j < 10; j++) {
			a[j] = 10;
		}
		cin >> n;
		if (n != 0) {
			b = n;
			while (a[9] == 10) {
				l = b;
				while (l > 0) {
					c = 0;
					x = 0;
					for (int j = 0; j < 10; j++) {
						if (x != 1) {
							if (a[j] == l % 10) {
								c++;
							}
							if (c == 0 && a[j] == 10) {
								a[j] = l % 10;
								x = 1;
								c++;
							}
						}
					}
					l /= 10;
				}
				b += n;
			}
			cout << "Case #" << i << ": " << b - n << endl;
		}
		else {
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
	}
	return 0;
}
