#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <ctime>
using namespace std;
unsigned long long int convert(unsigned long long int str, unsigned long long int base) {
	unsigned long long int digit = 0;
	unsigned long long int final = 0;
	while (str != 0) {
		unsigned long long int rem = str % 10;
		str /= 10;
		final += rem * pow(base, digit);
		digit++;
	}
	return final;
}
bool checkPrime(unsigned long long int number, unsigned long long int &divisor) {
	unsigned long long int max = ceil(sqrt(number));
	for (unsigned long long int i = 2; i < max; i++) {
		if (number % i == 0) {
			divisor = i;
			return false;
		}
	}
	return true;
}
unsigned long long int generateNumber(unsigned long long int hasGenerated, unsigned long long int length) {
	string number;
	number.clear();
	number.push_back('1');
	for (unsigned long long int i = 2; i < length; i++) {
		if (rand() % 2 == 0)
			number.push_back('0');
		else
			number.push_back('1');
	}
	number.push_back('1');
	
	unsigned long long int result = 0;
	for (int i = 0; i < length; i++)
		result += (int)(number.at(i) - '0') * pow(10, i);
	return result;
}
int main(void) {
	unsigned long long int T, N, J;
	unsigned long long int count = 0;
	unsigned long long int hasGeneratedNum = 0;
	vector<unsigned long long int> hasGenerated;

	srand(time(NULL));
	cin >> T >> N >> J;
	cout << "Case #1:" << endl;
	while (count < J) {
		unsigned long long int number = generateNumber(hasGeneratedNum, N);
		if (find(hasGenerated.begin(), hasGenerated.end(), number) != hasGenerated.end())
			continue;
		hasGenerated.push_back(number);
		bool isPrime = false;
		unsigned long long int nonTrivialDivisor[9] = { -1 };
		for (unsigned long long int i = 2; i <= 10; i++) {
			unsigned long long int convertedNumber = convert(number, i);
			if (checkPrime(convertedNumber, nonTrivialDivisor[i - 2])) {
				isPrime = true;
				break;
			}
		}
		if (!isPrime) {
			cout << number;
			for (unsigned long long int i = 0; i < 9; i++)
				cout << " " << nonTrivialDivisor[i];
			cout << endl;
			count++;
		}
		hasGeneratedNum++;
	}
	return 0;
}