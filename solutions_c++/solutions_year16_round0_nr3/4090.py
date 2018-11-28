/*
 * jamcoin.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: jpaone
 */

#include <math.h>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

const bool DEBUG = true;

class JamCoin {
public:
	JamCoin( long long int l ) : _length(l) {
		for( int i = 0; i < _length; i++ ) {
			_num.push_back( 0 );
		}
	}
	JamCoin( long long int l, vector<int> n ) : _length(l) {
		for( int i = 0; i < _length; i++ ) {
			_num.push_back( n.at(i) );
		}
	}

	JamCoin plusOne() {
		vector<int> newNum;
		int carryOne = 0;

		for( int i = _length-1; i >= 0; i-- ) {
			int numToAdd = (i == _length-1 ? 1 : 0);
			int nextNum = _num.at(i) + numToAdd + carryOne;
			newNum.insert( newNum.begin(), nextNum % 2 );
			carryOne = nextNum / 2;
		}

		return JamCoin( _length, newNum );
	}

	string toString() {
		stringstream ss;
		for( int i = 0; i < _length; i++ ) {
			ss << _num.at(i);
		}
		return ss.str();
	}

	long long int convertToBase( int base ) {
		long long int result = 0;

		for( int i = _length-1; i >= 0; i-- ) {
			result += pow( base, _length - 1 - i ) * _num.at(i);
		}

		return result;
	}

	int getDigitAtPos( int pos ) {
		return _num.at( pos );
	}

	bool allOnes() {
		for( int i = 0; i < _length; i++ ) {
			if( _num.at(i) == 0 )
				return false;
		}
		return true;
	}

	void makeDigitOne( int pos ) {
		_num.at( pos ) = 1;
	}

private:
	long long int _length;
	vector<int> _num;
};

bool isPrime( long long int num ) {
	if( num < 2 ) {
		return false;
	}
	for( long long int i = 2; i < num / 2; i++ ) {
		if( num % i == 0 ) {
			return false;
		}
	}
	return true;
}

bool isPrimeFaster( long long int num ) {
    if (num <=1)
        return false;
    else if (num == 2)
        return true;
    else if (num % 2 == 0)
        return false;
    else {
        bool prime = true;
        int divisor = 3;
        double num_d = static_cast<double>(num);
        int upperLimit = static_cast<int>(sqrt(num_d) +1);

        while (divisor <= upperLimit) {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}

int main( int argc, char *argv[] ) {

	int T;
	cin >> T;

	for( int i = 1; i <= T; i++ ) {

		long long int N, J;
		cin >> N >> J;

		cout << "Case #" << i << ":" << endl;

		JamCoin lastCoin( N );
		lastCoin.makeDigitOne( 0 );

		int foundCases = 0;

		while( foundCases < J ) {
			lastCoin = lastCoin.plusOne();
			if( lastCoin.getDigitAtPos( 0 ) == 1 && lastCoin.getDigitAtPos( N-1 ) == 1 ) {
				bool allNotPrime = true;

				if (DEBUG) cout << "JamCoin " << lastCoin.toString() << endl;

				vector<long long int> divisors;

				for( int b = 2; b <= 10; b++ ) {
					long long int newBase = lastCoin.convertToBase( b );
					if (DEBUG) cout << "\tAs base " << b << " = " << newBase << endl;

					if( isPrimeFaster( newBase ) ) {
						allNotPrime = false;
						break;
					} else {
						for( long long int i = 2; i < newBase / 2; i++ ) {
							if( newBase % i == 0 ) {
								divisors.push_back( i );
								break;
							}
						}
					}
				}

				if( allNotPrime ) {
					if (DEBUG) cout << "\tAll bases are Not Prime! -- " << lastCoin.toString() << endl;
					foundCases++;

					cout << lastCoin.toString() << " ";
					for( int i = 0; i < divisors.size(); i++ ) {
						cout << divisors.at(i);
						if( i < divisors.size() - 1 )
							cout << " ";
					}
					cout << endl;
				}
			}
		}
	}

	return 0;
}


