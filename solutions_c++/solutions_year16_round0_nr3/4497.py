#include <bitset>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>

#include <string>

#include <iterator>


template <class T>
std::string convertToString(T a)
{
	std::stringstream ss;
	ss << a;

	return ss.str();
}

void read(int& t, int& n, int& j)
{
	std::ifstream in("input.txt");
	if (!in.good())
	{
		std::cerr << "NOOOOOOOOOOOOOO\n";
		exit(1);

	}
	in >> t >> n >> j;
}

unsigned long long fromBase(const std::string& bits, int base)
{
	unsigned long long output = 0;
	unsigned long long powVal = 1;


	for (auto it = bits.rbegin(); it != bits.rend(); ++it)
	{
		output += (*it - '0')*powVal;
		powVal *= base;
	}
	return output;
}

bool isPrime(unsigned long long value, unsigned long long& div)
{
	
	unsigned long long limit = (unsigned long long) sqrt(value);
	//std::cout << "isPrime: " << value << " - " << limit << std::endl;

	for (unsigned long long it = 2; it <= limit; ++it)
	{
		if ((value % it) == 0)
		{
			div = it;
			return false;
		}
	}
	return true;
}

bool checkCoinJam(const std::string& bits, std::vector<unsigned long long>& divisors)
{
	for (int base = 2; base <= 10; ++base)
	{
		unsigned long long value = fromBase(bits, base);
		if (isPrime(value, divisors[base - 2]))
			return false;
	}
	return true;
}

void nextBits(std::string& bits)
{
	static const int N = 16;

	std::bitset<N-2> bs(bits.substr(1, bits.size() - 2));
	unsigned long long ul = bs.to_ullong();
	++ul;
	std::bitset<N-2> newbs(ul);
	bits.replace(1, bits.size() - 2, newbs.to_string());

}

int solve(std::ofstream& out, int n, int j)
{
	int numj = 0;

	std::string bits(n, '0');
	bits[0] = '1';
	bits[n - 1] = '1';

	while (numj < j)
	{
		std::vector<unsigned long long> divisors(9, 0);
		if (checkCoinJam(bits, divisors))
		{
			out << bits;

			for (auto it = divisors.begin(); it != divisors.end(); ++it)
			{
				out << " " << *it;
			}
			out << std::endl;
			++numj;
		}
		nextBits(bits);
	}
}

int main()
{
	int t;
	int n;
	int j;
	read(t, n, j);

	std::ofstream out("output.txt");
	for (int i = 1; i <= t; ++i)
	{
		out << "Case #" << i << ":\n";
		solve(out, n, j);
	}

	return 0;
}