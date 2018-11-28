#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

int main() {
	freopen("/home/gowtham/Downloads/B-small-attempt0.in", "r", stdin);
	freopen("/home/gowtham/Downloads/output.txt", "w", stdout);
	int T;
	cin >> T;
	for(int c = 1; c <= T; c++) {
		int A, B, K;
		cin >> A >> B >> K;
		long long ret = 0;
		for(int i = 0; i < K; ++i) {
			for(int j = 0; j < A; ++j) {
				for(int k = 0; k < B; ++k) {
					if((j & k) == i) {
						ret++;
					}
				}
			}
		}
		cout << "Case #" << c << ": " << ret << endl;
	}
	return 0;
}
