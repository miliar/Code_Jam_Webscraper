//A.cpp


#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

int parseNum(int n) {
	int allBits = 0;
	do {
		int digit = n % 10;
		if (0 == digit) {
			allBits |= (1<<9);
		} else {
			allBits |= (1<<(digit-1));
		}

		n = n/10;
	} while (n > 0);
	return allBits;
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		long long int N;
		cin >> N;

		if (N == 0) {
			cout << "Case #" << t+1 << ": INSOMNIA\n";
			continue;
		}

		int sleep = 0;
		int next = N;
		while (sleep < 1023) {
			sleep |= parseNum(next);
			next += N;
		}

		cout << "Case #" << t+1 << ": " << next-N << endl;

	}

	return 0;
}