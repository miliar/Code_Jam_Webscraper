#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

long long exponen(int K, int C);

int main() {

	int T;
	cin >> T;

	for (int z = 1; z <= T; z++) {
		int K, C, S;
		cin >> K >> C >> S;
		cout << "Case #" << z << ": ";
		if (K == 1) cout << 1 << endl;
		else{
			long long temp = (exponen(K, C) - 1) / (K - 1);
			long long printing = 1;
			for (int i = 0; i < K; i++){
				printf("%lld ", printing);
				printing += temp;
			}
			cout << endl;
		}
	}
	return 0;
}


long long exponen(int K, int C) {
	long long ret = 1;
	for (int i = 0; i < C; i++) {
		ret *= K;
	}
	return ret;
}