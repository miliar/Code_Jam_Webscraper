#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <sstream>
#include <string>
using namespace std;

typedef unsigned long long ull;

void increment(string& num) {
	int idx = num.size() - 2;

	while (num.at(idx) != '0') idx--;
	string ones;
	ones.push_back('1');
	for (int i = 0; i < num.size() - idx - 2; i++) {
		ones.push_back('0');
	}
	ones.push_back('1');
	num.erase(idx, num.size() - idx);
	num = num + ones;
}

ull convertToBase(string num, int base) {
	ull number = 0;
	int count = 0;
	while(!num.empty()) {
		number += pow(base, count) * (static_cast<int>(num.at(num.size() - 1)) - 48);
		num.pop_back();
		count++;
	}
	return number;
}

bool isPrime(ull num, ull* div, int base) {
	vector<bool> numbers;
	for (ull i = 2; i <= (ull) sqrt(num); i++) {
		numbers.push_back(1);
	}
	for (ull i = 2; i <= (ull) sqrt(num); i++) {
		if (numbers[i - 2]) {
			if (num % i == 0) {
				//cout << num << " " << i << " " << num / i << endl;
				div[base - 2] = i;
				return false;
			} else {
				//cout << num << " " << i << endl;
				for (ull j = i; j < (ull) sqrt(num); j += i) numbers[j - 2] = 0;
			}
		}
	}
	return true;
}

int main() {
	int t, n, j;
	cin >> t >> n >> j;
	string num = "1000000000000001";
	cout << "Case #1:" << endl;
	ull compTest;
	bool jamcoin;
	ull divisors[9];
	while (j != 0) {
		//cout << num << endl;
		jamcoin = true;
		for (int i = 2; i <= 10; i++) {
			//cout << "Test1" << endl;
			compTest = convertToBase(num, i);
			//cout << "Test2 " << compTest << endl;
			if (isPrime(compTest, divisors, i)) {
				//cout << "Test3" << endl;
				jamcoin = false;
				break;
			}
		}
		if (jamcoin) {
			cout << num;
			for (int i = 0; i < 9; i++) cout << " " << divisors[i];
			cout << endl;
			j--;
		}
		//cout << "Test4" << endl;
		increment(num);
	}


	return 0;
}