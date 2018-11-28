#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int T;
	double C, F, X;

	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cin >> C >> F >> X;
		
		double sum = 0;
		double nowpro = 2.0;
		while (1)
		{
			double notbuy = X / nowpro;
			double buyfarm = C / nowpro;
			double afterbuy = X / (nowpro + F);

			if (buyfarm + afterbuy < notbuy)
			{
				sum += buyfarm;
				nowpro += F;
			}
			else
			{
				sum += notbuy;
				break;
			}
		}
		
		printf("Case #%d: %.7lf\n", t, sum);
	}

	return 0;
}
