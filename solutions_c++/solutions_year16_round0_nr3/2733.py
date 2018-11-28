// Syed Ghulam Akbar
// CodeJam 2016

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iomanip>      // std::setprecision
#include <string>
#include <math.h>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {
		long N, J;

		// Read the problem input
		cin >> N >> J;

		// Make the lower and higher ranges. For example, if the N is 5 
		// then low = 10001 and hight = 11111 in binary
		long long low = pow((double)2, (double)N-1) + 1;
		long long high = pow((double)2, (double)N) - 1;

		char stringValue[100];

		// For best performance, generate Sieve prime before any input processing
		unsigned long upperBound = pow((double)2, (double)20);
		long upperLimit = (int)sqrt((double)upperBound);
		bool *isComposite = new bool[upperBound + 1];
		long *primerDiviser = new long[upperBound + 1];
		memset(isComposite, 0, sizeof(bool) * (upperBound + 1));
		for (long m = 2; m <= upperLimit; m++) {
			if (!isComposite[m]) {
				for (int k = m * m; k <= upperBound; k += m) {
					isComposite[k] = true;
					primerDiviser[k] = m;
				}
			}
		}

		int matchCount = 0;
		std::cout << "Case #" << test << ":" << "\n";

		// Check for all the numbers in this range for Coin Jam
		for (long long val = low; val < high; val = val +2) {
			
			// Make a binary string of this number 
			ultoa(val, stringValue, 2);
			//strcpy(stringValue, "1001");

			// Now check this number in all 10 bases and check if this is valid
			// jamcoin or not
			int nonPrimeCount = 0;
			long long baseNumbers[12];

			for (int i=2; i<11; i++) {
				
				// Convert this number to required base number system
				long long baseNum = 0;
				for (int j=0; j < strlen(stringValue); j++) {
					int digit = stringValue[j] == '1' ? 1 : 0;
					baseNum = baseNum * i + digit;
				}

				// Check if the number is prime
				bool isPrime = true;
				long divider = 0;
				long upperLimit = (long)sqrt((double)baseNum);
				for (long m = 2; m <= upperLimit; m++) {
					if (baseNum % m == 0) {
						isPrime = false;
						divider = m;
						break;
					}
				}

				// Check if this number is prime
				//if (isComposite[baseNum]) {
				if (!isPrime) {
					nonPrimeCount++;
					baseNumbers[i] = divider;
				}
				else
					break;
			}

			// if this number is prime in all bases
			if (nonPrimeCount == 9) {
				matchCount++;

				// Print the result
				cout << stringValue << " ";

				// Print all the proof numbers that this number is prime in all bases
				for (int i=2; i<11; i++) {
					cout << baseNumbers[i] << " ";
				}

				cout << "\n";

				// All required data if found
				if (matchCount >= J)
					break;
			}
		}
		
		// Release resources
		delete [] isComposite;
	}
}
