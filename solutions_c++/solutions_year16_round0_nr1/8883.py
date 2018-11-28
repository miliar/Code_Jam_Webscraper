#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int sol(unsigned long n ) {
	unsigned long j;
	unsigned long h = 0;
	unsigned long i = 1;
	const unsigned long mask = 0x03ff;
	if (n) {
		while (1) {
			j = i * n;
			while (j > 9) {
				h |= 0x01 << (j % 10);
				j /= 10;
			}
			h |= 0x01 << j;
			//printf("i = %d, i * n = %d, h = %x\n", i, i * n, h);
			if (mask == h)
				return i * n;
			++i;
		}
	}
	return -1;
}

int main() {
	unsigned long t, n, answer;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n
		answer = sol(n);
		if (answer == -1)
			cout << "Case #" << i << ": INSOMNIA" << endl;
		else 
			cout << "Case #" << i << ": " << answer << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
	return 0;
}
