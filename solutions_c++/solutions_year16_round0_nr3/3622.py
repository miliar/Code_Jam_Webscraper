#include <iostream>
using namespace std;

void findJamcoins(int, int, long long, int, int &);
long long convertFromBase(long long, int, int);
long long findDivisor(long long);


int main() {
	int T;
	cin >> T;
	int N, J;
	int numOfCoins;
	for(int count = 1; count <= T; ++count) {
		cin >> N >> J;
		numOfCoins = 0;
		cout << "Case #" << count << ":" << endl;
		findJamcoins(N, 0, 0, J, numOfCoins);
	}

	return 0;
}

void findJamcoins(int N, int addedSoFar, long long numSoFar, int J, int & numOfCoins) {
	if(numOfCoins == J)
		return;

	if(addedSoFar == N) {
		long long base2Div = findDivisor(convertFromBase(numSoFar, 2, N));
		if(base2Div == -1)
			return;
		long long base3Div = findDivisor(convertFromBase(numSoFar, 3, N));
		if(base3Div == -1)
			return;
		long long base4Div = findDivisor(convertFromBase(numSoFar, 4, N));
		if(base4Div == -1)
			return;
		long long base5Div = findDivisor(convertFromBase(numSoFar, 5, N));
		if(base5Div == -1)
			return;
		long long base6Div = findDivisor(convertFromBase(numSoFar, 6, N));
		if(base6Div == -1)
			return;
		long long base7Div = findDivisor(convertFromBase(numSoFar, 7, N));
		if(base7Div == -1)
			return;
		long long base8Div = findDivisor(convertFromBase(numSoFar, 8, N));
		if(base8Div == -1)
			return;
		long long base9Div = findDivisor(convertFromBase(numSoFar, 9, N));
		if(base9Div == -1)
			return;
		long long base10Div = findDivisor(convertFromBase(numSoFar, 10, N));
		if(base10Div == -1)
			return;

		cout << numSoFar << " " << base2Div << " " << base3Div << " " << base4Div << " " 
		<< base5Div << " " << base6Div << " " << base7Div << " " << base8Div << " " 
		<< base9Div << " " << base10Div << endl;
		numOfCoins = numOfCoins + 1;
		return;
	}


	if(addedSoFar != 0 && addedSoFar != N - 1)
		findJamcoins(N, addedSoFar + 1, numSoFar*10, J, numOfCoins);
		
	findJamcoins(N, addedSoFar + 1, numSoFar*10 + 1, J, numOfCoins);
}

long long convertFromBase(long long n, int base, int numOfDigits) {
	long long result = 0;
	long long divisor = 1;
	for(int i = 0; i < numOfDigits - 1; ++i) {
		divisor = divisor * 10;
	}

	int digit;
	while(divisor > 0) {
		digit = (n/divisor) % 10;
		result = result * base + digit;
		divisor = divisor/10;
	}

	return result;

}

long long findDivisor(long long n) {
	if(n <= 2)
		return -1;

	for(long long i = 2; i*i <= n; ++i) {
		if(n % i == 0)
			return i;
	}

	return -1;
}