#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

inline unsigned long long getLastNumberToFallAsleep(unsigned long long initial)
{
	if (initial == 0)
		return 0;

	static unsigned long long UPPERBOUND = std::numeric_limits<unsigned long long>::max()/2;
	int bitset = 0;
	for (int b = 0; b < 10; b++)
		bitset |= (0x1 << b);

	unsigned long long i;
	for (i = initial; i < UPPERBOUND; i += initial)
	{
		unsigned long long x = i;
		do
		{
			bitset &= ~(0x1 << (x % 10));
			x /= 10;
		} while (x > 0);

		if (bitset == 0)
			break;
	}

	return i > UPPERBOUND ? 0 : i;
}

int main( int argc, char* argv[] )
{
	if (argc != 1)
		std::cerr << "no parameter allowed";

	int n;
	std::cin >> n;
	for (int i = 0; i < n; ++i)
	{
		unsigned long long initial;
		std::cin >> initial;
		std::cout << "Case #" << i + 1 << ": ";
		unsigned long long last = getLastNumberToFallAsleep(initial);
		if (last == 0)
			std::cout << "INSOMNIA";
		else
			std::cout << last;
		std::cout << std::endl;
	}

	return 0;
}