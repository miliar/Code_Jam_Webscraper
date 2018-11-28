#include <cmath>
#include <iostream>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

unsigned long toBase(std::string n, int base) {
	if (base == 10) {
		return stol(n);
	}
	unsigned size = n.size();
	unsigned long result = 0;
	for (unsigned i = 0; i < size; i++) {
		if (n[i] == '1') {
			result += pow(base, size - 1 - i);
		}
	}
	return result;
}

std::string toBinary(unsigned long n) {
	if (n == 0) {
		return "0";
	}
	unsigned long numAlgs = log2(n) + 1;
	std::string result(numAlgs, '_');
	unsigned long counter = 0;
	while (n > 0) {
		result[numAlgs - 1 - counter] = (n % 2 == 0) ? '0' : '1';
		n /= 2;
		counter++;
	}
	return result;
}

std::string pad(const std::string& str, unsigned long length) {
	unsigned long size = str.size();
	if (size >= length) {
		return str;
	}
	return std::string(length - size, '0') + str;
}

std::string parse(int N, int J){
	std::vector<std::string> lines;
	for (unsigned i = 0; i < pow(2, N - 2); i++) {
		std::string result;
		std::string coin = std::string("1") + pad(toBinary(i), N - 2) + std::string("1");
		bool isJamcoin = true;
		for (int j = 2; j <= 10; j++) {
			unsigned long value = toBase(coin, j);
			bool ok = false;
			for (unsigned long k = 2; k <= sqrt(value); k++) {
				if (value % k == 0) {
					result += std::to_string(k) + " ";
					ok = true;
					break;
				}
			}
			if (!ok) {
				result.clear();
				isJamcoin = false;
				break;
			}
		}
		if (isJamcoin) {
			result = coin + " " + result + '\n';
			lines.push_back(result);
			if (lines.size() == J) {
				break;
			}
		}
	}

	std::string r;
	for (auto line : lines) {
		r += line;
	}
	return r;
}

int main(){
	int T, i = 0;
	int N, J;
	
	std::cin >> T;
	for (int i = 0; i < T; i++) {
		std::cin >> N >> J;
		auto r = parse(N, J);
		std::cout << "Case #" << (i+1) << std::endl;
		std::cout << r << std::endl;
	}
}