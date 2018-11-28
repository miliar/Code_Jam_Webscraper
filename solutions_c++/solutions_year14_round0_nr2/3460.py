#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
using namespace std;

long double time_cache, wtime, time_to_bye, time_to_end;

void prog(long double cost, long double fps, long double win, long double cps)
{
	long double time = 0 ;
	time_cache = win / cps;
	for (long double i = 1; i <= win; i += 1)
	{
		time_to_bye = cost / cps;
		cps += fps;
		time_to_end = win / cps;
		time = time + time_to_bye;
		if (time_cache > time + time_to_end)
		{
			time_cache = time + time_to_end;
		}
		else
			break;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long double cost, fps, win, time, cps = 2;
	int t;
	cin >> t;

	for (int k = 1; k <= t; k++)
	{
		cout << "Case #" << k << ": ";
		cps = 2;
		cin >> cost >> fps >> win;
		prog(cost, fps, win, cps);
		cout.precision(7);
		cout << fixed << time_cache << endl;
	}
	
	
	return 0;
}

