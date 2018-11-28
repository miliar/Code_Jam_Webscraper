#include <iostream>

using namespace std;

const long long target = (1 << 10) - 1;

long long derive_mask(long long n) {
	long long mask = 0;
	long long curr = n;
	while (curr) {
		int d = curr % 10;
		curr /= 10;
		mask |= (1 << d);
	}
	return mask;
}

long long process_case() {
	long long input_number;
	cin >> input_number;
	if (!input_number)
		return 0;
	long long mask = 0;
	long long curr = input_number;
	// int result = 0;
	while (mask != target) {
		mask |= derive_mask(curr);
		// ++result;
		curr += input_number;
	}
	return curr - input_number;
}

int main() {
	int test_count;
	cin >> test_count;
	for (int i = 1; i <= test_count; ++i) {

		long long result = process_case();
		if (result == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
			cerr << "Case #" << i << ": INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << i << ": " << result << endl;
			cerr << "Case #" << i << ": " << result << endl;
		}
	}

	return 0;
}
