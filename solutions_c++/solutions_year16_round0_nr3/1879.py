// 2015q3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>

#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>

#include <fstream>
#include <algorithm>
#include <functional>
#include <climits>


//int8_t  primes[178956971];

// Large
// const unsigned long probMAX = 4294967295; //  (2 ^ 32) - 1;
// const unsigned long probMAX_sqr = 65535;

// small
//const unsigned long probMAX = 65535; //  (2 ^ 32) - 1;
//const unsigned long probMAX_sqr = 255;

//int8_t  primes[probMAX/3];

//int64_t primes[23 * 1024 * 1024];


using namespace std;
using boost::multiprecision::uint128_t;

// total number of primes 

bool is_prime(uint64_t  n) {
	if (n <= 1) return false;
	if (n <= 3) return true;
	if (n % 2 == 0 || n % 3 == 0) return false;

	long i = 5;
	while (i*i <= n)
		if (n%i == 0 || n % (i + 2) == 0) return false;
		i += 6;
	return true;
}

uint64_t nontrivial_factor(uint128_t n) {
	if (n <= 1) return 0;
	if (n <= 3) return 0;

	if (n % 2 == 0) return 2;
	if (n % 3 == 0) return 3;

	long i = 5;
	while (i*i <= n) {
		if (n%i == 0) return i;
		if (n % (i + 2) == 0) return i + 2;

		i += 6;
	}

	return 0;

}


//bool is_prime_table(uint32_t n) {
//	if (n <= 1) return false;
//	if (n <= 3) return true;
//	if (n % 2 == 0 || n % 3 == 0) return false;
//	return (primes[ n / 3 - 1]);
//}

/* read the question! */
/*void prime_table() {

	long prime_count = 0;

	memset(primes, -1, sizeof(primes));
	
	// 26 seconds on my machine.
	
	uint32_t idx = 0;
	
	for (idx = 0; idx < probMAX_sqr ; idx++) {

		for (; idx < probMAX_sqr  ; idx++) { if (primes[idx]) break; }

			uint32_t i = (idx/2) * 6 + 5 + (idx%2?2:0) ;
			uint32_t j, idelta;

			
			idelta = i * 2;
			while ((idelta) % 6 != 0) idelta += i;
			idelta /= 6;
			idelta *= 2;


			j = i * i;
			while (j % 6 != 5) j += i;
			j = ((j - 5) / 6) * 2;
			
			for (; j < sizeof(primes); j += idelta) {
				primes[j] = 0;
			}

			j = i * i;
			while (j % 6 != 1) j += i;
			j = ((j - 1) / 6) * 2 -1;

			for (; j < sizeof(primes); j += idelta) {
				primes[j] = 0;
			}
	}

	cout << endl;

/* Dump the primes
	cout << "2, 3, ";
	prime_count = 2;

	for (uint32_t j =0; j< sizeof(primes);j++) {
		
		if (primes[j]){
			cout << j * 3 + 5 - (j % 2 ? 1:0) << ", ";
			prime_count++;
			if (prime_count % 10 == 0) cout << endl;
		}
	}

	cout << endl << "total primes " << prime_count << endl;
	
}
*/

string problem(std::ifstream& fin, std::ofstream& ferr) {

	long N , J;

	fin >> N >> J;
	
	uint32_t start = 1 << N + 1;
	int sol = 0;

	uint128_t value;
	uint128_t mult;
	uint32_t i;
	uint32_t i2;
	uint64_t factor;
	char sfactor[32];


	stringstream resultline;
	int base;
	stringstream res2;

	res2.clear();
	
	for (i = (1 << N-1) + 1; (sol < J) ; i+=2 ) {	
		resultline.str ("");

		for ( base = 2; base <= 10; base++) {
			i2 = i;
			mult = 1;
			value = 0;

			while (i2) {
				value += (1 & i2) * mult;
				mult *= base;
				i2 >>= 1;
			}
			
			factor = nontrivial_factor(value);
			if (factor == 0) break;
									
			resultline << " " << factor ;

		}

		if (base <= 10) continue;
	
		res2 << endl << value << resultline.str();
		sol++;
	}

	return res2.str();


}

int main()
{
	int T;
	string filename;

	string result;

	cout << "Enter the file prefix" << endl;
	cin >> filename;

	std::ifstream f_in((filename + ".in").c_str());
	std::ofstream f_out((filename + ".out").c_str());
	std::ofstream f_err((filename + ".err").c_str());


	if (!f_in) { cerr << "Failed to open input file." << endl; }
	if (!f_out) { cerr << "Failed to open output file." << endl; }
	if (!f_out) { cerr << "Failed to open debug file." << endl; }

	//prime_table();

	if (f_in && f_out) {

		f_in >> T;

		for (int i = 1; i <= T; i++) {
			result = problem(f_in, f_err);
			cerr << "Case #" << i << ": " << result << endl;
			f_out << "Case #" << i << ": " << result << endl;
		}

		f_in.close();
		f_out.close();
	}
}
