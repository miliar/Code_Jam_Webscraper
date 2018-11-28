#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int64_t K, C, S;
		cin >> K >> C >> S;
		int64_t sz = 1;
		for (int i = 1; i < C; ++i)
			sz *= K;
		cout << "Case #" << (t+1) << ": ";
		for (int64_t i = 0; i < K; ++i) {
			cout << i*sz+1 << " "; 
		}
		cout << endl;
	}
}