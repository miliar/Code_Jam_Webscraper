#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double time = 0;
		double rate = 2;
		double best = x / 2;
		while (true)
		{
			time += c / rate;
			rate += f;
			double newBest = time + x / rate;
			if (newBest < best)
				best = newBest;
			else
				break;
		}
		printf("Case #%d: %.7f\n", i, best);
	}
	return 0;
}