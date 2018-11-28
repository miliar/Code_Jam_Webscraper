#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

#define IN_FILE "large.txt"
#define OUT_FILE "output.txt"

using namespace std;

int main(int argc, char const *argv[]) { 

	freopen(IN_FILE, "r", stdin);
	freopen(OUT_FILE, "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {

		int N;
		cin >> N;

		vector<double> naomi(N), ken(N);
		vector<bool> used_naomi(N, false), used_ken(N, false);
		vector<bool> used_naomi_d(N, false), used_ken_d(N, false);
		
		for (int i = 0; i < N; ++i)
			cin >> naomi[i];

		for (int i = 0; i < N; ++i)
			cin >> ken[i];

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		int result_war = 0, result_d_war = 0;

		for (int n = 0; n < N; ++n) {
			int naomis_block = n;

			int kens_block = 0;
			while (kens_block < N && (used_ken[kens_block] || ken[kens_block] < naomi[naomis_block]))
				++kens_block;

			if (kens_block == N) {
				kens_block = 0;
				while (used_ken[kens_block])
					++kens_block;
			}

			if (naomi[naomis_block] > ken[kens_block])
				++result_war;

			used_naomi[naomis_block] = true;
			used_ken[kens_block] = true;

		}

		for (int n = 0; n < N; ++n) {
			int naomis_block = n;

			int kens_max_block = N - 1;
			int kens_min_block = 0;
			while (used_ken_d[kens_min_block])
				++kens_min_block;

			while (used_ken_d[kens_max_block])
				--kens_max_block;

			if (naomi[naomis_block] > ken[kens_min_block]) {
				used_naomi_d[naomis_block] = true;
				used_ken_d[kens_min_block] = true;

				++result_d_war;
			} else {
				used_naomi_d[naomis_block] = true;
				used_ken_d[kens_max_block] = true;
			}


		}

		printf("Case #%d: %d %d\n", t+1, result_d_war, result_war);
	}

	return 0;
}