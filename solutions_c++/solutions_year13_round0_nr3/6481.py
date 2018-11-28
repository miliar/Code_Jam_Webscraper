#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>

bool is_palindrome(int64_t n)
{
	std::stringstream ss;
	ss << n;
	std::string str = ss.str();
	return str == std::string( str.rbegin(), str.rend() );
}

int main(int argc, char **argv)
{
	std::ifstream input(argv[1]);

	int T;
	input >> T;

	uint64_t A, B, sqrtA, sqrtB;
	for (int i = 1; i <= T; i++)
	{
		int64_t res = 0;
		input >> A >> B;
		sqrtA = sqrt(A);
		sqrtB =  sqrt(B);

		for (int64_t n = ceil(sqrt(A)); n <= sqrt(B); n++)
		{
			if ( is_palindrome(n) && is_palindrome(n * n) )
			{
				//std::cerr << n << std::endl;
				res++;
			}
		}
		std::cout << "Case #" << i << ": " << res << std::endl;
	}

	input.close();
}
