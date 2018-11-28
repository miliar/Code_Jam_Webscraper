#include <iostream>
using namespace std;

int sums[1000];
int cur[100];
int mins[100];
int maxs[100];

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N, K;
		cin >> N >> K;

		for (int i = 0; i < K; i++) {
			cur[i] = mins[i] = maxs[i] = 0;
		}

		for (int i = 0; i < N-K+1; i++) {
			cin >> sums[i];
			if (i > 0) {
				cur[i%K] += sums[i]-sums[i-1];
				if (cur[i%K] < mins[i%K]) mins[i%K] = cur[i%K];
				if (cur[i%K] > maxs[i%K]) maxs[i%K] = cur[i%K];
			}
		}

		int worst = 0;
		int shift = 0;
		for (int i = 0; i < K; i++) {
			shift -= mins[i];
			if (maxs[i]-mins[i] > worst) worst = maxs[i]-mins[i];
		}
		if (shift%K != sums[0]%K) {
			int problem = ((sums[0]%K)-(shift%K)+K)%K;
			int accum = 0;
			for (int i = 0; i < K; i++) {
				accum += (worst-maxs[i]+mins[i]);
			}
			if (accum < problem) worst++;
		}

		cout << "Case #" << t << ": " << worst << '\n';
	}

	return 0;
}
