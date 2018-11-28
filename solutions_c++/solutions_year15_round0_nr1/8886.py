#include <bits/stdc++.h>

using namespace std;

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, n;
	string shy;

	cin >> t;
	for(int i = 1; i <= t; i++) {
		cin >> n >> shy;
		int standing = shy[0] - '0', invite = 0;
		for(int j = 1; j <= n; j++) {
			int temp = shy[j] - '0';
			if( j > (standing+invite) ) {
				invite++;
			}

			standing += temp;
		}

		cout << "Case #" << i << ": " << invite << "\n";
	}

	return 0;
}