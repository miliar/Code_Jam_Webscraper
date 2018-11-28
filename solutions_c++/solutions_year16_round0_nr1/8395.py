#include <iostream>

bool have_seen_all(bool digits[10])
{
	for (int i = 0 ; i < 10 ; ++i)
	{
		if (!digits[i])
		{
			return false;
		}
	}
	return true;
}

bool mark_digits(int N, bool digits[10])
{
	while (N > 0)
	{
		digits[N % 10] = true;
		N /= 10;
	}
	return have_seen_all(digits);
}
		

int main() {
	int testCases = 0;
 
	std::cin >> testCases;
	
	for (int testCase = 0 ; testCase < testCases ; ++testCase)
	{
		int N = 0;
		std::cin >> N;
		bool digits[10];
		for (int i = 0 ; i < 10 ; ++i)
		{
			digits[i] = false;
		}
		if (N == 0)
		{
			std::cout << "Case #" << testCase + 1 << ": INSOMNIA" << std::endl;
		}
		else
		{
			int current = N;
			bool found = false;
			for (int i = 2 ; N * i > N ; ++i)
			{
				if (mark_digits(current, digits))
				{
					std::cout << "Case #" << testCase + 1 << ": " << current << std::endl;
					found = true;
					break;
				}
				current = N * i;
			}
			if (!found)
			{
				std::cout << "Case #" << testCase + 1 << ": INSOMNIA" << std::endl;
				break;
			}
		}
	}
 
	return 0;
}
