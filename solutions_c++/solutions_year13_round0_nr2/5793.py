#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

typedef std::vector<std::vector<unsigned int> > Lawn;

template<typename T>
T parse(const std::string& string)
{
	std::stringstream ss(string);
	T number;
	ss >> number;
	return number;
}

template <typename T> 
void parse(const std::string& string, T& value1, T& value2)
{
	std::stringstream ss(string);
	ss >> value1;
	ss >> value2;
}

bool horizontalPossible(const Lawn& lawn, unsigned int n, unsigned int m, unsigned int h, unsigned int ai)
{
	const std::vector<unsigned int>& row = lawn[ai];
	for (unsigned int x = 0; x < m; ++x)
	{
		if (row[x] > h)
			return false;
	}
	return true;
}

bool verticalPossible(const Lawn& lawn, unsigned int n, unsigned int m, unsigned int h, unsigned int aj)
{
	for (unsigned int x = 0; x < n; ++x)
	{
		if (lawn[x][aj] > h)
			return false;
	}
	return true;
}

bool lawnLayoutPossible(const Lawn& lawn, unsigned int n, unsigned int m, unsigned int lowest)
{
	for (unsigned int h = 100; h >= lowest; --h)
	{
		for (unsigned int ai = 0; ai < n; ++ai)
		{
			for (unsigned int aj = 0; aj < m; ++aj)
			{
				if (lawn[ai][aj] == h && !horizontalPossible(lawn, n, m, h, ai) && !verticalPossible(lawn, n, m, h, aj))
					return false;
			}
		}
	}

	return true;
}

void appendSolutionToFile(const Lawn& lawn, unsigned int n, unsigned int m, unsigned int lowest, unsigned int id, std::ofstream& outfile)
{
	std::stringstream result;
	outfile << "Case #" << id << ": " << (lawnLayoutPossible(lawn, n, m, lowest) ? "YES" : "NO");
}

void main()
{
	std::cout << "filename > ";
	std::string filename;
	std::cin >> filename;

	std::ifstream infile(filename.c_str());

	std::string line;
	std::getline(infile, line);

	std::ofstream outfile("b.out");

	const unsigned int numTestCases = parse<unsigned int>(line);

	for (unsigned int i = 0; i < numTestCases; ++i)
	{
		std::getline(infile, line);
		unsigned int n, m;
		parse(line, n, m);
		Lawn lawn(n);
		unsigned int lowest = static_cast<unsigned int>(-1);

		for (unsigned int ai = 0; ai < n; ++ai)
		{
			std::getline(infile, line);
			std::stringstream lineStream(line);

			lawn[ai].resize(m);

			for (unsigned int aj = 0; aj < m; ++aj)
			{
				unsigned int aij;
				lineStream >> aij;
				lawn[ai][aj] = aij;
				lowest = aij < lowest ? aij : lowest;
			}
		}

		appendSolutionToFile(lawn, n, m, lowest, i + 1, outfile);
		outfile << std::endl;
	}
}
