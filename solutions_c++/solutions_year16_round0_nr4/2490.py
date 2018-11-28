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
	std::ifstream is("L:/D-small-attempt0.in");
	is >> t;
	int c = 1;
	while (t-- > 0)
	{
		int K, C, S;
		is >> K >> C >> S;
//		Number res = find_n(s);
		std::cout << "Case #" << c++ << ":";
		for (int n = 1; n <= S; ++n)
			std::cout << " " << n;
		std::cout << std::endl;
	}
	return 0;
}