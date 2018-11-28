// coinjam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <tuple>
#include <stdexcept>
#include <string>
#include <bitset>
#include <vector>
#include <map>
#include <type_traits>

//! Returns the first prime < 100 by which the specified integer is divisible
template<typename T>
std::tuple<T, bool> firstDividingPrime(T value)
{
	static_assert(std::is_integral<T>::value, "Function has to be called with integers.");

	const std::vector<T> primes = { 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97 };
	for (auto p : primes) {
		if (value % p == 0) return { p,true };
	}
	return { 0,false };
}

//! Converts a bitset to an integer in the specified base
template<typename T, size_t N>
T jamcoinToInt(const std::bitset<N>& bitset, T base)
{
	T result = T(0);
	for (size_t i = 0; i < N; i++) {
		result += bitset[i] * static_cast<T>(std::pow(base, i));
	}
	return result;
}

//! Returns the divisors of the different base representations of the specified jamcoin or an empty map if no divisor was found for one base
template<size_t N>
std::tuple<std::map<int,int>,bool> jamCoinDivisors(const std::bitset<N>& jamcoin)
{
	// Calculate base representations
	std::map<int, unsigned long long> inBase;
	for (int i = 2; i <= 10; i++) {
		inBase[i] = jamcoinToInt<unsigned long long>(jamcoin, i);
		// std::cout << jamcoin << " in base " << i << " is " << inBase.at(i) << "\n";
	}

	std::map<int,int> baseDivisors;
	for (const auto& pair : inBase) {
		bool isDivisible;
		unsigned long long prime;
		// Check if divisible by primes < 100
		std::tie(prime, isDivisible) = firstDividingPrime<unsigned long long>(pair.second);

		if (!isDivisible) {
			return { std::map<int,int>(),false };
		} else {
			baseDivisors[pair.first] = static_cast<int>(prime);
		}
	}

	return{ baseDivisors,true };
}

template<size_t N>
struct JamCoinGenerator {
	//! Construct a jamcoin generator
	JamCoinGenerator()
		: firstCall_(true)
		, currentCoin_(initialJamCoin())
		, counter_(0)
	{
		static_assert(N > 2, "Jamcoins must be of length > 2");
	}

	//! Return the next valid jamcoin
	std::tuple<std::bitset<N>, bool> next()
	{
		if (firstCall_)  {
			bool isJamCoin;
			std::tie(currentDivisors_, isJamCoin) = jamCoinDivisors(currentCoin_);
			if (isJamCoin) {
				firstCall_ = false;
				return{ currentCoin_,true };
			} else {
				firstCall_ = false;
			}
		}

		bool inRange, isJamCoin;
		// Increment until jamcoin is found or maximum coin is reached
		do {
			inRange = this->incrementCoin();
			std::tie(currentDivisors_, isJamCoin) = jamCoinDivisors(currentCoin_);
			// std::cout << counter_ << " " << currentCoin_.to_string() << "\n";
		} while (inRange && !isJamCoin);
		return{ currentCoin_,inRange };		
	}

	//! Return current divisor map (association of base to smallest divisor)
	std::map<int, int> divisors() {
		return currentDivisors_;
	}

private:
	bool firstCall_;
	std::bitset<N> currentCoin_;
	std::map<int, int> currentDivisors_;
	unsigned long long counter_;

	//! Constructs the initial jamcoin bitset
	static constexpr std::bitset<N> initialJamCoin()
	{
		return std::bitset<N>(static_cast<unsigned long long>(std::pow(2, N-1)) + 1);
	}

	//! Tries to increment the current coin wihtout checking whether it is a jamcoin. Returns false if maximum coin is reached
	bool incrementCoin()
	{
		// Increment inner bits
		for (size_t i = 1; i < N - 1; i++) {
			if (currentCoin_[i] == 0) {
				currentCoin_[i] = 1;
				break;
			}
			else {
				currentCoin_[i] = 0;
			}
		}

		// Check if maximum coin is reached (overflow)
		if (currentCoin_ == initialJamCoin()) return false;
		// Count increment
		counter_++;
		return true;
	}
};

int main()
{
	// std::cout << "Coin Jam" << "\n";
	// std::cout << "--------" << "\n";

	// Length of jamcoins to generate
	constexpr int N = 16;

	// Get number of jamcoins to generate
	int jamcoinCount;
	std::cin >> jamcoinCount;

	// std::cout << "Trying to generate " << jamcoinCount << " jamcoins of length " << N << "\n";

	std::cout << "Case #1:" << "\n";

	// Construct generator
	JamCoinGenerator<N> generator;
	for (int i = 0; i < jamcoinCount; i++) {
		std::bitset<N> jamcoin;
		bool isValid;
		std::tie(jamcoin, isValid) = generator.next();

		if (!isValid) throw std::logic_error("No more available jamcoins.");

		std::cout << jamcoin.to_string();
		auto divisors = generator.divisors();
		for (int i = 2; i < 11; i++) {
			std::cout << " " << divisors.at(i);
		}
		std::cout << "\n";
	}

    return 0;
}

