// main.cpp : Defines the entry point for the console application.
//
// This program uses the BigInteger/BigUnsigned C++ library written by Matt McCutchen <matt@mattmccutchen.net>
// It is available at https://mattmccutchen.net/bigint/ and is freely available in the public domain. See the
// README file located in the bundle at the address mentioned above.
//
// I have implemented an integer square root function, power function, and istream handlers that are included
// in the code here below to supplement the features in Matt's library.
// 

#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
#include <math.h>
#include "BigIntegerLibrary.hh"

using namespace std;

typedef unsigned int uint;

std::istream &operator >>(std::istream &is, BigUnsigned &x);
std::istream &operator >>(std::istream &is, BigInteger &x);
BigUnsigned sqrt(const BigUnsigned &a);
BigUnsigned pow(const BigUnsigned &a, const BigUnsigned &b);

void vecprint(const vector<uint> &v);

int main()
{
	int T;
	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		uint A;
		uint N;
		uint steps = 0;

		cin >> A >> N;

		vector<uint> Nsizes;
		uint mote;
		uint largest;
		bool breaker = false;
		for (uint i = 1; i <= N; ++i)
		{
			cin >> mote;
			Nsizes.push_back(mote);
		}

		// Sort mote array
		sort(Nsizes.begin(), Nsizes.end(), greater<uint>());
		//cout << "Start size: " << A << endl;
		//vecprint(Nsizes); cout << endl;

		// Simple check: if starting size is already bigger than biggest mote, we're done
		largest = Nsizes.front();
		if (A > largest) {
			cout << "Case #" << (t+1) << ": " << steps << endl;
			continue;
		}

		// Reduce down the list by greedy consumption until we can't consume any longer
		int place = 0;
		while (place < Nsizes.size())
		{
			int j;
			for (place = 0, j = Nsizes.size(); place < j && Nsizes[place] >= A; ++place) {};

			// Now, consume everything from there to the end and grow in size
			for (int i = place, j = Nsizes.size(); i < j; ++i)
			{
				A += Nsizes[i];
			}

			// Remove these
			Nsizes.erase(Nsizes.begin() + place, Nsizes.end());

			// Look again
		}

		// Done consuming. Is the list empty?
		if (Nsizes.size() == 0)
		{
			cout << "Case #" << (t+1) << ": " << steps << endl;
			continue;
		}
		else
		{
			do
			{
				if (A > largest) {
					breaker = true;
				}
				else {
					mote = Nsizes.back();
					if (A > mote) {
						// Eat it and grow in size. Muwahaha!
						Nsizes.pop_back();
						A += mote;
					}
					else
					{
						// Can't eat any more small ones, so now we need to make a change/decision
						// We need to create a new one large enough to eat which hopefully is large enough to
						// grow us the size we need to keep going.
						if (A == 1) {
							// Too small to be able to eat something, so we have to remove item instead. In fact,
							// we must remove ALL of them.
							steps += Nsizes.size();
							Nsizes.empty();
							breaker = true;
						}
						else
						{
							// We either need to add sizes or remove items. Check to see which is "cheaper"
							//double numd = ceil(log10( (double)mote/(A-1) ) / log10(2));
							int numToAdd = (int)ceil(log10( (double)mote/(A-1) ) / 0.3010299956f);
							if (numToAdd <= Nsizes.size())
							{
								// It's less to add to get up to eating capacity than to remove them all
								uint newone;
								do {
									newone = A - 1;
									A += newone;
									//cout << "Size is now: " << A << endl;
									steps++;
								} while (A <= mote);
							}
							else
							{
								// It's cheaper to just remove what's left
								steps += Nsizes.size();
								Nsizes.empty();
								breaker = true;
							}
						}
					}
				}
			} while (breaker == false);

			cout << "Case #" << (t+1) << ": " << steps << endl;
		}
	}

	return 0;
}

std::istream& operator >>(std::istream &is, BigUnsigned &x) {
	std::string bigstr;

	is >> bigstr;
	x = stringToBigUnsigned(bigstr);

	return is;
}

std::istream &operator >>(std::istream &is, BigInteger &x) {
	std::string bigstr;

	is >> bigstr;
	x = stringToBigInteger(bigstr);

	return is;
}

/* Sqrt function
* Adapted from method posted on StackOverflow by Fredrik Johansson
* http://stackoverflow.com/questions/1623375/writing-your-own-square-root-function
*/
BigUnsigned sqrt(BigUnsigned &a) {
	long NB = a.bitLength();
	BigUnsigned twop(2);

	twop <<= (NB >> 1);
	BigUnsigned x(twop);
	BigUnsigned y(0);

	while (true)
	{
		y = (x + (a / x)) >> 1;
		if (y >= x)
			return x;
		x = y;
	}
}

/* Pow function
* Calculates a^b power, with a and b both BigUnsigned
* Unknown behavior for very large values of b
*/
BigUnsigned pow(const BigUnsigned &a, const BigUnsigned &b)
{
	BigUnsigned result(1);
	BigUnsigned n(b);
	BigUnsigned x(a);

	while (n != 0)
	{
		if (n.getBit(0) == 1)
		{
			result *= x;
			n--;
		}
		x *= x;
		n >>= 1;
	}
	return result;
}

void vecprint(const vector<uint> &v)
{
	for (uint val : v)
	{
		cout << val << " ";
	}
}