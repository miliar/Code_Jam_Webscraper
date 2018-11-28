//============================================================================
// Name        : codejam.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <iostream>
#include <boost/foreach.hpp>
#include <boost/range/irange.hpp>
#include <boost/lexical_cast.hpp>
#include <string>
#include <bitset>
#include <vector>

#include <cstdlib>
#include <cstring>

using namespace std;
using namespace boost;


void integer_to_bcd1(unsigned long integer, vector<uint8_t> & bcd)
{
	unsigned long max_pow = ceil(log(integer) / log(10));

	if (pow(10, max_pow) > integer)
	{
		max_pow--;
	}

	for (long power = max_pow; power >= 0; power--)
	{
		unsigned long order = pow(10, power);

		unsigned long digit = integer / order;

		//std::cout << "KN: " << kN << endl;
		//std::cout << "order: " << order << endl;
		//std::cout << "Digit: " << digit << endl;

		integer -= digit * order;

		bcd.push_back(digit);
	}

}

void integer_to_bcd2(unsigned long integer, vector<uint8_t> & bcd)
{
	unsigned long max_pow = ceil(log(integer) / log(10));

	if (pow(10, max_pow) > integer)
	{
		max_pow--;
	}

	bcd.resize(max_pow+1);

	sprintf((char*) &bcd[0], "%lu", integer);

	BOOST_FOREACH(uint8_t & digit, bcd)
	{
		digit = digit - '0';
	}

}


unsigned long largest_kN(unsigned long N)
{
	unsigned long k = 1;
	unsigned long kN;
	bitset<10> digits(0);
	vector<uint8_t> bcd;
	while (digits.count() < 10)
	{
		kN = k*N;

		bcd.clear();

		integer_to_bcd2(kN, bcd);

		BOOST_FOREACH(uint8_t digit, bcd)
		{
			digits.set(digit);
		}

		k++;
	}

	return kN;
}


int main() {

	int T;
	cin >> T;

	BOOST_FOREACH(int t, irange(0, T))
	{
		unsigned long N;
		cin >> N;

		string output;

		if (N == 0)
		{
			output = "INSOMNIA";
		}
		else
		{
			unsigned long kN = largest_kN(N);
			output = lexical_cast<string>(kN);
		}

		cout << "Case #" << (t+1) << ": " << output << "\n";
	}

	cout.flush();


	return 0;
}

