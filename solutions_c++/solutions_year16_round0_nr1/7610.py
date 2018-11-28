#include <iostream>
#include <vector>

int main()
{
	int testCases;
	std::cin >> testCases;

	std::vector<int> tests;
	for (int i = 0; i < testCases; i++)
	{
		int n;
		std::cin >> n;

		tests.push_back(n);
	}

	for (int i = 0; i < testCases; i++)
	{
		int n = tests[i];

		bool seenDigits[10];
		for (int i = 0; i < 10; i++)
			seenDigits[i] = false;

		int countSeenDigits = 0;

		bool fallsAsleep = false;
		long long current = n;
		while (current > 0 && countSeenDigits < 10)
		{
			int c = current;
			while (c > 0)
			{
				int num = c % 10;
				c = c / 10;

				if (seenDigits[num] == false)
				{
					countSeenDigits++;
					seenDigits[num] = true;
				}
			}

			if (countSeenDigits == 10)
				fallsAsleep = true;
			else
				current += n;
		}

		if (!fallsAsleep)
			std::cout << "Case #" << i + 1 << ": INSOMNIA" << std::endl;
		else
			std::cout << "Case #" << i + 1 << ": " << current << std::endl;
	}
}