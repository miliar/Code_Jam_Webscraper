#include <iostream>
#include <set>

using namespace std;

long getMax(int N)
{
	long max = N;
	while (N) {
		max *= 100;
		N /= 10;
	}
	return max;
}

int main(int argc, char *argv[])
{
	int T;
	set<int> digits;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int N;
		cin >> N;
		if (N == 0) {
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}
		long max = getMax(N), acc = N;
		digits.clear();
		while (digits.size() != 10) {
			int tmp = acc;
			while (acc) {
				digits.insert(acc % 10);
				acc /= 10;
			}

			acc = tmp + N;
			if (acc > max) {
				break;
			}
		}

		cout << "Case #" << i + 1<< ": ";
		if (digits.size() != 10) {
			cout << "INSOMNIA" << endl;
		} else {
			cout << acc - N << endl;
		}
	}

	return 0;
}

