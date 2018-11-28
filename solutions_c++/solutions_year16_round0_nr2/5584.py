// RevengeofthePancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream file("D:/Dev/GoogleJam/RevengeofthePancakesIn.txt");

	//std::ostream& output = std::cout;
	std::ofstream outFile("D:/Dev/GoogleJam/RevengeofthePancakesOut.txt");
	std::ostream& output = outFile;

	unsigned int total;
	file >> total;

	unsigned int count = 0;
	std::for_each(std::istream_iterator<std::string>(file), std::istream_iterator<std::string>(),
		[&](const std::string& in)
	{
		++count;

		unsigned int flip = 0;
		char cur = '+';
		for (auto iter = in.rbegin(); iter != in.rend(); ++iter)
		{
			if (*iter != cur)
			{
				++flip;
				cur = (cur == '+' ? '-' : '+');
			}
		}

		output << "Case #" << count << ": " << flip << std::endl;
	});

	return 0;
}
