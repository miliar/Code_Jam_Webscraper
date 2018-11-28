//============================================================================
// Name        : task4.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>

void pv(std::vector<int>& v)
{
#if 0
	for (std::size_t n = 0; n < v.size(); ++n)
		std::cout << v[n] << " ";
	std::cout << std::endl;
#endif
}

int main()
{
	std::fstream f;
	f.open("3.in");

	int T;
	f >> T;

	for (int t = 0; t < T; ++t)
	{
		int N, M;
		f >> N >> M;

		std::vector<int> mm(N * M);
		for (int n = 0; n < N; ++n)
		{
			for (int m = 0; m < M; ++m)
			{
				f >> mm[n * M + m];
			}
		}
		pv(mm);

		std::vector<int> canv(N, -1);
		std::vector<int> canh(M, -1);

		for (int n = 0; n < N; ++n)
		{
			int v = mm[n * M];
			bool ok = true;
			for (int m = 1; m < M; ++m)
			{
				if (mm[n * M + m] > v)
				{
					ok = false;
					break;
				}
			}
			if (ok)
				canv[n] = v;
		}
		pv(canv);

		for (int m = 0; m < M; ++m)
		{
			int h = mm[m];
			bool ok = true;
			for (int n = 1; n < N; ++n)
			{
				if (mm[n * M + m] > h)
				{
					ok = false;
					break;
				}
			}
			if (ok)
				canh[m] = h;
		}
		pv(canh);

		std::vector<int> check(mm.size(), 2);
		for (int n = 0; n < N; ++n)
		{
			int v = canv[n];
			if (v > 0)
			{
				for (int m = 0; m < M; ++m)
				{
					if (check[n * M + m] > v)
						check[n * M + m] = v;
				}
			}
		}
		for (int m = 0; m < M; ++m)
		{
			int h = canh[m];
			if (h > 0)
			{
				for (int n = 0; n < N; ++n)
				{
					if (check[n * M + m] > h)
						check[n * M + m] = h;
				}
			}
		}
		pv(check);

		bool ok = true;
		for (std::size_t k = 0; k < check.size(); ++k)
		{
			if (mm[k] != check[k])
			{
				ok = false;
				break;
			}
		}

		if (ok)
			std::cout << "Case #" << t + 1 << ": YES" << std::endl;
		else
			std::cout << "Case #" << t + 1 << ": NO" << std::endl;
	}

	return 0;
}
