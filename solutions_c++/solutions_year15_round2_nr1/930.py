#include <iostream>
#include <algorithm>
using namespace std;

unsigned long long int solve(unsigned long long int n) {
	unsigned long long int cost = 0;

	while (n > 10) {
		if (n % 10 == 0) {
			cost++;
			n--;
		} else if (n % 10 > 1) {
			cost += n % 10 - 1;
			n = n - n % 10 + 1;
		} else {
			string s = to_string(n);
			string next = s;

			for (size_t i = s.size() / 2; i < s.size() - 1; i++) {
				next[i] = '0';
			}

			string rnext = next;
			reverse(rnext.begin(), rnext.end());

			if (rnext < s) {
				cost += n - stoull(next) + (next != rnext);
				n = stoull(rnext);
			} else {
				cost++;
				n--;
			}
		}
	}

	return cost + n;
}

int main(void) {
	int numCases;

	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		unsigned long long int N;

		cin >> N;
		cout << "Case #" << numCase << ": " << solve(N) << endl;
	}
}