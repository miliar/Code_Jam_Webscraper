#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define SIZE 101


int main() {
	std::ifstream fin;
	fin.open("input.txt");
	std::ofstream fout;
	fout.open("output.txt");

	int T;
	fin >> T;
	for (int i = 1; i <= T; ++i) {
		int N, J;
		fin >> N >> J;
		uint32_t candidate;
		uint32_t max;
		if (N == 16) {
			candidate = 0x8001;
			max = 0xffff;
		} else if (N == 32) {
			candidate = 0x80000001;
			max = 0xffffffff;
		} else {
			return -1;
		}

		fout << "Case #1:" << std::endl;
		uint64_t while_max = (uint64_t)max + 1;
		while (J > 0 && candidate < while_max) {
			std::cout << std::hex << candidate << std::dec << std::endl;
			std::vector<uint32_t> divisors;
			for (int base = 2; base <= 10; base++) {
				uint64_t cand_b = candidate;
				//uint64_t cand_b = 9;
				uint64_t cand_10 = 0;
				uint64_t multiplier = 1;
				// convert to base 10
				while (cand_b > 0) {
					cand_10 += multiplier * (cand_b & 0x01);
					cand_b >>= 1;
					multiplier *= base;
				}
				// check if prime
				bool prime = true;
				uint32_t fac;
				for (fac = 2; fac <= std::ceil(std::sqrt(cand_10)); fac++) {
					if (cand_10 % fac == 0) {
						prime = false;
						break;
					}
				}
				// if not prime, add to list
				if (!prime) {
					divisors.push_back(fac);
					//std::cout << "\t" << fac << std::endl;
				} else {
					break;
					//std::cout << "base " << base << "is prime" << std::endl;
				}

				//std::cout << cand_10 << std::endl;
			}
			// check if all bases have divisors
			std::cout << "divs: " << divisors.size();
			if (divisors.size() == 9) {
				J--;
				uint32_t c = candidate;
				std::vector<bool> bits;
				while (c > 0) {
					bits.push_back(c % 2);
					c >>= 1;
				}
				for (int i = bits.size() - 1; i >= 0; i--) {
					fout << bits[i];
				}
				for (auto d : divisors) {
					fout << " " << d;
				}
				fout << std::endl;
			}
			candidate += 2;
		}

		std::cout << std::hex << candidate << " " << max << std::dec << std::endl;
	}

	fin.close();
	fout.close();
	return 0;
}