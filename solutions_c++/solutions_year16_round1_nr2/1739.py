#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int T, N;
	int ns[2501];
	int list[100][50];
	int res[51];
	/*
	int list[100][50];
	int complete[50][50];
	bool used[100];
	int ns[50][2500];
	bool rows[50];
	bool cols[50];
	int minv, maxv;
	*/

	cin >> T;

	int i, j, k;

	for (i = 0; i < T; ++i) {
		cin >> N;

		memset(ns, 0x00, sizeof(ns));
		memset(list, 0x00, sizeof(list));
		memset(res, 0x00, sizeof(res));
		/*
		memset(list, 0x00, sizeof(list));
		memset(complete, 0x00, sizeof(complete));
		memset(used, 0x00, sizeof(used));
		memset(ns, 0x00, sizeof(ns));
		memset(rows, 0x00, sizeof(rows));
		memset(cols, 0x00, sizeof(cols));

		minv = 10000;
		maxv = -1;
		*/

		for (j = 0; j < 2 * N - 1; ++j) {
			for (k = 0; k < N; ++k) {
				cin >> list[j][k];

				++ns[list[j][k]];

				/*
				++ns[k][list[j][k]];

				if (k == 0)
					minv = min(minv, list[j][k]);
				if (k == N - 1)
					maxv = max(maxv, list[j][k]);
					*/
			}
		}

		int n_res = 0;

		for (j = 1; j <= 2500; ++j) {
			if (ns[j] % 2 == 1) {
				res[n_res] = j;
				++n_res;
			}
		}

		sort(&res[0], &res[n_res]);

		printf("Case #%d:", i + 1);

		for (j = 0; j < n_res; ++j)
			printf(" %d", res[j]);

		printf("\n");

		/*
		if (ns[0][minv] == 2) {
			for (j = 0; j < 2 * N - 1; ++j) {
				if (minv == list[j][0]) {
					memcpy(&complete[0][0], &list[j][0], sizeof(int) * N);
					used[j] = true;
					rows[0] = true;
					break;
				}
			}

			for (++j; j < 2 * N - 1; ++j) {
				if (minv == list[j][0]) {
					for (k = 1; k < N; ++k)
						complete[k][0] = list[j][k];
					used[j] = true;
					cols[j] = true;
					break;
				}
			}
		}

		else {
			for (j = 0; j < 2 * N - 1; ++j) {
				if (maxv == list[j][N - 1]) {
					memcpy(&complete[N - 1][0], &list[j][0], sizeof(int) * N);
					used[j] = true;
					rows[N - 1] = true;
					break;
				}
			}

			for (++j; j < 2 * N - 1; ++j) {
				if (maxv == list[j][N - 1]) {
					for (k = 1; k < N; ++k)
						complete[k][N - 1] = list[j][k];
					used[j] = true;
					cols[N - 1] = true;
					break;
				}
			}
		}
		*/
	}
}