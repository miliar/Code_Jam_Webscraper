#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <sstream>
//#include <boost/multiprecision/mpfr.hpp>
#include <boost/multiprecision/cpp_int.hpp>

typedef boost::multiprecision::int128_t BigInt;

void printCoin(const std::vector<bool> &coin)
{
	int size = coin.size();
	for (int i = size -1; i >= 0 ; i--) {
		std::cout << coin[i];
	}
	std::cout << " ";
}
std::vector<bool> addCoin(const std::vector<bool> &coin, int offset) 
{
	std::vector<bool> result(coin);
	const int size = result.size();
	for (int i = 1; i < size - 1; i++) {
		unsigned int mask = 1 << (i - 1);
		if ((mask&offset) == mask) {
			result[i] = true;
		}
	}
	return result;
}
unsigned long long coinValue(const std::vector<bool> &coin, int base)
{
	const int size = coin.size();
	unsigned long long result = 0;
	for (int i = 0; i < size; i++) {
		if (coin[i]) {
			result += ::pow(base, i);
		}
	}
	return result;
}

BigInt coinValueBig(const std::vector<bool> &coin, int base)
{
	const int size = coin.size();
	BigInt result = 0;
	for (int i = 0; i < size; i++) {
		if (coin[i]) {
			result += (BigInt)boost::multiprecision::pow(BigInt(base), i);
		}
	}
	return result;
}
bool isprime(unsigned long long &div, const unsigned long long value)
{
	const unsigned long long high = ::sqrt(value);
	for (unsigned long long i = 2; i <= high; i++) {
		if (value%i == 0) { div = i; return false; }
	}
	return true;
}
bool isprimeBig(unsigned long long &div, const BigInt &value)
{
	const int GIVE_UP = 10000;
	const unsigned long long high = (unsigned long long) boost::multiprecision::sqrt(value);
	for (unsigned long long i = 2; i <= GIVE_UP; i++) {
		if (value%i == 0) { div = i; return false; }
	}
	return true;
}

void printJamCoins(const int len, const int count)
{
	std::vector<bool> bCoin(len, 0);
	bCoin[0] = true; bCoin[len - 1] = true; // First, Last = 1
	const int MaxOffset = 1 << (len-2);
	for (int i = 0, j = 0; i < MaxOffset, j < count; i++) {
		std::vector<bool> coin(addCoin(bCoin, i));
		bool prime = false;
		std::ostringstream oss;
		for (int j = 2; j <= 10; j++) {
			//unsigned long long value = coinValue(coin, j);
			BigInt value = coinValueBig(coin, j);
			unsigned long long div;
			if (!isprimeBig(div, value)) {
				oss << div; oss << " ";
				//oss << value << "/" << div; oss << " ";
			} else { prime = true; break;  }
		}
		if (!prime) {
			printCoin(coin); std::cout << oss.str() << std::endl;
			j++;
		}
	}
}

int main()
{
	int NumTests = 0;
	std::cin >> NumTests; // only 1
	for (int i = 1; i <= NumTests; i++) {
		int length = 0, count = 0;
		std::cin >> length >> count;
		std::cout << "Case #" << i << ": " << std::endl;
		printJamCoins(length, count);
	}
	return 0;
}