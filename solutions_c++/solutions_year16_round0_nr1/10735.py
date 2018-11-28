#include <iostream>
#include <fstream>
#include <ostream>
#include <sstream>
#include <vector>
#include <set>

enum ZeroToNine
{
	_1 = 49,
	_2
};

std::set<int> extractUniqueNumbers(long long number)
{
	std::stringstream ss;
	ss << number;

	std::string strNumber;
	ss >> strNumber;

	std::set<int> numbers;
	for (const char& c : strNumber)
	{
		int n = (int)c - 48;
		numbers.insert(n);
	}

	return numbers;
}

int insertNumbers(long long number, std::set<int>& numbers)
{
	std::stringstream ss;
	ss << number;

	std::string strNumber;
	ss >> strNumber;

	for (const char& c : strNumber)
	{
		int n = (int)c - 48;
		numbers.insert(n);

		if (numbers.size() == 10)
		{
			return n;
		}
	}

	return -1;
}

void main()
{
	//std::set<int> numbers = extractUniqueNumbers(1234567890);
	/*for (int i : numbers)
	{
		std::cout << i << ", ";
	}*/

	std::ifstream in = std::ifstream("A-large.in");

	std::ofstream out = std::ofstream("out.txt");

	std::string line;
	std::getline(in, line);
	
	int numTestCases = std::stoi(line);

	for (int i = 0; i < numTestCases; ++i)
	{
		std::getline(in, line);

		int num = std::stoi(line);
		//std::cout << num << std::endl;

		if (num == 0)
		{
			//std::cout << "Case #" << (i + 1) << ": INSOMNIA" << std::endl;
			out << "Case #" << (i + 1) << ": INSOMNIA" << std::endl;
		}
		else
		{
			std::set<int> numbers;
			long long current = num;
			int result = -1;
			int multiplicator = 1;
			while (result == -1)
			{
				current = multiplicator * num;
				result = insertNumbers(current, numbers);

				multiplicator += 1;
			}

			//std::cout << "Case #" << (i + 1) << ": " << current << std::endl;
			out << "Case #" << (i + 1) << ": " << current << std::endl;
		}
		
		
	}

	out.flush();
	out.close();

	getchar();
	
}

