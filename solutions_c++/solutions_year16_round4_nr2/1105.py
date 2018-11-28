#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <unordered_map>
#include <bitset>

using namespace std;

void test(int number)
{
	int N, K;
	cin >> N >> K;
	double P[N];
	for (int i = 0; i < N; ++i)
		cin >> P[i];

	double bestProb = 0.0;
	int bestInd = 0;

	for (int i = 0; i < (1 << N); ++i) {
		int bits = 0;
		int ind = i;
		while (ind) {
			if (ind & 1) bits++;
			ind >>= 1;
		}
		if (bits != K) continue;

		vector<double> prob(K);
		prob[0] = 1.0;
		for (int j = 0; j < N; ++j) {
			if (!(1 << j & i)) continue;
			vector<double> newProb(K);
			for (int k = 0; k < K; ++k) {
				newProb[k] = (1.0 - P[j]) * prob[k];
				if (k) newProb[k] += P[j] * prob[k-1];
			}
			prob = newProb;
		}
		if (prob[K/2] > bestProb) {
			bestProb = prob[K/2];
			bestInd = i;
		}
	}

	printf("Case #%d: %f\n", number + 1, bestProb);
}

int main(int argc, char *argv[])
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
		test(t);
	return 0;
}