#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int T, n, m;
int P[1043];
int main() {
	freopen("input2.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
	cin >> T;
	for (int test = 1; test <= T; test++) {
		cin >> n;
		int maxP = 0;
		for (int i = 0; i < n; i++) {
			cin >> P[i];
			if (P[i] > maxP) maxP = P[i];
		}
		int ans = 1 << 30;
		for (int k = 1; k <= maxP; k++) {
			int sum = 0;
			for (int i = 0; i < n; i++) {
				if (P[i] > k) {
					sum += (P[i] - 1) / k;
				}
			}
			sum += k;
			if (sum < ans) ans = sum;
		}

		cout << "Case #" << test << ": " << ans << endl; 
	}
	return 0;
}
