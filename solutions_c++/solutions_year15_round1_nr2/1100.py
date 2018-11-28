#include <iostream>

using namespace std;

const long MAXINT = 0x7fffffffffffffff;
int main()
{
	int T;
	cin >> T;
	for (int casenum = 1; casenum <= T; ++casenum) {
		int B, N;
		cin >> B >> N;
		long btimes[B];
		double rate = 0.0;
		for (int i = 0; i < B; ++i) {
			cin >> btimes[i];
			rate += 1.0/btimes[i];
		}
		long n = B;
		long at = (N-B)/rate;
		for (int i = 0; i < B; ++i) {
			n += (at-1)/btimes[i];
		}
		int barber = 0;
		while (n < N) {
			for (int i = 0; i < B; ++i) {
				if (at%btimes[i] == 0) {
					++n;
					if (n == N) {
						barber = i + 1;
						break;
					}
				}
			}
			++at;
		}
		--at;


		cout << "Case #" << casenum << ": " << barber << endl;
		n = B;
		for (int i = 0; i < B; ++i) {
			if (i < barber && at%btimes[i] == 0) ++n;
			n += (at-1)/btimes[i];
		}
		if (N != n) {
			cout << N << ':' << n << endl;
			return 0;
		}
	}
	return 0;
}

