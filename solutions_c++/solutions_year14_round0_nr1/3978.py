#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> SplitString (std::string line, char delimeter)
{
	std::vector<std::string> result;

	int delIndex;
	while ((delIndex = line.find (delimeter)) != std::string::npos)
	{
		result.push_back (line.substr (0, delIndex));
		line = line.substr (delIndex + 1);
	}

	result.push_back (line);
	return result;
}

int main ()
{
	std::ifstream input ("A-small-attempt1.in");
	std::ofstream output ("A-small-attempt1.out");
	std::string line;
	getline (input, line);
	size_t n = atoi (line.c_str ());

	int firstArrangement [4][4], secondArrangement[4][4];

	size_t spaceIndex;
	for (size_t t = 0; t < n; ++t)
	{
		getline (input, line);
		size_t firstGuessRow = atoi (line.c_str ()) - 1;

		for (size_t l = 0; l < 4; ++l)
		{
			getline (input, line);

			std::vector<std::string> sublines = SplitString (line, ' ');
			for (size_t col = 0; col < sublines.size (); ++col)
			{
				firstArrangement[l][col] = atoi (sublines[col].c_str ());
			}
		}

		getline (input, line);
		size_t secondGuessRow = atoi (line.c_str ()) - 1;

		for (size_t l = 0; l < 4; ++l)
		{
			getline (input, line);

			std::vector<std::string> sublines = SplitString (line, ' ');
			for (size_t col = 0; col < sublines.size (); ++col)
			{
				secondArrangement[l][col] = atoi (sublines[col].c_str ());
			}
		}

		int matches = 0;
		int matchingNumber;
		for (size_t col1 = 0; col1 < 4; ++col1)
		{
			int subtotal = 1;
			for (size_t col2 = 0; col2 < 4; ++col2)
			{
				subtotal *= firstArrangement[firstGuessRow][col1] - secondArrangement[secondGuessRow][col2];
				if (subtotal == 0) matchingNumber = firstArrangement[firstGuessRow][col1];
			}
			
			if (subtotal == 0) ++matches;
		}

		switch (matches)
		{
		case 0:
			{
				output << "Case #" << t + 1 << ": Volunteer cheated!" << std::endl;
				break;
			}
		case 1:
			{
				output << "Case #" << t + 1 << ": " << matchingNumber << std::endl;
				break;
			}
		default:
			{
				output << "Case #" << t + 1 << ": Bad magician!" << std::endl;
			}
		}
	}

	input.close ();
	output.close ();
	return 0;
}