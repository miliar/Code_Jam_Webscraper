#include <fstream>
#include <string>
#include <vector>

int main()
{
	std::ifstream input("input.txt");
	std::ofstream output("output.txt");

	unsigned int total;
	input >> total;
	for (int i = 0; i < total; ++i)
	{
		unsigned int row1, row2;
		std::vector<bool> cards(16, false);
		unsigned int matches = 0;
		unsigned int match;

		input >> row1;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				unsigned int card;
				input >> card;
				if (j == row1 - 1)
					cards[card] = true;
			}
		}

		input >> row2;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				unsigned int card;
				input >> card;
				if (j == row2 - 1 && cards[card])
				{
					++matches;
					match = card;
				}
			}
		}

		if (matches == 0)
			output << "Case #" << i + 1 << ": Volunteer cheated!" << std::endl;
		else if (matches == 1)
			output << "Case #" << i + 1 << ": " << match << std::endl;
		else
			output << "Case #" << i + 1 << ": Bad magician!" << std::endl;
	}
}
