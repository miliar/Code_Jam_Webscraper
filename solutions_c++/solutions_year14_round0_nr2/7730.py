#include "iostream"
#include "vector"
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main ()
{
	freopen("input.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
	int T;
	cin >> T;

	for (int test = 0; test < T; ++test)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double timeBest = double(X) / 2.0;
		std::vector<double> summ(int(X) + 2);
		std::vector<double> sp(int(X) + 2);
		{
			double time = 0;
			double speed = 2;
			for (int j = 0; j < summ.size(); ++j)
			{
				summ[j] = time;
				sp[j] = speed;
				time += double(C) / speed;
				speed += F;
			}
		}
		for (int farm = 1; farm <= int(X) + 1; ++farm)
		{
			double time = summ[farm];
			time += double(X) / sp[farm];
			timeBest = std::min(time, timeBest);
		}
		printf("Case #%d: %.9f\n", test + 1, timeBest);
	}
	return 0;
}