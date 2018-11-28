#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <string>
#include <iterator>

template <class T>
std::string convertToString(T a)
{
	std::stringstream ss;
	ss << a;

	return ss.str();
}

void read(int& t, std::vector<unsigned long long>& input)
{
	std::ifstream in("input.txt");
	if (!in.good())
	{
		std::cerr << "NOOOOOOOOOOOOOO\n";
		exit(1);
	
	}
	in >> t;
	input.resize(t);
	for (int i = 0; i < t; ++i)
	{
		in >> input[i];
	}
}

void digitize(unsigned long long n, std::vector<short>& digits)
{
	do {
		digits[n % 10] = 1;
		n /= 10;
	} while (n != 0);
}

std::string solve(unsigned long long n)
{
	std::vector<short> digits(10, 0);
	
	for (unsigned long long i = 1;; ++i)
	{
		unsigned long long newN = i*n;
		if (newN == n*(i - 1))
			return "INSOMNIA";
		digitize(newN, digits);

		auto it = std::find(digits.begin(), digits.end(), 0);
		if (it == digits.end())
			return convertToString(newN);
	}
}

int main()
{
	int t;
	std::vector<unsigned long long> input;
	read(t, input);

	std::ofstream out("output.txt");
	for (int i = 1; i <= t; ++i)
	{
		out << "Case #" << i << ": " << solve(input[i-1]) << std::endl;
	}
	 
	return 0;
}