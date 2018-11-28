#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <assert.h>
#include <queue>

using namespace std;

double prob(const vector<double>& p, int start, int k)
{
	if (start >= p.size()) {
		return k == 0 ? 1 : 0;
	}
	double left = p[start] * prob(p, start + 1, k - 1);
	double right = (1 - p[start]) * prob(p, start + 1, k);
	return left + right;
}

void test()
{
	int N, K;
	cin >> N >> K;

	vector<double> P(N, 0);
	for (int i = 0; i < N; i++) {
		cin >> P[i];
	}

	int maskMax = 1 << N;
	vector<double> PK(K, 0);
	double result = 0;
	for(int mask = 0; mask < maskMax; mask++) {
		int votersCount = 0;
		for(int i = 0; i < N; i++) {
			if ((mask & (1 << i)) != 0) {
				if (votersCount < K) {
					PK[votersCount] = P[i];
				}
				votersCount++;
			}
		}
		if (votersCount != K) {
			continue;
		}
		// нужно посчитать вероятность того, что будет ровно половина голосов
		double tieProbability = prob(PK, 0, K / 2);
		result = max(result, tieProbability);
	}
	cout << result;
}

int main()
{
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		test();
		cout << endl;
	}
	return 0;
}
