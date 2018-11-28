#include <string>
#include <vector>
#include <iostream>
#include <fstream>

template <typename T>
void printCase(int id, T result, std::ofstream& stream)
{
	stream << "Case #" << id + 1 << ": " << result << std::endl;
}

int main()
{
	int T;
	std::cin >> T;

	std::string line;
	// Consume
	std::getline(std::cin, line);

	std::vector<std::string> testCases;
	for (int i = 0; i < T; i++)
	{
		std::getline(std::cin, line);
		testCases.push_back(line);
	}

	std::ofstream fStream;
	fStream.open("result.txt");

	for (int i = 0; i < T; i++)
	{
		line = testCases[i];

		std::string result;
		int currentValue = 0;
		result.push_back(line[0]);
		currentValue = line[0];

		for (int c = 1; c < line.size(); c++)
		{
			if ((int)(line[c]) >= currentValue)
			{
				result.insert(result.begin(), line[c]);
				currentValue = line[c];
			}
			else
				result.push_back(line[c]);
		}

		printCase(i, result, fStream);
	}
}