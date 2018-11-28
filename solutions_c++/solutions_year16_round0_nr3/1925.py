#include <iostream>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <vector>
#include <NTL/ZZ.h>
#include <set>

using namespace std;
using namespace NTL;

vector<int> primes;

void calcprimes() {
	primes.push_back(2);
	for( int i = 3; i <= 5000; i += 2 ) {
		for( int p : primes ) {
			if( p*p > i ) break;
			if( i % p == 0 ) goto next;
		}
		primes.push_back( i );
	next:;
	}
}

bool verify( int N, const vector<ZZ>& numbers, const vector<int>& divisors ) {
	assert( numbers.size() == 9 );

	string prev_s;
	for( int i = 0; i < 9; ++i ) {
		if( numbers[i] % divisors[i] != 0 || numbers[i] == divisors[i] ) return false;

		int base = 2+i;
		string s;
		for( ZZ x = numbers[i]; x != 0; x /= base ) {
			int rem = x % base;
			assert( rem == 0 || rem == 1 );
			s += (char)('0'+rem);
		}
		assert( (int)s.size() == N && s[0] == '1' && s[s.size()-1] == '1' );
		if( i > 0 ) assert( s == prev_s );
		prev_s = s;
	}

	return true;
}

int main() {
	calcprimes();

	int N, J, cases;
	std::set<ZZ> found_numbers;

	cin >> cases >> N >> J;
	cout << "Case #1:" << endl;

	srand( time(0) );

	while( J > 0 ) {
		int r = rand() % (1<<(N-2));
		bool ok = true;
		vector<ZZ> numbers;
		for( int base = 2; base <= 10; ++base ) {
			ZZ x = to_ZZ(1);
			for( int i = 0; i < N-2; ++i ) {
				x = x * base + ( ( r & (1<<i) ) != 0 );
			}
			x = x * base + 1;

			if( ProbPrime( x ) ) {
				ok = false;
				break;
			}
			numbers.push_back( x );
		}
		if( ok ) {
			assert( numbers.size() == 9 );

			vector<int> divisors;

			for( int i = 0; i < 9; ++i ) {
				bool found_factor = false;
				for( int p : primes ) {
					if( numbers[i] % p == 0 ) {
						divisors.push_back( p );
						found_factor = true;
						break;
					}
				}
				if( !found_factor ) break;
			}

			if( divisors.size() == 9 && verify( N, numbers, divisors ) ) {
				if( found_numbers.insert( numbers[8] ).second ) {
					cout << numbers[8];
					for( int i = 0; i < 9; ++i ) {
						cout << ' ' << divisors[i];
					}
					cout << endl;
					--J;
				}
			}
		}
	}

	return 0;
}
