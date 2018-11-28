#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <stack>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <climits>

typedef std::vector<int> vi;

template <typename T>
void printCase(int id, T result, std::stringstream& stream)
{
	stream << "Case #" << id + 1 << ": " << result << std::endl;
}

std::stringstream testResultStream;


void computeTestCase(int id)
{
	int parties;
	std::cin >> parties;

	int totalCount = 0;

	vi counts;
	counts.resize(26);

	for (int i = 0; i < parties; i++)
	{
		int tmp;
		std::cin >> tmp;

		counts[i] = tmp;
		totalCount += tmp;
	}
	
	std::string removed;
	while (totalCount > 0)
	{
		// Find max
		int maxIndex = 0;
		for (int i = 1; i < parties; i++)
		{
			if (counts[i] <= counts[maxIndex])
				continue;
			maxIndex = i;
		}

		totalCount--;
		counts[maxIndex]--;

		removed += ('A' + maxIndex);
	}

	std::string finalResult;
	int counter = 0;
	for (int i = removed.size() - 1; i >= 0; i--)
	{
		if (counter == 2)
		{
			finalResult += ' ';
			counter = 0;
		}

		finalResult += removed[i];
		counter++;
	}

	std::reverse(finalResult.begin(), finalResult.end());

	printCase(id, finalResult, testResultStream);
}

int main()
{
	int T;
	std::cin >> T;

	std::string line;
	// Consume
	std::getline(std::cin, line);

	std::ofstream fStream;
	fStream.open("result.txt");

	for (int i = 0; i < T; i++)
		computeTestCase(i);

	fStream << testResultStream.str() << std::flush;
}