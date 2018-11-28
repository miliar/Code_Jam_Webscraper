// CountingSheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

typedef unsigned int UINT;
typedef unsigned __int64 UINT64;

typedef std::vector<UINT64> UintArray;

namespace
{

UintArray GetNumbersFromFile(const std::string& fileName)
{
	std::ifstream file(fileName);
	if (!file)
		throw std::runtime_error("Can't open input file");

	UintArray result;
	std::string s;

	while (std::getline(file, s))
		result.push_back(static_cast<UINT64>(_atoi64(s.c_str())));

	return result;
}

} // namespace


//
int _tmain(int argc, _TCHAR* argv[])
{
	try
	{
		UintArray inputNumbers = GetNumbersFromFile("source.txt");

		std::ofstream output("output.txt");
		if (!output)
			throw std::runtime_error("Can't open output file");

		const size_t numberCount = inputNumbers[0];
		inputNumbers.erase(std::begin(inputNumbers));
		assert(!inputNumbers.empty() && numberCount <= inputNumbers.size());

		for (size_t i = 0; i < numberCount; ++i)
		{
			const UINT64 N = inputNumbers[i];
			if (N == 0)
			{
				output << "Case #" << i+1 << ": " << "INSOMNIA" << std::endl;
				continue;
			}

			std::set<UINT> countedDigits;
			UINT64 nextNum = N;
			for (;;)
			{
				UINT64 num = nextNum;
				while (num)
				{
					const UINT d = num % 10;
					countedDigits.insert(d);
					num /= 10;
				}

				if (countedDigits.size() == 10)
				{
					output << "Case #" << i+1 << ": " << nextNum << std::endl;
					break;
				}

				nextNum += N;
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

