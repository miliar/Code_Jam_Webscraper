#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int testcase = 1; testcase <= T; testcase++) {
		int answer = 0, smax;
		string representation;

		cin >> smax >> representation;

		int standing = 0;

		for (int i = 0; i <= smax; i++) {
			int need = representation[i] - '0';
			if (i == 0) {
				standing += need;
			} else {
				if (i > standing && need > 0) {
					answer += (i - standing);
					standing += answer;
				}
				standing += need;
			}
		}

		cout << "Case #" << testcase << ": " << answer << endl;
	}

}