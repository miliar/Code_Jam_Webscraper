#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
using namespace std;

int main()
{
	cout << fixed << setprecision(7);
	unsigned N = 0;
	double C = 0.0, F = 0.0, X = 0.0, seconds = 0.0,
	time_elasped = 0.0, cookies = 0, rate = 0, new_rate = 0,
	new_potential = 0.0, cur_potential = 0.0;
	bool dont_buy = false;
	cin >> N;
	for(auto i = 0; i < N; ++i)
	{
		rate = 2.0;
		time_elasped = 0.0;
		dont_buy = false;
		cin >> C >> F >> X;
		while(true)
		{
			if(dont_buy)
			{
				time_elasped += X / rate;
				break;
			}
			else
			{
				new_rate = rate + F;
				new_potential = (X / new_rate) + (C / rate);
				cur_potential = (X / rate);
				if(cur_potential <= new_potential)
				{
					dont_buy = true;
				}
				else
				{
					time_elasped += (C / rate);
					rate = new_rate;
				}

			}
		}
		cout << "Case #" << i + 1 << ": " << time_elasped << endl;
	}
	return 0;
}
