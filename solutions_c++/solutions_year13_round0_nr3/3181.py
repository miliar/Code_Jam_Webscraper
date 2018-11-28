#include <cstdio>
#include <cmath>
#include <iostream>

bool is_palindrome(int v)
{
	static char buffer[128];
	int n = sprintf(buffer, "%d", v);

	for (int i = 0; i < n/2; i++)
		if (buffer[i] != buffer[n-1])
			return false;
	return true;
}


int next_palindrome(int v)
{
	v++;
	for ( ; !is_palindrome(v); v++);
	return v;
}

int main(int argc, char ** argv)
{
	int cases;
	std::cin >> cases;

	for (int c = 0; c < cases; c++)
	{
		long min, max;
		std::cin >> min >> max;

		min = std::ceil( std::sqrt(min));
		max = std::floor(std::sqrt(max));

		long v = min;
		if (!is_palindrome(v))
			v = next_palindrome(v);

		int n = 0;
		for (; v <= max; v = next_palindrome(v))
		{
			if (is_palindrome(v*v))
				n++;
			//std::cout << v << ' ' << v*v << ' ' << n << std::endl;
		}

		std::cout << "Case #" << c+1 << ": " << n << std::endl;
	}

	return 0;
}