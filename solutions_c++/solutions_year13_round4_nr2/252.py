#include <iostream>
using namespace std;

const int maxN = 51;
long long power2[maxN];

long long mostRank(long long K, int N) {
	long long val = 0;
	while (K > 0 && N >= 1) {
		val += power2[N - 1];
		K = K - K / 2 - 1;
		-- N;
	}
	return val;
}

long long leastRank(long long K, int N) {
	long long val = 0;
	while (N >= 1) {
		if (K == power2[N] - 1) {
			val += power2[N - 1];
			K = power2[N - 1] - 1;
		} else 
			K = (K + 1) / 2;
		-- N;
	}
	return val;
}

int main() {
	power2[0] = 1;
	for (int i = 1; i <= 50; ++ i)
		power2[i] = power2[i - 1] << 1;
	int T;
	cin >> T;
	for (int tcase = 1; tcase <= T; ++ tcase) {
		long long N, P;
		cin >> N >> P;
		long long left = 0;
		long long right = power2[N] - 1;
		while (left <= right) {
			long long mid = (left + right) >> 1;
			if (mostRank(mid, N) >= P)
				right = mid - 1;
			else left = mid + 1;
		}
		cout << "Case #" << tcase << ": " << left - 1; 
		left = 0;
		right = power2[N] - 1;
		while (left <= right) {
			long long mid = (left + right) >> 1;
			if (leastRank(mid, N) < P)
				left = mid + 1;
			else right = mid - 1;
		}
		cout << " " << left - 1 << endl;
	}
	return 0;
}
