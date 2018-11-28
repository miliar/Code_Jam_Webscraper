#include <iostream>

using namespace std;

typedef unsigned long long ULL;

ULL b[9];

void solve()
{
	int n, j;
	cin >> n >> j;
	ULL p[9][n];
	bool num[n];
	num[0] = 1;
	num[n - 1] = 1;
	for (int i = 0; i < 9; i++) {
		b[i] = 1;
		p[i][0] = 1;
		for (int j = 1; j < n; j++) p[i][j] = p[i][j - 1] * (i + 2);
		b[i] += p[i][n - 1];
	}
	while (j > 0) {
		bool isJamcoin = true;
		int d[9] = {0};
		for (int i = 0; i < 9; i++) {
			if (b[i] % 2 == 0){
				d[i] = 2;
				continue;
			}
			for (ULL td = 3; td * td <= b[i]; td += 2) {
				if (b[i] % td == 0) {
					d[i] = td;
					break;
				}
			}
			if (d[i] == 0) {
				isJamcoin = false;
				break;
			}
		}
		if (isJamcoin) {
			cout << b[8];
			for (int i = 0; i < 9; i++) cout << " " << d[i];
			cout << endl;
			j--;
		}
		int i = n - 2;
		while (num[i] == 1) {
			num[i] = 0;
			for (int k = 0; k < 9; k++) b[k] -= p[k][n - 1 - i];
			i--;
		}
		if (i >= 1) {
			num[i] = 1;
			for (int k = 0; k < 9; k++) b[k] += p[k][n - 1 - i];
		}
	}
}

int main()
{
	int t;
	cin >> t;
	cout << "Case #1:\n";
	solve();
	return 0;
}
