#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <iterator>
#include <vector>
#include <cmath>

using namespace std;

int pancakes(string stack);
long long isPrime(long long input);
void jamcoins(int length, int number);

int main() {
	int num_test_cases;
	string line;
	getline(cin, line);
	istringstream convert(line);
	convert >> num_test_cases;

	int c_len = 0;
	int c_num = 0;
	getline(cin, line);

	vector<string> tokens;

    istringstream iss(line);
	copy(istream_iterator<string>(iss),
		     istream_iterator<string>(),
			      back_inserter(tokens));

	istringstream converter1(tokens[0]);
	converter1 >> c_len;
	istringstream converter2(tokens[1]);
	converter2 >> c_num;

	/*
	cout << "Num cases: " << num_test_cases << endl;
	cout << "Len: " << c_len << endl;
	cout << "Num_coins: " << c_num << endl;
	*/
	for (int i = 0; i < num_test_cases; i++) {
		cout << "Case #" << i+1 << ": " << endl;
		jamcoins(c_len, c_num);
	}
	return 0;
}

void print_jamcoin(vector<bool> &coin) {
	// Print pancake
	for (bool b : coin) {
		cout << b;
	}
	//cout << endl;
	return;
}

void find_jamcoins(vector<bool> coin, int index, int length, int number, int *num_found) {
	if (*num_found >= number) {
		return;
	}
	if (index == length - 1) {
		//cout << "found: " << *num_found << endl;
		//cout << endl;
		//print_jamcoin(coin);
		//cout << endl;
		//cout << "--------" << endl;
		bool isjamcoin = true;
		vector<int> divisors(9,0); // 10 ints with value 0
		for (int i = 2; i <= 10; i++) {
			// Get jamcoin in proper base
			long long base_num = 0;
			for(int j = 0; j < length; j++) {
				base_num += coin[length - 1 - j] * pow(i, j);
			}
			divisors[i-2] = isPrime(base_num);
			//cout << "Base " << i << ": " << base_num << " " << divisors[i-2] << endl;
			if (divisors[i-2] == 1) {
				isjamcoin = false;
				//cout << "Not Jamcoin" << endl;
			}
			if (!isjamcoin) { break; }
		}
		if (isjamcoin) {
			*num_found += 1;
			print_jamcoin(coin); 
			cout << " ";
			for(int d : divisors) {
				cout << d << " ";
			}
			cout << endl;
		}
		return;
	}
	vector<bool> coin1 = coin;
	vector<bool> coin2 = coin;
	coin1[index] = 0;
	coin2[index] = 1;
	find_jamcoins(coin1, index + 1, length, number, num_found);
	find_jamcoins(coin2, index + 1, length, number, num_found);
	return;
}

void jamcoins(int length, int number) {
	vector<bool> coin(length);
	coin[0] = coin[length-1] = 1;
	int *num_coins_found = (int*) malloc(sizeof(int));
	*num_coins_found = 0;
	find_jamcoins(coin, 1, length, number, num_coins_found);
	return;
}

// Returns a nontrivial divisor of input or 1 if prime
long long isPrime(long long input) {
	for(long long i = 2; i <= sqrt(input); i++) {
		if(input%i == 0) {
			return i;
		}
	}
	return 1;
}
