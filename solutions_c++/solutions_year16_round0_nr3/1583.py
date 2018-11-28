#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <BigInteger/BigInteger.hh>
#include <BigInteger/BigUnsignedInABase.hh>
#include <BigInteger/BigIntegerUtils.hh>

using namespace std;

struct TestCase {
	int len, count;
};

std::vector<TestCase> load(const std::string& s) {
	std::ifstream fs(s);
	if (!fs.is_open())
		std::cout << "Not found" << std::endl;

	int n;
	std::vector<TestCase> res;
	fs >> n;
	for (int i = 0; i < n; i++) {
		TestCase tc;
		fs >> tc.len >> tc.count;
		res.push_back(tc);
	}
	fs.close();
	return res;
}

#define PRIME_COUNT 1000
static int primes[PRIME_COUNT];


void loadPrimes(const std::string& s) {
	std::ifstream fs(s);
	if (!fs.is_open())
		std::cout << "Not found" << std::endl;

	int count = 0;
	while (fs.good()) {
		int nr;
		fs >> nr;
		primes[count] = nr;
		count++;
		if (count >= PRIME_COUNT)
			break;
	}
	fs.close();
}



BigInteger isqrt_impl(
	BigInteger n,
	BigInteger xk)
{
	BigInteger xk1 = (xk + n / xk) / 2;
	return (xk1 >= xk) ? xk : isqrt_impl(n, xk1);
}

BigInteger isqrt(BigInteger n)
{
	if (n == 0) return 0;
	return isqrt_impl(n, n);
}

BigInteger getDivisor(BigInteger nr) {
	BigInteger limit = isqrt(nr) + 1;
	for (int i = 1; i < PRIME_COUNT; i++) {
		if (nr % primes[i] == 0)
			return primes[i];
	}
	return -1;
}

BigInteger getDivisor2(BigInteger nr) {
	BigInteger limit = isqrt(nr) + 1;
	for (BigInteger i = 3; i <= limit; i += 2) {
		if (nr % i == 0)
			return i;
	}
	return -1;
}

unordered_set<long long> generatedComposites;

vector<BigInteger> checkBases(const string& nr) {
	vector<BigInteger> res;
	for (int base = 2; base <= 10; base++) {
		BigInteger check = BigUnsignedInABase(nr, base);
		BigInteger divisor = getDivisor(check);
		if (divisor == -1)
			return vector<BigInteger>();
		res.push_back(divisor);
	}
	return res;
}

std::string solve(TestCase& tc) {
	string base = string(tc.len, '1');
	for (size_t i = 1; i < base.length() - 1; i++)
		base[i] = '0';

	vector<pair<string, vector<BigInteger>>> res;
	unsigned long long baseLong = stoll(base, nullptr, 2);
	while (res.size() < (size_t)tc.count) {
		base = std::bitset<64>(baseLong).to_string().substr(64 - base.length(), base.length());
		vector<BigInteger> divisors = checkBases(base);
		if (divisors.size() > 0) {
			res.push_back(make_pair(base, divisors));
			std::cout << "Found " << base << std::endl;
		}
		baseLong += 2;
	}

	string out;
	for (size_t i = 0; i < res.size(); i++) {
		out += res[i].first;
		for (size_t j = 0; j < res[i].second.size(); j++) {
			out += ' ';
			out += to_string((long long)res[i].second[j].toLong());
		}
		out += '\n';
	}
	return out;
}

int main(int argc, const char *argv[]) {
	srand(1337);
	loadPrimes("primes1.txt");
	std::cout << "Primes loaded" << std::endl;
	std::ofstream fs("big.out");
	int i = 1;
	auto cases = load("big.in");
	for (auto it = cases.begin(); it != cases.end(); ++it) {
		fs << "Case #" << i << ":\n" << solve(*it);
		i++;
	}
	fs.close();

	return 0;
}
