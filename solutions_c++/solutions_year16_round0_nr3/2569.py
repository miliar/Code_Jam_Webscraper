#include <iostream>
#include <vector>
#include <bitset>
#include <cmath>
#include <string>

typedef std::bitset<16> bit_seq;
typedef std::bitset<14> sub_seq;

uint64_t find_divisor(uint64_t n) {
	for (uint64_t i = 2; i < (uint64_t)(std::sqrt(n))+1; ++i) {
		if (n % i == 0) {
			return i;
		}
	}
	return 0;
}

uint64_t convert_to_base(uint64_t base, bit_seq& seq) {
	uint64_t result = 0;
	for (uint64_t i = 0; i < seq.size(); ++i) {
		result += seq[i] * std::pow(base,i);
	}
	return result;
}

int main () {

	uint64_t T,N,J;
	std::cin >> T >> N >> J;
	std::cout << "Case #1:" << std::endl;

	uint64_t count = 0;
	uint64_t found = 0;
	std::vector<uint64_t> divisors(9,0);

	for (uint64_t j = 0; j < J;) {
		
		sub_seq sub(count++);
		bit_seq seq("1"+sub.to_string()+"1");
		std::fill(divisors.begin(), divisors.end(), 0);

		for (uint64_t i = 2; i <= 10; ++i) {
			

			auto num = convert_to_base(i,seq);
			auto d = find_divisor(num);
			if (d != 0) {
				divisors[i-2] = d;
			}
			else {
				break;
			}
		}

		if (std::find(divisors.begin(), divisors.end(), 0) == divisors.end()) {

			++j;
			for (int k = seq.size()-1; k >= 0; --k) {
				std::cout << seq[k];
			}
				
			for (auto& element : divisors) {
				std::cout << " " << element;
			}
			std::cout << std::endl;
		}
		

	}

	

	
	return 0;
}


