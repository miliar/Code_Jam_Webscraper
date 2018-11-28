#include <iostream>
#include <sstream>
#include <algorithm>
#include <math.h>

bool ispalindrome(unsigned long long l)
{
	std::stringstream ss;
	ss << l;

	std::string s1 = ss.str();
	std::string s2 = s1;

	std::reverse(s2.begin(), s2.end());

	if (s1 == s2)
		return true;

	return false;
}

bool isSquare(unsigned long long n,  unsigned long long& out)
{
	(unsigned long long) out = sqrt((long double )n);
	if (out * out == n)
		return true;
	return false;
}

int search(unsigned long long a,  unsigned long long b)
{
	unsigned long count = 0;
	for (unsigned long long i = a; i <= b; i++)
	{
		if (ispalindrome(i))
		{
			unsigned long long sq = 0;
			if (isSquare(i,sq))
			{
				if (ispalindrome(sq))
					count++;
			}
		}
	}

	return count;
}



int main(int argc, char* argv[])
{
	int T;
	std::cin >> T;

	for (int i = 0; i < T; i++)
	{
		unsigned long long a, b;

		std::cin >> a;
		std::cin >> b;

		std::cout << "Case #" << i + 1 << ": " << search(a,b)  << std::endl;;
	}


	return 0;
}	