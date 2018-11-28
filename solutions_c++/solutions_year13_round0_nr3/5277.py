#include <cmath>
#include <iostream>
#include <sstream>
#include <string>

bool is_palindrome(int i)
{
	std::ostringstream ss;
	ss << i;
	auto s(ss.str());
	for (int i = 0; i < s.size() / 2; ++i)
		if (s[i] != s[s.size() - 1 - i])
			return false;
	return true;
}

bool is_fair_and_square(int i)
{
	if (!is_palindrome(i))
		return false;

	int ii(std::floor(std::sqrt((long double)(i)) + .5L));
	if (ii * ii != i)
		return false;

	if (!is_palindrome(ii))
		return false;

	return true;
}

int main()
{
	int t;
	{
		std::string s;
		std::getline(std::cin, s);
		std::istringstream ss(s);
		ss >> t;
	}

	for (int i = 0; i < t; ++i)
	{
		int a, b;
		{
			std::string s;
			std::getline(std::cin, s);
			std::istringstream ss(s);
			ss >> a >> b;
		}

		int n = 0;
		for (int i = a; i <= b; ++i)
			if (is_fair_and_square(i)) ++n;

		std::cout << "Case #" << i + 1 << ": " << n << std::endl;
	}
}
