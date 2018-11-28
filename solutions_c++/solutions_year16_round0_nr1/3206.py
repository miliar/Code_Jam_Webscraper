// Syed Ghulam Akbar
// CodeJam 2016

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {
		
		// Read the initial number
		long N;
		cin >> N;

		int digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		int matches = 0;
		int steps = 0;
		long Num = N;

		// Keep counting until, hopefully, the sheel sleeps
		while (true) {
			if (Num <= 0) break;

			// Check if any new digits are found in this new number
			long temp = Num;
			while (temp > 0) {
				int digit = temp % 10;
				temp = temp / 10;

				// Check if this digit is already found or new one
				if (digits[digit] == 0) {
					digits[digit] = 1;
					matches++;
				}
			}

			// if all digits are found, the sheep must be sleep by now
			if (matches == 10)
				break;

			// Now increment the number
			steps++;
			Num = N * steps;
		}

		cout << "Case #" << test << ": ";
		if (Num <= 0)
			cout << "INSOMNIA";
		else
			cout << Num;
		cout << "\n";
	}
}
