#include <iostream>
#include <vector>
#include <iomanip>
#include <fstream>

int main()
{
	int T;
	std::cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		std::vector<double> pis;
		int K, N;
		std::cin >> N >> K;
		double maxP = 0.0;
		pis.resize(N);
		for (int j = 0; j < N; ++j)
			std::cin >> pis[j];
		for (uint32_t m = 0; m < (1<<N); ++m)
		{
			if (__builtin_popcount(m) != K)
				continue;
			std::vector<int> selected;
			for (int ji = 0; ji < N; ++ji)
				if ((1 << ji) & m)
					selected.push_back(ji);
			double p = 0.0;
			for (uint32_t m2 = 0; m2 < (1<<K); ++m2)
			{
				if (__builtin_popcount(m2) != K / 2)
					continue;
				double p1 = 1.0, p2 = 1.0;
				for (int ji = 0; ji < K; ++ji)
					if ((1 << ji) & m2)
					{
						p1 *= pis[selected[ji]];
						p2 *= (1.0 - pis[selected[ji]]);
					}
				    else
					{
						p2 *= pis[selected[ji]];
						p1 *= (1.0 - pis[selected[ji]]);
					}
				p += p1;
			}
			if (p > maxP)
				maxP = p;

		}
		std::cout << "Case #" << i << ": " << std::setprecision(19) << maxP << std::endl;
	}
	return 0;
}
