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

void read(int& t, std::vector<std::string>& input)
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

int simpleCount(const std::string& s)
{
	if (s == "-")
		return 1;
	if (s == "+")
		return 0;
	if (s == "-+")
		return 1;
	if (s == "+-")
		return 2;
	return -1;
}

char flip(char c)
{
	if (c == '+')
		return '-';
	return '+';
}

void flip(std::string& s, int begin, int end)
{
	//std::cout << "flip: " << s << std::endl;
	while (begin < end)
	{
		char sbeg = s[begin];
		char send = s[end];

		s[end] = flip(sbeg);
		s[begin] = flip(send);
		++begin;
		--end;
	}
	if (begin == end)
	{
		s[begin] = flip(s[begin]);
	}
}

int solve(std::string& s)
{
	//std::cout << "solve: " << s << std::endl;
	int count = 0;

	auto it = s.rbegin();
	while (it != s.rend() && (*it == '+'))
	{
		s.pop_back();
		it = s.rbegin();
	}
	if (s.empty())
		return count;

	int c = simpleCount(s);
	if (c > 0)
		return count += c;
	
	++count;
	int end = s.size() - 1;
	if (s[end] == s[0])
	{
		flip(s, 0, s.size()-1);

		return count += solve(s);
	}
	else
	{
		while (end >= 0 && s[end] == '-')
		{
			--end;
		}
		if (end == 0)
			return count + 1;
		flip(s, 0, end);

		return count += solve(s);
	}
}

int main()
{
	int t;
	std::vector<std::string> input;
	read(t, input);

	std::ofstream out("output.txt");
	for (int i = 1; i <= t; ++i)
	{
		out << "Case #" << i << ": " << solve(input[i - 1]) << std::endl;
	}

	return 0;
}