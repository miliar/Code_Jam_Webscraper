#include <algorithm>
#include <iostream>
#include <iterator>
#include <bitset>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

#define TYPE unsigned long long
#define f(i, N) for(unsigned i = 0; i < N; ++i)
#define fr(i, N) for(int i = N-1; i >= 0; --i) // reverse
#define ff(i, j, N) for(unsigned i = 0; i < N; ++i) for(unsigned j = 0; j < N; ++j)
#define V vector<TYPE>


TYPE power(unsigned n, unsigned k) {
	// n<= 100, 0 < k <= 100, n^k <= 10^18;
	TYPE r = n;
	while (--k) {
		r *= n;
	}
	return n; 
}


void solve(unsigned K, unsigned C, unsigned S)
{
	if (C == 1) {
		if (S < K) cout << "IMPOSSIBLE";
		else {
			f(i, K) {
				cout << i + 1 << " ";
			}
		}
		return;
	}

	TYPE KCm1 = power(K, C - 1);
	f(i, K / 2) {
		auto r = 2 * i*KCm1 + 2 * (i + 1);
		cout << r << " ";
	}
	if (K % 2 == 1) {
		cout << K*KCm1;
	}
}

int main() {
	unsigned T = 1;
	cin >> T;
	unsigned K, C, S;
	f(t, T) {
		cin >> K >> C >> S;
		try {
			cout << "Case #" << t + 1 << ": ";
			solve(K, C, S);
			cout << endl;
		}
		catch (const std::exception& e) {
			cout << e.what() << endl;
		}
		catch (...) {
			cout << "Unknown exception" << endl;
		}
	}
}