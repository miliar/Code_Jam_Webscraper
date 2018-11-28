#include <iostream>

int main()
{
	int T;
	std::cin >> T;
	double C, F, X;
	double t[100000];
	for(int round = 1; round <= T; ++round)
	{
		std::cin >> C >> F >> X;

		for(int fac = 0; fac < X / C; ++fac)
		{
			if(fac == 0)
			{
				t[0] = X / 2.0;
			}
			else
			{
				t[fac] = 0;
				for(int i = 0; i < fac; ++i)
				{
					t[fac] += C / (2 + i * F);
				}
				t[fac] += X / (2 + fac * F);
			}
		}

		double min = t[0];
		for(int i = 1; i < X / C; ++i)
		{
			if(t[i] < min)
			{
				min = t[i];
			}
		}

		std::cout.precision(7);
		std::cout.setf(std::ios::fixed);
		std::cout << "Case #" << round << ": " << min << std::endl;
	}
}
