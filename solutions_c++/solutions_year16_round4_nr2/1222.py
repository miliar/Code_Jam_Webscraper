#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <iomanip>
using namespace std;

using ll = long long int;
ifstream fin("1.in");
ofstream fout("1.out");

int N, K;
double probs[16];

double getprob(int mask) {
	double dp[16] = {1};
	double newDp[16];
	for (int i = 0; i < N; i++) {
		if (mask & (1 << i)) {
			for (int j = 0; j < N; j++) {
				newDp[j] = dp[j] * (1 - probs[i]) + (j>0 ? dp[j - 1] * probs[i] : 0);
			}
			for (int j = 0; j < N; j++) {
				dp[j] = newDp[j];
			}
		}
	}

	return dp[K / 2];
}

int main() {
	int T;
	fin >> T;
	fout << std::setprecision(10);
	for (int t = 1; t <= T; t++) {
		double best = 0;
		fout << "Case #" << t << ": ";
		fin >> N >> K;
		for (int i = 0; i < N; i++)
			fin >> probs[i];
		for (int i = 0; i < (1 << N); i++) {
			int size = 0;
			for (int j = 0; j < N; j++) {
				size += (bool)((1 << j) & i);
			}
			if (size == K) {
				double p = getprob(i);
				if (p > best)
					best = p;
			}
		}
		fout << best << endl;
	}
}
