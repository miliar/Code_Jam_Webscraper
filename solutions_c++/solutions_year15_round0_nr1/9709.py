#include <bits/stdc++.h>

using namespace std;

int main() {

	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {

		int S_max;
		string values;
		cin >> S_max >> values;
		
		int res = 0;
		int till_now = 0;
		
		int j = 0;
		
		for (int j = 0; j <= S_max; j++) {
			if (j > till_now) res += j - till_now;
			till_now += (values[j] - '0') + max(0, j - till_now);
		}

		cout << "Case #" << i + 1 << ": " << res << endl;
	}

	return 0;
}