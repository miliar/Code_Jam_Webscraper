// CoinJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <cmath>

using namespace std;


unsigned long long convertBase(string s, int base) {
	unsigned long long result = 0;

	for (int i = 0; i < s.length(); ++i) {
		if (s[s.length() - 1 - i] == '1')
		{
			result += (unsigned long long)pow(base, i);
		}
			
	}

	return result;
}

unsigned long long findDivisor(unsigned long long n) {
	for (unsigned long long i = 2; i <= sqrt(n); ++i) {
		if (n % i == 0) return i;
	}
	return 0;
}

vector<unsigned long long> check(string s) {
	vector<unsigned long long> divs;

	for (int i = 2; i <= 10; ++i) {
		unsigned long long num = convertBase(s, i);
		unsigned long long div = findDivisor(num);
		if (div != 0) {
			divs.push_back(div);
		} else {
			break;
		}
	}

	return divs;
}


int main()
{
	cout << "Case #1:" << endl;
	int t, n, j;
	cin >> t >> n >> j;

	unordered_set<string> seen;

	while (j > 0) {
		string s;

		s += '1';
		for (int i = 0; i < n-2; ++i) {
			int random = rand() % 2;
			s += (random + '0');
		}
		s += '1';

		if (!seen.count(s)) {
			vector<unsigned long long> divisors = check(s);
			seen.insert(s);

			if (divisors.size() == 9) {
				cout << s << " ";
				for (int i = 0; i < 9; ++i) {
					cout << divisors[i] << " ";
				}
				cout << endl;
				--j;
			}
		}
	}
    return 0;
}

