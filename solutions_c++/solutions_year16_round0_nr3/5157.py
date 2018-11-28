// CoinJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

typedef unsigned int UINT;
typedef unsigned __int64 UINT64;

typedef std::vector<UINT> UintArray;

namespace
{
//
std::string GenerateCoin(UINT coinSize)
{
	UINT n = 0;
	if (rand_s(&n) != 0)
		throw std::runtime_error("rand_s failed!");

	char coin[64] = {0};
	_ltoa_s(n, coin, 2);

	coin[0] = '1';

	for (UINT i = strlen(coin); i < coinSize - 1; ++i)
	{
		coin[i] = '0';
	}

	coin[coinSize - 1] = '1';
	coin[coinSize] = '\0';

	return coin;
}

//
UINT GetNontrivialDivisor(UINT64 n)
{
	for (UINT i = 2; i < 1000; ++i)
	{
		if ((n % i) == 0)
			return i;
	}
	return 0;
}

} // namespace


//
int _tmain(int argc, _TCHAR* argv[])
{
	try
	{
		std::ofstream output("output.txt");
		if (!output)
			throw std::runtime_error("Can't open output file");

		output << "Case #1: " << std::endl;

		const UINT coinSize = 16;
		const UINT coinCount = 50;

		std::vector<std::string> minedCoins;

		for (UINT i = 1; i <= coinCount; ++i)
		{
			std::string coin;
			UintArray divisors;

			for (;;)
			{
				coin = GenerateCoin(coinSize);

				if (std::find(std::begin(minedCoins), std::end(minedCoins), coin) != std::end(minedCoins))
					continue;

				UINT divisor = 0;
				for (int i = 2; i <= 10; ++i)
				{
					divisor = GetNontrivialDivisor(_strtoui64(coin.c_str(), nullptr, i));

					if (!divisor)
						break;

					divisors.push_back(divisor);
				}

				if (!divisor)
				{
					divisors.clear();
					continue;
				}

				minedCoins.push_back(coin);

				output << coin << "\t";
				for (UINT i = 0; i < divisors.size(); ++i)
					output << divisors[i] << " ";

				output << std::endl;
				break;
			}
		}
	}
	catch (const std::exception& e)
	{
		std::cout << "Error: " << e.what() << std::endl;
	}

	system("pause");
	return 0;
}

