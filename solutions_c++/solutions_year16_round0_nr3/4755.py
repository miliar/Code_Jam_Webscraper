#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;

	for(int cases = 1; cases <= t; cases++) {
		unsigned int n, j;
		cin >> n >> j; // find j jamcoins of length n. 2 <= n <= 32 (could overflow otherwise)
		
		cout << "Case #" << cases << ':' << endl;

		unsigned long long int try_coin = (1 << (n-1)); // this bit must be set
		for(unsigned int i = 0; (i < n); i++) // being careful to avoid overflowing a long long in the larger input cases
			try_coin |= (1 << i); // start search with all ones (2^n - 1)

		for(unsigned int jth_jamcoin = 1; jth_jamcoin <= j; jth_jamcoin++) {

			//search from 2^n - 1 down to 2^n-1 + 1, with a step of 2
			for(; try_coin > (1U << (n-1)) ; try_coin -= 2) {
				unsigned long long int divisors[11] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
				unsigned long long int number = try_coin;
				int found_divisors = 0;

				for(int base = 2; base <= 10; base++) {
					if(number%2==0) {
						divisors[base] = 2;
						found_divisors++;
					}
					else {
						for(unsigned int d = 3; (d < 10000) && (d*d <= number); d += 2) { // we cut the trial short at 10000 to avoid primes (quasi-primes) gumming up our search. strictly speaking, we have no guarantee of a solution, but practically, it will be relatively easy to find the composite numbers we need
							if(number%d==0) {
								divisors[base] = d;
								found_divisors++;
								break;
							}
						}
					}
					if(found_divisors < base-1) // we didnt find a divisor, try next number
						break;
					// prepare number for next iteration:
					number = ((1 << (n-1)) & try_coin) == 0 ? 0 : 1;
					for(int i = n-2; i >= 0; i--) { // horner's rule to calculate jamcoin in base b+1 for next iteration
						number *= (base+1);
						number += ( ((1 << i) & try_coin) == 0 ? 0 : 1 );
					}
				}
				if(found_divisors==9) { // successful hit
					for(int i = n-1; i >= 0; i--) {
						if( (1 << i) & try_coin )
							cout << '1';
						else
							cout << '0';
					}
					for(int i = 2; i <= 10; i++) {
						cout << ' ' << divisors[i];
					}
					cout << endl;
					try_coin -= 2;
					break; // next jamcoin to be found
				}
				//else


			}
		}
		if(try_coin < (1U << (n-1)) )
			cout << "search unsuccessful: look harder next time" << endl;



	}
}