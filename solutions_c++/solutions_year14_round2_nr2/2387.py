/*
	b.cpp
	Christopher Cabrera
*/

#include <iomanip>
#include <iostream>

int main()
{
	int T;

	std::cin >> T;

	for (int t = 0; t < T; ++t)
	{
		long A, B, K;
		std::cin >> A;
		std::cin >> B;
		std::cin >> K;

		int pos = 0;
		for (int x = 0; x < A; ++x)
		{
			for (int y = 0; y < B; ++y)
			{
				if ((x&y) < K) ++pos;
			}
		}

		std::cout << "Case #" << t + 1 << ": " << pos << '\n';
	}

	return 0;
}