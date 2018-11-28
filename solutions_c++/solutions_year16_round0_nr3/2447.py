#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <array>
#include <cassert>


std::string dec2bin(unsigned __int64 n) {
	const int size = sizeof(n) * 8;
	std::string res;
	bool s = 0;
	for (unsigned __int64 a = 0; a<size; a++) {
		bool bit = n >> (size - 1);
		if (bit)
			s = 1;
		if (s)
			res.push_back(bit + '0');
		n <<= 1;
	}
	if (!res.size())
		res.push_back('0');
	return res;
}


bool IsPrime(unsigned __int64 number)
{
	unsigned __int64 i;

	for (i = 2; i*i<=number; i++)
	{
		if (number % i == 0)
		{
			return false;
		}
	}

	return true;
}


std::array<unsigned __int64, 9> IsJamcoin(const std::string& str, bool& bValid)
{
	bValid = true;
	std::array<unsigned __int64, 9> divisors;
	for (unsigned __int64 base = 2; base < 11; base++)
	{
		unsigned __int64 value = 0;
		for (unsigned __int64 i = str.size(); i > 0; i--)
		{
			unsigned __int64 power = i - 1;
			unsigned __int64 digit = static_cast<unsigned __int64>(str[power]) - 48;
			unsigned __int64 oldValue = value;
			value += (unsigned __int64)pow(base, power) * digit;
			assert(value >= oldValue); //Avoid overflow
		}
		for (unsigned __int64 i = 2; i < (unsigned __int64)ceil(sqrt((float)value)); i++)
		{
			if (value % i == 0)
			{
				divisors[base - 2] = i;
				break;
			}
		}
		if (IsPrime(value))
			bValid = false;
	}
	return divisors;
}


int main()
{
	std::ofstream out("output.txt");

	unsigned __int64 N = 16, J = 50;

	out << "Case #1: " << std::endl;

	unsigned __int64 Max = (unsigned __int64)pow(2, N / 2) - 1; //Used to help generate the jamcoins

	for (unsigned __int64 i = 0; i < J; i++)
	{
		std::string forward = dec2bin(Max - i);

		std::string reversed = forward;
		std::reverse(reversed.begin(), reversed.end());

		std::string jamcoin = forward + reversed;

		bool bValid = true;
		std::array<unsigned __int64, 9> divisors = IsJamcoin(jamcoin, bValid);

		if (bValid)
		{
			out << jamcoin;
			for (unsigned __int64 j = 0; j < 9; j++)
			{
				out << ' ' << divisors[j];
			}
			out << std::endl;
		}
		else
		{
			J++;
		}
	}

	out.close();

	return 0;
}


