#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
#include<iomanip>
using namespace std;

int main(void)
{
	freopen("temp.in", "r", stdin);
	freopen("temp.out", "w", stdout);
	int T;
	double C, F, X;

	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cin >> C >> F >> X;
		double min_time = X / 2;
		int farm_num = 0;
		double temp_time, current_speed;
		while (true)
		{
			++farm_num;
			temp_time = 0;
			current_speed = 2.0;
			for (int j = 0; j < farm_num; ++j)
			{
				temp_time += C / current_speed;
				current_speed += F;
			}
			temp_time += (X / current_speed);
			if (temp_time < min_time)
			{
				min_time = temp_time;
			}
			else
			{
				break;
			}
		}

		cout << "Case #" << i << ": " << fixed<<setprecision(7)<<min_time << endl;
	}
	return 0;
}