/*
	b.cpp
	Christopher Cabrera
	Cookie Clicker Alpha - Code Jam 2014 Qualification
*/

#include <iomanip>
#include <iostream>

int main()
{
	int T;
	double C, F, X;

	std::cin >> T;

	for (int t = 0; t < T; ++t)
	{
		std::cin >> C >> F >> X;


		double time_spent = 0.0F, rate = 2.0F;

		// get current cost to fill at current rate
		double cur_time = X / rate + time_spent;

		// get cost to fill after upgrading factory
		double next_time = X / (rate + F) + (time_spent + (C / rate));

		while (next_time < cur_time)
		{
			// upgrade factory
			cur_time = next_time;

			time_spent += (C / rate);
			rate += F;

			next_time =  X / (rate + F) + (time_spent + (C / rate));
		}

		std::cout << "Case #" << t + 1 << ": " 
				  << std::fixed << std::setprecision(7) << cur_time << '\n';
	}

	return 0;
}