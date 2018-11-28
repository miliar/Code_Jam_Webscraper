#include <iostream>
#include <string>
#include <bitset>
#include <cmath>
#include <vector>

int caseNumber = 1;
using namespace std;



void printResult (unsigned N, unsigned J) {
	cout << "Case #" << caseNumber << ":" << "\n";
	string str;
	unsigned long long base2value = pow(2,N - 1) + 1;
	unsigned long long baseInter;
	
	bool foundPrime;
	bool foundDivisor;
	
	unsigned long long sqBI;
	unsigned long long divisors[11];

	while (J != 0) {
		foundPrime = false;

		bitset<16> bs(base2value);
		str = bs.to_string();
		for (int i = 2; i != 11; ++i) {
			foundDivisor = false;

			baseInter = stoull(str, NULL, i);
			sqBI = sqrt(baseInter) + 1;

			for (unsigned long long j = 3; j < sqBI; ++j) {
				if (baseInter % j == 0) {
					foundDivisor = true;
					divisors[i] = j;
					break;
				}
			}

			if (!foundDivisor) {
				foundPrime = true;
				break;
			}
		}

		if (!foundPrime) {
			cout << bs;
			for (int i = 2; i != 11; ++i) {
				cout << " " << divisors[i];
			}
			cout << "\n";
			--J;
		}

		base2value += 2;

	}
}
	
	

int main() {
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	unsigned N, J;
	if (T == 0) {
		return 0;
	}

	++T;

	while(caseNumber != T) {
		cin >> N;
		cin >> J;
		printResult(N, J);
		++caseNumber;
	}
}