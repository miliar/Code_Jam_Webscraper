#include <iostream>
#include <bitset>
#include <cmath>
#include <map>

unsigned long long binarySeqToBaseN(const std::string& iSequence, unsigned long long toBase) {
	unsigned long long result(0);
	unsigned long long exp(0);
	for(auto a = iSequence.crbegin(); a!=iSequence.crend(); ++a) {
		if(*a == '1') {
			result += (pow(toBase, exp));
		}
		++exp;
	}
	return result;
}

bool isPrime(unsigned long long number) {
	for (unsigned long long i = 2; i < sqrt(number); ++i) {
		if (0 == (number % i)) {
			return false;
		}
	}
	return true;
}

// To be used only in case of non-prime numbers!
unsigned long returnNonTrivialDivisorIfNotPrime(unsigned long number) {
	for (unsigned long i = 2; i < number; ++i) {
		if (0 == (number % i)) {
			return i;
		}
	}
	return 0;
}

int main(int argc, char **argv) {
	unsigned short T, N, J;
	std::cin >> T >> N >> J;
	std::cout << "Case #1:\n";

	std::bitset<16> jamcoinSequence;
	jamcoinSequence.flip();
	//std::cout << jamcoinSequence.to_string() << "\n";
	const unsigned long long maxCount(jamcoinSequence.to_ulong());
	unsigned long numJamCoinsFound(0);

	for(unsigned long long count = (pow(2,N-1) + 1); count < maxCount; ++count) {
		//std::cout << count << "\n";
		std::bitset<16> mybitset(count);
		//std::cout << "mybitset --> " << mybitset.to_string() << "\n";
		if(!mybitset[0]) { continue;}
		//std::cout << "Bitset --> " << mybitset << "\n";
		std::map<size_t, unsigned long long> baseValues;
		bool skipSequence(false);

		for(size_t i = 2; i <= 10; ++i) {
			unsigned long long sequenceToBaseResult = binarySeqToBaseN(mybitset.to_string(), i);

			//Quick reject
			if(sequenceToBaseResult%3 == 0 ||
				sequenceToBaseResult%5 == 0 ||
				sequenceToBaseResult%7 == 0 ||
				sequenceToBaseResult%11 == 0 ||
				sequenceToBaseResult%13 == 0) {

			} else {
				// skip this sequence
				skipSequence = true;
				break;
			}

			// If this sequenceToBaseResult is prime, skip this sequence
			if(isPrime(sequenceToBaseResult)) {
				skipSequence = true;
				break;
			}
			baseValues.insert(std::make_pair(i, binarySeqToBaseN(mybitset.to_string(), i)));
		}

		if(!skipSequence) {
			// We got a jam coin! Find non-trivial divisors, and print.
			std::cout << mybitset.to_string();
			// For each base
			for(const auto& pair : baseValues) {
				//std::cout << " " << pair.first << "|" << pair.second;
				std::cout << " " << returnNonTrivialDivisorIfNotPrime(pair.second);
			}
			std::cout << std::endl;
			++numJamCoinsFound;
			if(numJamCoinsFound >= J) {
				// We are all done!
				//std::cout << "COUNT REACHED : " << numJamCoinsFound;
				return 0;
			}
		}

	}


}
