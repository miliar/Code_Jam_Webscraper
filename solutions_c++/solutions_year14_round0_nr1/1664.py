#include <bits/stdc++.h>

using namespace std;

int a[10][10], b[10][10];
int T, x, y;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.ou", "w", stdout);
	cin >> T;

	
	for (int test = 1; test <= T; test++) {
		cin >> x;
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				cin >> a[i][j];
			}
		}
		
		cin >> y;		
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				cin >> b[i][j];
			}
		}		
		int count = 0;
		int res;
		
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				if (a[x][i] == b[y][j]) {
					count++;
					res = a[x][i];
				}
			}
		}
		
		cout << "Case #" << test << ": ";
		if (count == 1) {
			cout << res << endl;
		}
		if (count == 0) {
			cout << "Volunteer cheated!" << endl;
		}
		if (count > 1) {
			cout << "Bad magician!" << endl;
		}
	}
}
