#include <iostream>     // std::cout
#include <algorithm>    // std::next_permutation, std::sort
#include <math.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <stdio.h>

using namespace std;


int m[1001];

int main () {
	int T, n;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> m[i];
		}

		long long int y = 0, z = 0;
		int max_dif = 0;
		for (int i = 0; i + 1 < n; ++i) {
			if (m[i] > m[i+1]) {
				y += m[i] - m[i+1];
				max_dif = max(max_dif, m[i] - m[i+1]);
			}
		}


		for (int i = 0; i + 1 < n; ++i) {
			z += min(max_dif, m[i]);
		}


		printf("Case #%d: %lld %lld\n", t, y , z);

	}
	return 0;
}
