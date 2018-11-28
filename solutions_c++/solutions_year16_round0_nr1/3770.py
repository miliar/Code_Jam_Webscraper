#include <bits/stdc++.h>

using namespace std;

void solve(int64_t N) {
	vector<bool> seen(10);
	int64_t max_mult = 1e5;
	int64_t mult;
	for (mult = 1; mult < max_mult; ++mult) {
		int64_t num = N*mult;
		string str = to_string((long long)num);
		for (char c : str) {
			seen[c-'0'] = true;
		}
		int sc = 0;
		for (bool b : seen) sc += b;
		if (sc == 10) {
			break;
		}
	}
	if (mult == max_mult) {
		cout << "INSOMNIA" << endl;
	} else {
		cout << (N*(mult)) << endl;
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int64_t N;
		cin >> N;
		cout << "Case #" << (t+1) << ": ";
		solve(N);
	}

}