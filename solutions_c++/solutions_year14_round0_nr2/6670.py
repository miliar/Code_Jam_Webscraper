#include <iostream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		double C,F,X,rate = 2.0, cur = 0, time = 0, nextFarm = 0;
		cin>>C>>F>>X;


		if (C >= X)
		{
			printf("Case #%d: %.7f\n", t, X/rate);
			continue;
		}

		nextFarm = (C-cur)/rate;
		time += nextFarm;
		cur = C;

		while((X-cur)/rate > (X-cur+C)/(rate+F))
		{
			cur -= C;
			rate += F;
			nextFarm = (C-cur)/rate;
			time += nextFarm;
			cur = C;
		}

		time += (X-cur) /rate;

		printf("Case #%d: %.7f\n", t, time);
	}
}