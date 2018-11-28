#include <iostream>

double TimeToAquire(double per_sec, double cost)
{
	return cost / per_sec;
}

void DoTest()
{
	double c, f, x;
	double cookies_per_sec = 2;
	std::cin >> c >> f >> x;
	double time = 0;
	while (true)
	{
		double factory_time = TimeToAquire(cookies_per_sec, c);
		double new_x_time = TimeToAquire(cookies_per_sec + f, x);
		double x_time = TimeToAquire(cookies_per_sec, x);
		if (x_time <= factory_time + new_x_time)
		{
			std::cout << std::fixed << time + x_time << '\n';
			return;
		} else
		{
			cookies_per_sec += f;
			time += factory_time;
		}
	}
}

int main()
{
	int t;
	std::cin >> t;
	std::cout.precision(7);
	for (int i = 1; i <= t; i++)
	{
		std::cout << "Case #" << i << ": ";
		DoTest();
	}
}
