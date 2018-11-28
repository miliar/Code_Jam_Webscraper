#include <iostream>
#include <fstream>

#include <vector>
#include <map>
#include <set>
#include <cstdlib>

#include "bigInt.h"

using namespace std;

//typedef di_unsigned<unsigned int, unsigned int, 350> big_digit;

class Palindrome {
	bool even;
	int middle;
	vector<int> upper_digits;

public:
	// construct the smallest palindrome not bigger than i
	Palindrome(const string& s) : upper_digits() {
		even = !(s.size() & 1);

		vector<int> digits;

		for(auto c : s) {
			digits.push_back( int(c)-48 );
		}

		for(int i=0; i<digits.size()/2; ++i) {
			upper_digits.push_back(digits.at(i));
		}

		if(!even) {
			middle = digits.at(digits.size()/2);
		} else {
			middle = -1;
		}

		//for(auto c : upper_digits) cout << c << endl;
	}

	void increment() {
		if(!even && middle < 9) {
			middle++;
			return;
		}

		// else
		middle = 0;
		int idx = 0;

		while(true) {
			if(idx == upper_digits.size()) {
				// need to increment digit size
				if(even) {
					even = false;
					middle = 0;
					if(upper_digits.size() == 0) {
						upper_digits.push_back(1);
					} else {
						upper_digits.at(0) = 1;
					}
					for(int i=1; i<upper_digits.size(); ++i) upper_digits.at(i) = 0;
					return;
				} else {
					even = true;
					if(upper_digits.size() == 0) {
						upper_digits.push_back(1);
						return;
					} else {
						upper_digits.at(0) = 1;
					}
					for(int i=1; i<upper_digits.size(); ++i) upper_digits.at(i) = 0;
					upper_digits.push_back(0);
					return;
				}
			}
			int digit = upper_digits.at(upper_digits.size()-1-idx);
			if(digit < 9) {
				upper_digits.at(upper_digits.size()-1-idx) += 1;
				return;
			} else {
				upper_digits.at(upper_digits.size()-1-idx) = 0;
				idx++;
			}
		}
	}

	void check_square(const BigInt::Rossi& lower, const BigInt::Rossi& upper, bool& is_palindrome, bool& above_range, bool& below_range) {
		stringstream ss;
		for(auto digit : upper_digits) ss << digit;
		if(!even) ss << middle;
		for(int i=upper_digits.size()-1; i>=0; i--) ss << upper_digits.at(i);

		BigInt::Rossi number(ss.str(), BigInt::DEC_DIGIT);
		BigInt::Rossi square = number*number;

		if(square < lower) { below_range = true; return; }
		if(square > upper) { above_range = true; return; }

		below_range = false;
		above_range = false;

		string sqstring = square.toStrDec();
		for(int i=0; i<sqstring.size()/2; ++i) {
			if(sqstring.at(i) != sqstring.at(sqstring.size()-1-i)) {
				is_palindrome = false;
				return;
			}
		}
		
		is_palindrome = true;
	}

	void print() {
		for(auto i : upper_digits) {
			cout << i;
		}
		if(!even)
			cout << "|" << middle;

		cout << endl;
	}
};

int main(int argc, char const *argv[])
{
	ifstream ifs(argv[1]);
	int ncases;
	ifs >> ncases;

	for (int casenum = 1; casenum < ncases+1; ++casenum) {
		string lowerstring, upperstring;
		ifs >> lowerstring >> upperstring;
		
		
		bool is_palindrome, below_range, above_range=false;

		BigInt::Rossi lower(lowerstring, BigInt::DEC_DIGIT);
		BigInt::Rossi upper(upperstring, BigInt::DEC_DIGIT);

		string sqrtlowerbound = "1";
		for(int i=1; i<sqrt(lowerstring.size()); ++i) {
			sqrtlowerbound += "0";
		}

		//cout << "lower bound: " << sqrtlowerbound << endl;

		//Palindrome p(lower.sqrt().toStrDec());
		Palindrome p(sqrtlowerbound);
		//p.print();

		int nhits = 0;
		while(!above_range) {
			p.check_square(lower, upper, is_palindrome, above_range, below_range);
			if(!below_range && !above_range && is_palindrome) {nhits++; /*p.print();*/ }
			p.increment();
		}

		cout << "Case #" << casenum << ": " << nhits << endl;
	}

	return 0;
}

