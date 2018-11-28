#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

#include "BigInteger.hh"

using namespace std;

stringstream out;

BigInteger convertBinaryToBase(string binary, int base)
{
	int length = binary.length();
	BigInteger result = 0;
	BigInteger pow = 1;
	for (int i = length - 1; i >= 0; i--)
	{
		if (binary[i] == '1')
			result += pow;
		pow *= base;
	}
	return result;
}

bool MaR(BigInteger x, BigInteger n) 
{
	if (x >= n) return 0;
	BigInteger d = 1, y;
	BigInteger t = 0;
	BigInteger l = n - 1;
	while (l % 2 == 0)
	{
		t++;
		l /= 2;
	}

	for (; l > 0 || t != 0; l /= 2)
	{
		t--;
		if (l % 2 == 1)
			d = (d * x) % n;

		if (l != 0)
		{
			x = d;
			l = -1;
		}

		y = (x * x) % n;
		if (y == 1 && x != 1 && x != n - 1)
			return 1;
		x = y;
	}
	return (x != 1);
}

bool isPrime(BigInteger x)
{
	return !(x < 2 || MaR(2, x) || MaR(325, x) || MaR(9375, x) || MaR(28178, x) || MaR(450775, x) || MaR(9780504, x) || MaR(1795265022, x));
}

BigInteger getDivisor(BigInteger number)
{
	if (number % 2 == 0)
		return 2;

	if (isPrime(number))
		return -1;

	for (BigInteger i = 3; ; i += 2)
	{
		if (i > 1000)
			return -1;
		if (number % i == 0)
			return i;
	}
	return -1;
}

string getNextBinary(string binary)
{
	int c = 1;
	int i = binary.length() - 2;
	while (c) 
	{
		if (binary[i] == '0')
		{
			binary[i] = '1';
			c = 0;
		}
		else
		{
			binary[i] = '0';
			c = 1;
		}
		i--;
	}
	return binary;
}

void function()
{
	int n, j;
	cin >> n >> j;
	string strNumber = "1" + string(n - 2, '0') + "1";
	BigInteger divisors[9];
	int nFound = 0;
	bool found;
	out << endl;
	while (nFound < j) {
		found = true;
		for (int i = 2; i <= 10; i++)
		{
			BigInteger number = convertBinaryToBase(strNumber, i);
			BigInteger divisor = getDivisor(number);
			if (divisor != -1)
				divisors[i - 2] = divisor;
			else
			{
				found = false;
				break;
			}
		}
		if (found)
		{
			out << strNumber;
			for (int i = 0; i < 9; i++)
				out << " " << divisors[i].toLong();
			out << endl;
			nFound++;

			clog << nFound << endl;
		}
		strNumber = getNextBinary(strNumber);
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		out << "Case #" << i << ": ";
		function();
	}

	cout << out.str();

	return 0;
}