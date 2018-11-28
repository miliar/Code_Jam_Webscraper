#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int T, n, m, r, c;

int main() {
	freopen("input4.txt", "r", stdin);
	freopen("output4.txt", "w", stdout);
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cin >> n >> r >> c;
		cout << "Case #" << test << ": ";
		
		if (n == 4) {
			if (r <= 2 || c <= 2) {
				cout << "RICHARD" << endl;
				continue;
			}
			if (r * c == 12 || r * c == 16)
				cout << "GABRIEL" << endl;
			else
				cout << "RICHARD" << endl;
			continue;
		}
		if (n == 1) {
			cout << "GABRIEL" << endl;
			continue;
		}
		if (n == 2) {
			if ((r * c % 2) == 1) cout << "RICHARD" << endl;
				else cout << "GABRIEL" << endl;
		}
		else {
			if ((r * c % 3) != 0 || r == 1 || c == 1) cout << "RICHARD" << endl;
				else cout << "GABRIEL" << endl;
		} 
	}
	return 0;
}
