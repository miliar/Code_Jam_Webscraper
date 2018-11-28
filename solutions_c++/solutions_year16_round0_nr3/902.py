#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <string>

using namespace std;

int n, j, t;
long long start_coin, finish_coin;
long long n_found;
vector <long long> divisors(11);
vector <long long> ans_coins;
vector <vector <long long> > ans_divisors;


string to_binary(long long x) {
	string res = "";
	while (x > 0) {
		res = to_string(x % 2) + res;
		x = x / 2;
	}
	return res;
}

bool check(long long x) {
	//cout << "CHECK" << endl;
	//cout << to_binary(x) << endl;
	for (int k = 2; k <= 10; k++) {
		long long bit_mask = x;
		long long number = 0;
		long long cur_k = 1;
		while (bit_mask > 0) {
			long long d = bit_mask % 2;
			bit_mask = bit_mask / 2;
			number += d * cur_k;
			cur_k *= k;
		}
		bool prime = true;
		for (long long j = 2; j * j <= number; ++j) {
			if (number % j == 0) {
				//cout << k << ' ' << number << ' ' << j << endl;
				divisors[k] = j;
				prime = false;
				break;
			}
		}
		if (prime)
			return false;
	}
	return true;
}


int main()
{
	n = 16;
	j = 50;
	start_coin = (1 << (n - 1)) + 1;
	finish_coin = (1 << n) + 1;
	n_found = 0;
	for (long long cur_coin = start_coin; cur_coin <= finish_coin; cur_coin += 2) {
		if (check(cur_coin)) {
			//cout << "Found " << to_binary(cur_coin) << ' ' << divisors.size() << endl;
			ans_coins.push_back(cur_coin);
			ans_divisors.push_back(divisors);
			n_found += 1;
		}
		if (n_found == j)
			break;
	}
	cout << "Case #1:\n";
	for (long long i = 0; i < ans_divisors.size(); ++i) {
		cout << to_binary(ans_coins[i]) << ' ';
		for (long long j = 2; j <= 10; ++j)
			cout << ans_divisors[i][j] << ' ';
		cout << endl;
	}
}