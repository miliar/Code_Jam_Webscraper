#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>
#include <set>

std::vector<long long> primes;


std::string bin(long long input) {
	std::stringstream ss;
	ss << std::hex << input;

	std::string hexNum = ss.str();
	std::stringstream out;

	for (int i = 0; i < hexNum.size(); ++i) {
		switch (hexNum.at(i)) {
		case '0':
			out << "0000";
			break;
		case '1':
			out << "0001";
			break;
		case '2':
			out << "0010";
			break;
		case '3':
			out << "0011";
			break;
		case '4':
			out << "0100";
			break;
		case '5':
			out << "0101";
			break;
		case '6':
			out << "0110";
			break;
		case '7':
			out << "0111";
			break;
		case '8':
			out << "1000";
			break;
		case '9':
			out << "1001";
			break;
		case 'a':
		case 'A':
			out << "1010";
			break;
		case 'b':
		case 'B':
			out << "1011";
			break;
		case 'c':
		case 'C':
			out << "1100";
			break;
		case 'd':
		case 'D':
			out << "1101";
			break;
		case 'e':
		case 'E':
			out << "1110";
			break;
		case 'f':
		case 'F':
			out << "1111";
			break;
		}
	}

	return out.str();
}

long long nextPrime(long long p) {
	while (1) {
		++p;
		bool isPrime = true;
		for (int i = 0; i < primes.size(); ++i) {
			if (p % primes[i] == 0) {
				isPrime = false;
				break;
			}
		}
		if (isPrime) {
			primes.push_back(p);
			return p;
		}
	}

}

long long changeBase(std::string& binary, int base) {
	long long number = 0;

	long long mult = 1;
	for (int i = binary.size() - 1; i >= 0; --i) {
		if (binary.at(i) == '1') number += mult;
		mult *= base;
	}

	return number;
}

long long divisor(std::string& binary, long long base) {
	long long number = 0;

	long long mult = 1;
	for (int i = binary.size() - 1; i >= 0; --i) {
		if (binary.at(i) == '1') number += mult;
		mult *= base;
	}

	long long thresh = number / 2;
	long long p;

	for (int i = 0; i < primes.size(); ++i) {
		p = primes[i];
		if (p * p > thresh) return 1;
		if (number % p == 0) return p;
	}

	long long next = nextPrime(p);

	while (next * next <= thresh) {
		if (number % next == 0) return next;

		next = nextPrime(next);
	}

	return 1;
}

int main() {

	primes.push_back(2);
	long long t, n, j;
	std::cin >> t >> n >> j;

	long long orig = pow(2, n - 1) + 1;
	long long check = pow(2, n - 1) + 1;

	std::vector<std::vector<long long> > table;
	std::set<long long> hits;

	int mult = 1;
	bool setup = false;
	std::set<long long>::iterator it;
	while (table.size() < j) {

		std::string binary = bin(check);

		std::vector<long long> coin;
		coin.push_back(check);

		bool success = true;
		for (int i = 2; i <= 10; ++i) {
			long long div = divisor(binary, i);

			if (div == 1) {
				success = false;
				break;
			}

			coin.push_back(div);
		}

		if (success && !hits.count(check)) {
			hits.insert(check);
			table.push_back(coin);
		}

		check = orig + 210 * mult;
		if (table.size() >= 49) {
			if (!setup) it = hits.begin();
			check = *it + 30;
			++it;
		}

		++mult;

	}

	std::cout << "Case #1:" << std::endl;

	for (int i = 0; i < table.size(); ++i) {
		std::cout << bin(table[i][0]);
		for (int k = 1; k < table[i].size(); ++k) {
			std::cout << ' ' << table[i][k];
		}
		std::cout << std::endl;
	}


	return 0;
}
