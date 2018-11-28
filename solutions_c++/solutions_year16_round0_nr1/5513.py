// CountingSheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream file("D:/Dev/GoogleJam/CountingSheep/in.txt");

	//std::ostream& output = std::cout;

	std::ofstream outFile("D:/Dev/GoogleJam/CountingSheep/out.txt");
	std::ostream& output = outFile;

	unsigned int total;
	file >> total;

	unsigned int count = 0;
	std::for_each(std::istream_iterator<uint64_t>(file), std::istream_iterator<uint64_t>(),
		[&](uint64_t in)
	{
		++count;
		if (in == 0)
		{
			output << "Case #" << count << ": INSOMNIA" << std::endl;
			return;
		}

		uint32_t digits = 0;
		const uint64_t max = UINT64_MAX / in;
		for (uint64_t n = 1; n < max; ++n)
		{
			const uint64_t inVal = in * n;
			for (uint64_t val = inVal; val > 0; val /= 10)
			{
				digits |= (1 << val % 10);
			}
			if (digits == 1023)
			{
				output << "Case #" << count << ": " << inVal << std::endl;
				return;
			}
		}

		output << "Case #" << count << ": INSOMNIA" << std::endl;
	});

	return 0;
}
