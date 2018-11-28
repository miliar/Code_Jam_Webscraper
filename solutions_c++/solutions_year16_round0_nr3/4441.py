#include <iostream>
#include <bitset>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>

using namespace std;

bool isPrime(long int num);
bool isValid(long int num);
void checkTestCase(unsigned int N, unsigned int J);
long binaryToBase(string binary, int base);
vector<int> findDivisors(string binary);

int main() {
	int testCases = 0;
	cin >> testCases;
	int testCasesNArr[testCases];
	int testCasesJArr[testCases];
	for(int i = 0; i < testCases; i++) {
		cin >> testCasesNArr[i];
		cin >> testCasesJArr[i];
	}
	for(int i = 0; i < testCases; i++) {
		cout << "Case #" << i + 1 << ": " << endl;
		checkTestCase(testCasesNArr[i], testCasesJArr[i]);
	}
	return 0;
}

void checkTestCase(unsigned int N, unsigned int J) {
	unsigned int asdf = 0;
	int count = 0;
	asdf |= 1 << 0;
	asdf |= 1 << (N - 1);
	//go through all the posibilities? 
	while(!((asdf >> N) & 1) && J > count) {
		vector<int> values = findDivisors(bitset<16>(asdf).to_string());
		if(values.size() == 9) {
			count++;
			cout << bitset<16>(asdf).to_string();
			for(int i = 0; i < values.size(); i++) {
				cout << ' ' << values[i];
			}
			cout << endl;
		}
		asdf += 2;
	}
}

vector<int> findDivisors(string binary) {
	vector<int> values;
	for(int i = 2; i <= 10; i++) {
		long int temp = binaryToBase(binary, i);
		for(int j = sqrt(sqrt(temp)) + 1; j < sqrt(temp); j++) {
			if(temp % j == 0) {
				values.push_back(j);
				break;
			}
		}
	}
	return values;
	cout << endl;
}

long binaryToBase(string binary, int base) {
	long decimal = strtol(binary.c_str(), NULL, base);
	return decimal;
}

