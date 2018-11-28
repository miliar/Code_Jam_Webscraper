#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double best_time = X / 2.0;
		int farms_number = 0;
		while (1)
		{
			farms_number++;
			double rate = 2.0;
			double current_time = 0.0;
			for (int j = 0; j < farms_number; j++)
			{
				current_time += C / rate;
				rate += F;
			}
			current_time += X / rate;
			if (current_time < best_time)
				best_time = current_time;
			else
				break;
		}
		cout << fixed << setprecision(7) << "Case #" << i << ": " << best_time << endl;
	}
	return 0;
}