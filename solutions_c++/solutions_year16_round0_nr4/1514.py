#include <iostream>
#include <string.h>
#include <stdint.h>
#include <vector>
#include <stack>
#include <algorithm>
#include <stdio.h>
#include <bitset>
using namespace std;

int K, C, S, R;
void solve()
{
	uint64_t F = 1;
	for (int c = 1; c < C; c++) {
		F *= K;
	}
	for (uint64_t v = 1; ; v++) {
		uint64_t result = 0;
		uint64_t factor = F;
		uint64_t vv = v;
		for (int c = 0; c < C; c++) {
			result += (vv - 1) * factor;
			if (vv < K) vv++;
			if (factor > 1) factor /= K;
		}
		cout << " " << result + 1;
		if (--R <= 0) {
			return;
		}
	}
}

int main(int argc, char* argv[])
{
	if (argc >= 2) {
		FILE* fp = freopen(argv[1], "r", stdin);
	}

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> K >> C >> S;
		cout << "Case #" << i + 1 << ":";
		if (K == 1) {
			if (S == 0) {
				cout << " IMPOSSIBLE" << endl;
			} else {
				cout << " 1" << endl;
			}
		} else {
			R = K - (C - 1);
			if (R <= 0) R = 1;
			if (S < R) {
				cout << " IMPOSSIBLE" << endl;
			} else {
				solve();
				cout << endl;
			}
		}
	}

	return 0;
}
