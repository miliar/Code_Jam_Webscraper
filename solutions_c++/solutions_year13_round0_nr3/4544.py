#include <cmath>

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

bool palindrome(double i);

int main(int argc, char** argv)
{
	if (argc != 2)
	{
		std::cout << "Usage: Fair_and_Square.exe <input_file>" << std::endl;
		return -1;
	}

	std::ifstream input(argv[1], std::ios::in);
	int index_limit = -1;
	input >> index_limit;

	for (int index = 1; index <= index_limit; ++index)
	{
		int result = 0;
		double from = 0.0;
		input >> from;
		double to = 0.0;
		input >> to;

		for (double i = ceil(sqrt(from)); ; ++i)
		{
			if (palindrome(i))
			{
				double aux = i * i;
				
				if (aux > to)
				{
					break;
				}

				if (palindrome(aux))
				{
					++result;
				}
			}
		}

		std::cout << "Case #" << index << ": " << result << std::endl;
	}
	return 0;
}

bool palindrome(double i)
{
	std::stringstream io;
	io << i;
	std::string aux;
	io >> aux;

	bool itis = true;
	
	std::string::iterator it1 = aux.begin();
	std::string::reverse_iterator it2 = aux.rbegin();
	for (size_t i = 0; i < (aux.size() / 2) + 1 && itis ; ++i, ++it1, ++it2)
	{
		itis = *it1 == *it2;
	}

	return itis;
}
