#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

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

bool isPalinDrome(long long x)
{
	std::stringstream ss;
	ss << x;
	const std::string xString = ss.str();

	const std::size_t numDigits = xString.length();
	if (numDigits == 1)
		return true;

	for (std::size_t i = 0; i < numDigits / 2; ++i)
	{
		if (xString[i] != xString[numDigits-i-1])
			return false;
	}

	return true;
}

bool isSquare(long long x, long long& squareRoot)
{
	for (long long i = 0; i * i <= x; ++i)
	{
		if (i * i == x)
		{
			squareRoot = i;
			return true;
		}
	}
	return false;
}

void appendSolutionToFile(long long A, long long B, long long id, std::ofstream& outfile)
{
	std::stringstream result;
	long long numFairAndSquare = 0;
	for (long long x = A; x <= B; ++x)
	{
		long long squareRoot;
		if (isSquare(x, squareRoot) && isPalinDrome(x) && isPalinDrome(squareRoot))
			++numFairAndSquare;
	}

	outfile << "Case #" << id << ": " << numFairAndSquare;
}

void main()
{
	std::cout << "filename > ";
	std::string filename;
	std::cin >> filename;

	std::ifstream infile(filename.c_str());

	std::string line;
	std::getline(infile, line);

	std::ofstream outfile("c.out");

	const long long numTestCases = parse<long long>(line);

	for (long long i = 0; i < numTestCases; ++i)
	{
		std::getline(infile, line);
		long long A, B;
		parse(line, A, B);

		appendSolutionToFile(A, B, i + 1, outfile);

		outfile << std::endl;
	}
}
