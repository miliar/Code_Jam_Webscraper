#include <iostream>
#include <bitset>

int main(int argc, char* argv[])
{
	int numCases;
	std::cin >> numCases;
	for (int i=0; i<numCases; i++)
	{
		long A, B, K;
		std::cin >> A >> B >> K;
		int cases = 0;

		for (int j=0; j<A; ++j)
		{
			for (int k=0; k<B; ++k)
			{
				int both = j&k;
				if (both < K)
					cases++;
			}
		}

		std::cout << "Case #" << (i+1) << ": " << cases << std::endl;
	}
	return 0;
}
