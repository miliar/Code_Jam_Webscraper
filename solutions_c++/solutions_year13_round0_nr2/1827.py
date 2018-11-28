#include <iostream>

using namespace std;



int main() {
	int a[100][100];
	bool b[100][100];
	int x,y;
	bool ans;
	
	int cases;
	cin >> cases;
	for (int caseno = 1; caseno <= cases; caseno++) {
		cout << "Case #" << caseno << ": ";
		cin >> x >> y;
		ans = true;
		for (int i = 0; i < x; i++) {
			for (int j = 0; j < y; j++) {
				cin >> a[i][j];
			}
		}
		for (int h = 1; h < 100 && ans; h++) {
			for (int i = 0; i < x; i++) {
				for (int j = 0; j < y; j++) {
					b[i][j] = false;
				}
			}
			for (int i = 0; i < x && ans; i++) {
				for (int j = 0; j < y && ans; j++) {
					if (b[i][j])
						continue;
					if (a[i][j] == h) {
						bool c = true;
						bool r = true;
						for (int k = 0; k < x; k++) {
							b[k][j] = true;
							if (a[k][j] != h) {
								c = false;
								break;
							}
						}
						for (int k = 0; k < y; k++) {
							b[i][k] = true;
							if (a[i][k] != h) {
								r = false;
								break;
							}
						}
						ans = c || r;
					}
					b[i][j] = true;
				}
			}
			for (int i = 0; i < x; i++) {
				for (int j = 0; j < y; j++) {
					if (a[i][j] == h)
						a[i][j]++;
				}
			}
		}
		if (ans)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
}