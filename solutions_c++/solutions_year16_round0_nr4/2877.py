#include <iostream>

using namespace std;

void impossible() {
	cout << " IMPOSSIBLE";
}

void sequence(size_t max, size_t number) {
	for (size_t i = max; number > 0; --i, --number) {
		cout << ' ' << i;
	}
}

void process(size_t k, size_t c, size_t s) {
	if (c == 1) {
		if (k == s) {
			sequence(k, k);
		} else {
			impossible();
		}
	} else {
		if (s >= k-1) {
			sequence(k, s);
		} else {
			impossible();
		}
	}
}

int main(int argc, char** argv) {
	size_t inputCount;
	cin >> inputCount;
	for (size_t inputNumber = 1; inputNumber <= inputCount; ++inputNumber) {
		size_t k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << inputNumber << ":";
		process(k,c, s);
		cout << endl;
	}
	return 0;
}
