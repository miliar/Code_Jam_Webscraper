#include <iostream>
#include <vector>
#include <fstream>

#define _FILE

int main(int argc, char *argv[])
{
#ifdef _FILE
	std::ifstream In("Input.txt");
	std::cin.set_rdbuf(In.rdbuf());

	std::ofstream Out("Output.txt");
	std::cout.set_rdbuf(Out.rdbuf());
#endif

	unsigned int Tests;
	std::cin >> Tests;

	for (unsigned int t = 0; t < Tests; t++)
	{
		unsigned int Count;
		std::cin >> Count;

		std::vector<unsigned int> Levels;
		Levels.reserve(Count + 1);

		for (unsigned int x = 0; x < Levels.capacity(); x++)
		{
			char Temp;
			std::cin >> Temp;
			Levels.push_back(Temp - '1' + 1);
		}

		unsigned int Total = 0;
		unsigned int Extra = 0;
		unsigned int x = 0;

		while (x < Levels.size())
		{
			for (x; x <= Total && x < Levels.size(); x++)
				Total += Levels[x];

			if (x == Levels.size())
				break;

			Extra++;
			Total++;
		}

		std::cout << "Case #" << (t + 1) << ": " << Extra << std::endl;
	}

	return 0;
}