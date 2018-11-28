#include <bits/stdc++.h>

using namespace std;

int main() {
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		bool digit[10]{};
		map<long long, bool> vis;
		long long N;
		cin >> N;
		string result = "INSOMNIA";
		for (int i = 1; N * (double) i < 7e18 && !vis[N * i]++; i++) {
			string S = to_string(N * i);
			for (char A: S)
				digit[A - '0']++;

			bool found = true;
			for (int j = 0; j < 10; j++)
				if (!digit[j])
					found = false;

			if (found) {
				result = S;
				break;
			}
		}

		cout << "Case #" << t << ": " << result << endl;
	}

	return 0;
}
