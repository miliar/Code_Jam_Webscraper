#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int T, N, H[3000];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> T;
	for (int t = 1; t <= T; t++) {
		memset(H, 0, sizeof(H));
		cin >> N;

		for (int i = 0; i < 2 * N - 1; i++)
		for (int j = 0; j < N; j++) {
			int x;
			cin >> x;

			H[x]++;
		}

		vector<int> ret;

		for (int h = 1; h <= 2500; h++) if (H[h] % 2 != 0) ret.push_back(h);

		sort(ret.begin(), ret.end());

		printf("Case #%d:", t);

		for (int i = 0; i < N; i++)
			printf(" %d", ret[i]);

		printf("\n");
	}
}