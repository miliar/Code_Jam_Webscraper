#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int t, d, n, cn, result, p[1024], ss;

int main() {

	cin >> t;
	for (int C = 1; C <= t; C++) {
		printf("Case #%d: ", C);

		cin >> d;
		result = 0;
		for (int i = 0; i < d; i++) {
			cin >> p[i];
			result = max(result, p[i]);
		}

		for (int k = 2; k < result; k++) {
			ss = 0;
			for (int i = 0; i < d; i++) {
				ss += p[i] / k;
				if (p[i] % k == 0) {
					ss--;
				}
			}
			result = min(result, k + ss);
		}

		printf("%d\n", result);
	}

	return 0;
}
