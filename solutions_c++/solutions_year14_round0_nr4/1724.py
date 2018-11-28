#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	char *output = "Case #";
	cin >> n;
	double N[1001];
	double K[1001];
	for (int round = 1; round <= n; ++round) {
		int num_of_block;
		cin >> num_of_block;
		for (int i = 0; i < num_of_block; ++i)
			cin >> N[i];
		for (int i = 0; i < num_of_block; ++i)
			cin >> K[i];

		sort(N, N+num_of_block);
		sort(K, K+num_of_block);

		int deceitful_result = 0;
		int war_result = 0;
		int n_i = num_of_block - 1;
		int n_small = 0;
		int k_i = num_of_block - 1, k_small = 0;
		for (; n_i >= n_small; --n_i) {
			for (; k_i >= k_small; --k_i) {
				if (N[n_i] > K[k_i]){
					deceitful_result++;
					k_i--;
					break;
				}
				else {
					++n_small;
				}
			}
		}

		int K_start = 0;
		for (int i = num_of_block - 1; i >= 0; i--) {
			bool beatN = false;
			for (int j = K_start; j < num_of_block; j++) {
				if (K[j] > N[i]){
					K[j] = -1;
					beatN = true;
					break;
				}
			}
			if (!beatN) {
				K_start++;
				war_result++;
			}
		}

		cout << output << round << ": " << deceitful_result << " " << war_result << endl;
	}
}