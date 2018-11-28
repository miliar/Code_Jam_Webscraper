#include <iostream>
#include <vector>
using namespace std;

int N;
long long P, N2;

long long worst(long long n) {
	long long remBetter = n, remWorse = N2-1 - n;
	long long out = 0;
	int rounds = 0;
	while (rounds < N) {
		++rounds;
		out <<= 1;
		if (remBetter > 0) {
			// lose
			out |= 1;
			--remBetter;

			if (remWorse & 1) {
				--remBetter;
				++remWorse;
			}
			remWorse >>= 1;
			remBetter >>= 1;
		}
		else {
			// win
			// (keep winning)
		}
	}
	return out;
}

long long best(long long n) {
	long long remBetter = n, remWorse = N2-1 - n;
	long long out = 0;
	for (int rounds = 0; rounds < N; ++rounds) {
		out <<= 1;
		if (remWorse > 0) {
			// win
			--remWorse;
			if (remWorse & 1) {
				++remBetter;
				--remWorse;
			}
			remWorse >>= 1;
			remBetter >>= 1;
		}
		else {
			// lose
			// (keep losing)
			out |= 1;
		}
	}
	return out;
}

void solve() {
	cin >> N >> P;
	N2 = 1LL << N;

	{
		long long low = 0, high = N2;
		while (low + 1 < high) {
			long long mid = (low + high) / 2;
			if (worst(mid) < P)
				low = mid;
			else
				high = mid;
		}
		cout << low << ' ';
	}
	{
		long long low = 0, high = N2;
		while (low + 1 < high) {
			long long mid = (low + high) / 2;
			if (best(mid) < P)
				low = mid;
			else
				high = mid;
		}
		cout << low << endl;
	}
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
