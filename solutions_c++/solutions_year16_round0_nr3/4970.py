#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <stdint.h>
#include <random>
using namespace std;

char prime_table[1 << 17];


void genPrimeTable()
{
	memset(prime_table, 1, 1 << 17);
	for (int i = 2; i < 1 << 17; ++i) {
		if (prime_table[i] == 0) {
			continue;
		}
		for (int j = i * 2; j < 1 << 17; j += i) {
			prime_table[j] = 0;
		}
	}
}

bool isPrime(int64_t n, int64_t& factor) {
	for (int64_t i = 2; i * i <= n; ++i) {
		if (n % i == 0) {
			factor = i;
			return false;
		}
	}
	factor = 1;
	return true;
}

bool passTest(int64_t d, vector<int64_t>& digits, vector<int64_t>& factors) {
	//vector<int> digits;
	while (d != 0) {
		digits.push_back(d % 2);
		d /= 2;
	}
	vector<int64_t> nums;
	for (int64_t i = 2; i <= 10; ++i) {
		int64_t n = 0;
		for (int64_t j = digits.size() - 1; j >= 0; --j) {
			n = n * i + digits[j];
		}
		nums.push_back(n);
		//printf("%d\n", n);
	}
	//vector<int> factors;
	for (int64_t n : nums) {
		int64_t factor;
		if (isPrime(n, factor)) {
			return false;
		}
		factors.push_back(factor);
	}
}

int main()
{


	int N = 16;
	int J = 50;

	set<int> result;

	ofstream f_out("c_small.out");
	f_out << "Case #1:\n";
	std::random_device rd;     // only used once to initialise (seed) engine
	std::mt19937 rng(0);    // random-number engine used (Mersenne-Twister in this case
	std::uniform_int_distribution<int> uni(0, 1 << (N - 2)); // guaranteed unbiased
	for (int i = 0; i < J; ++i) {
		printf("i %d\n", i);
		while (true) {
			int random_int = uni(rng);
			int64_t d = (1 << (N - 1)) | (random_int << 1) | 1;
			//cout << d << "\n";
			vector<int64_t> digits;
			vector<int64_t> factors;
			if (passTest(d, digits, factors) && result.find(d) == result.end()) {
				result.insert(d);
				for (int i = digits.size() - 1; i >= 0; --i) {
					f_out << digits[i];
				}
				for (int i = 0; i < factors.size(); ++i) {
					f_out << " " << factors[i];
				}
				f_out << "\n";
				break;
			}
		}
	}


	system("pause");
	return 0;

}