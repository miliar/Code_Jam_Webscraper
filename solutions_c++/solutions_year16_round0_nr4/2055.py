#include <iostream>
#include <vector>

using namespace std;


int main() {
	int T;
	cin >> T;
	for (int case_n = 1; case_n <= T; ++case_n) {
		cout << "Case #" << case_n << ":";
		long long K;
		int C, S;
		cin >> K >> C >> S;
		int required_requests = (K / C) + (((K % C) > 0) ? 1 : 0);
		if (S < required_requests) {
			cout << " IMPOSSIBLE" << endl;
			continue;
		}
		vector<long long> pow_k;
		pow_k.push_back(1);
		for (int i = 1; i < C; ++i) {
			pow_k.push_back(pow_k.back() * K);
		}
		long long last_asked = -1;
		for (int i = 0; i < required_requests; ++i) {
			long long request = 0;
			for (int j = 0; (j < C) && ((last_asked + 1) < K); ++j) {
				long long cur = last_asked + 1;
				request += cur * pow_k[j];
				++last_asked;
			}
			cout << " " << (request + 1);
		}
		cout << endl;
	}	
	return 0;
}