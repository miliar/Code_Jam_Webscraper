#include <iostream>
#include <fstream>
#include <limits>
#include <string>

typedef unsigned long long Number;

Number find_n(std::string s)
{
	bool found[10] = {};
	int left = 10;
	int l = s.length();
	int res = 0;
	while (--l >= 0)
	{
		if (s[l] == '-')
		{
			++res;
			for (int n = 0; n <= l; ++n)
			{
				s[n] = s[n] == '-' ? '+' : '-';
			}
		}
	}
	return res;
}
int main()
{
	int t;
	std::ifstream is("L:/B-small-attempt0.in");
	is >> t;
	int c = 1;
	while (t-- > 0)
	{
		std::string s;
		is >> s;
		Number res = find_n(s);
		std::cout << "Case #" << c++ << ": ";
		std::cout << res << std::endl;
	}
	return 0;
}