#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

string gen_coin_candidate(int i, int length);
unsigned long long bin_convert(string coin, int base);
unsigned long long get_min_divisor(unsigned long long n, vector<int>* prime_list);

int main()
{
	// Get list of primes. //2147483649
	vector<bool> sieve(32769, true);
	sieve[0] = false;
	sieve[1] = false;
	int siever = 2;
	while (siever <= 182) {
		int start = siever * siever;
		for (int i = start; i < 32769; i += siever) {
			sieve[i] = false;
		}

		for (int i = siever + 1; i < 32769; ++i) {
			if (sieve[i] == true) {
				siever = i;
				break;
			}
		}
	}

	vector<int> prime_list;
	for (int i = 0; i < 32769; ++i) {
		if (sieve[i] == true) {
			prime_list.push_back(i);
		}
	}

	ofstream f_primes("primes.txt");
	for (auto itr = prime_list.begin(); itr != prime_list.end(); ++itr) {
		f_primes << to_string(*itr) << endl;
	}
	f_primes.flush();
	f_primes.close();


	// Initialize: open file for read, create variables, etc.
	ifstream f_in("input.txt");
	ofstream f_out("output.txt");
	string str_buf;

	// Read input parameters.
	getline(f_in, str_buf);
	int T = atoi(str_buf.c_str());
	getline(f_in, str_buf, ' ');
	int N = atoi(str_buf.c_str());
	getline(f_in, str_buf, ' ');
	int J = atoi(str_buf.c_str());

	// Calculate J different jamcoins of length N.
	vector<string> coins;

	f_out << "Case #1:" << endl;
	// Start at i = 3 because 2 is the smallest prime number (base 10).
	for (int i = 0; coins.size() < static_cast<unsigned int>(J); ++i) {
		string coin_candidate = gen_coin_candidate(i, N);
		bool is_jamCoin = true;
		vector<int> divisors;

		for (int base = 2; base <= 10; ++base) {
			unsigned long long converted = bin_convert(coin_candidate, base);
			unsigned long long min_divisor = get_min_divisor(converted, &prime_list);
			if (min_divisor < converted) {
				divisors.push_back(min_divisor);
			} else {
				is_jamCoin = false;
				break;
			}
		}

		if (is_jamCoin) {
			cout << coin_candidate << endl;
			coins.push_back(coin_candidate);
			f_out << coin_candidate;
			for (auto itr = divisors.begin(); itr != divisors.end(); ++itr)
				{ f_out << " " << to_string(*itr); }
			f_out << endl;
		}
	}

	// Cleanup: close files.
	f_in.close();
	f_out.flush();
	f_out.close();

	return 0;
}



string gen_coin_candidate(int i, int length)
{
	string output = "";
	int length_gen = length - 2;
	for (int j = 0; j < length_gen; ++j) {
		output += to_string(i % 2);
		i /= 2;
	}
	output = "1" + output + "1";
	return output;
}



unsigned long long bin_convert(string coin, int base)
{
	unsigned long long coin_dec = 0;
	unsigned long long digit_val = 1;
	for (auto itr = coin.rbegin(); itr != coin.rend(); ++itr, digit_val *= base) {
		string digit(itr, itr+1);
		coin_dec += digit_val * atoi(digit.c_str());
	}

	return coin_dec;
}



unsigned long long get_min_divisor(unsigned long long n, vector<int>* prime_list)
{
	unsigned long long min_divisor = n;
	//for (int i = 0; (*prime_list)[i] < n; ++i) {
	for (unsigned long long i = 0; (*prime_list)[i] < 182; ++i) {
		unsigned long long prime = (*prime_list)[i];
		if (n % prime == 0) {
			min_divisor = prime;
			break;
		}
	}

	return min_divisor;
}
