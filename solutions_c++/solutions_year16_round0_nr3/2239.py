#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <unistd.h>
#include "primes.h"

void print_bitarray(char* bitarray, int n) {
	for (int i = 0; i < n; ++i) {
		printf("%c", bitarray[i]);
	}
}


//  (1*243 + 1*81 + 0*27 + 1*9 + 1*3 + 1*1)
long long int str_to_long_long_int(char* s, int len, int base) {
	long k = base;
	long long int acc = 0;
	for (int i = len-1; i > -1; i--) {
		acc += k * (s[i] - 48);
		k *= base;
	}
	return acc;
}

// linear search because caching
// we can improve here. if a number is greater than
// a certain value, just linear search from a different location
// should save tiny amount of time
// also hardcode first few cases
bool is_definitely_prime(long long int N) {
	
	if (   N == 2 || N == 3 || N == 5 || N == 7 || N == 11
	    || N == 13 || N == 17 || N == 19 || N == 23 || N == 29
	    || N == 31 || N == 37 || N == 41 || N == 43) {
		return true;
	}

	for (unsigned int i = 14; i < 10000; i++) {
		if (N == PRIMES[i]) {
			return true;
		}
	}
	return false;
}

// returns a value that's greater than 1 if a divisor was found;
long long int first_nontrivial_divisor(long long int N) {

	// if we're prime then just jump out.
	if (is_definitely_prime(N)) {
		return -1;
	}

	long long int i = 2;
	while(i <= sqrt(N))
    {
        if(N%i==0) {
            return i;
            // if (i != (N / i)) { return N/i; }
        } 
        i++;
    }

    return -1;
}

int main(void) {

	int T, N, NEEDED;
	int good;
	good = scanf("%i\n", &T);
	assert(good == 1);
	good = scanf("%i %i\n", &N, &NEEDED);
	assert(good == 2);

	//TODO: special case when N == 3 or 4 or 5 or 6.
	if (N == 3) {

		// 101 or 111

	} 
	else {

		char bitstring[N];
		bitstring[0] = '1';
		bitstring[N-1] = '1';
		int MAX_INNER_BITS = N - 2;
		int generated = 0;

		//printf("MAX INNER BITS: %i\n", MAX_INNER_BITS);

		// this minus one is an all-one bitstring of length MAX_INNER_BITS
		int BSK = (1<<MAX_INNER_BITS);
		//printf("COUNTING DOWN FROM: (1<<%i)-1, %i\n", MAX_INNER_BITS, BSK);
		// generate all possible bitstrings from 2^N down to 0
		while(--BSK > 0) {
/*
			if (BSK % 10000000 == 0) {
				printf("BSK = %i\n", BSK);
			}
*/

			for (unsigned int k = 0; k < MAX_INNER_BITS; ++k) {
				bool is_set = BSK & (1 << k);
				bitstring[k+1] = is_set + 48;  // convert 0 -> '0' and 1 -> '1'
			}
			//sleep(1);
			//puts("=========BITARRAY==========");
			//print_bitarray(bitstring, N);

			// NOTE: unrolled the if statements
			// this is to test primality at each if block

			long long int base2 = strtoll(bitstring, NULL, 2);
			long long int b2d = first_nontrivial_divisor(base2);

			if (b2d != -1) {
				long long int base3 = strtoll(bitstring, NULL, 3);
				long long int b3d = first_nontrivial_divisor(base3);
				if (b3d != -1) {
				    long long int base4 = strtoll(bitstring, NULL, 4);
				    long long int b4d = first_nontrivial_divisor(base4);
				    if (b4d != -1) {
					    long long int base5 = strtoll(bitstring, NULL, 5);
					    long long int b5d = first_nontrivial_divisor(base5);
					    if (b5d != -1) {
						    long long int base6 = strtoll(bitstring, NULL, 6);
						    long long int b6d = first_nontrivial_divisor(base6);
						    if (b6d != -1) {
								long long int base7 = strtoll(bitstring, NULL, 7);
								long long int b7d = first_nontrivial_divisor(base7);
								if (b7d != -1) {
									long long int base8 = strtoll(bitstring, NULL, 8);
									long long int b8d = first_nontrivial_divisor(base8);
									if (b8d != -1) {
										long long int base9 = strtoll(bitstring, NULL, 9);
										long long int b9d = first_nontrivial_divisor(base9);
										if (b9d != -1) {
											long long int base10 = strtoll(bitstring, NULL, 10);
											long long int b10d = first_nontrivial_divisor(base10);

											if (b10d != -1) {
												print_bitarray(bitstring,N);
												printf(" %lld %lld %lld %lld %lld %lld %lld %lld %lld\n", b2d, b3d, b4d, b5d, b6d, b7d, b8d, b9d, b10d);
												generated++;
												if (generated == NEEDED) {
													break;
												}
											}
										}
									}
								}
						    }
						}
					}
				}
			}
		}
	}
}
