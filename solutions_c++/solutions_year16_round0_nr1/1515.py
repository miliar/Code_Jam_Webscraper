#include <iostream>
#include <string.h>
#include <stdint.h>
#include <vector>
#include <stack>
#include <algorithm>
#include <stdio.h>
#include <bitset>
using namespace std;

int main(int argc, char* argv[])
{
	if (argc >= 2) {
		FILE* fp = freopen(argv[1], "r", stdin);
	}

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		uint64_t N;
		cin >> N;
		if (N == 0) {
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}

		bitset<10> b;
		uint64_t n = N;

		for (uint64_t m = n; m > 0; m /=10) {
			b.set(m % 10);
		}
		while (!b.all()) {
			n += N;
			for (uint64_t m = n; m > 0; m /=10) {
				b.set(m % 10);
			}
		}

		cout << "Case #" << i + 1 << ": " << n << endl;
	}

	return 0;
}
