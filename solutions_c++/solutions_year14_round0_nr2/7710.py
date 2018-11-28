#include <cstdio>
#include <iostream>

using namespace std;

double calc_time(double farm, double speed, double goal)
{
	double current_speed = 2;
	double time = 0;
	while(true)
	{
		double time_d = goal / current_speed;
		double time_u = farm / current_speed;
		time_u += goal / (current_speed + speed);
		if(time_d < time_u) return (time + time_d);
		else
		{
			time += farm / current_speed;
			current_speed += speed;
		}
	}
}

int main()
{
	//freopen("..\\Debug\\in.txt", "r", stdin);
	//B-small-attempt0.in
	freopen("..\\Debug\\B-large.in", "r", stdin);freopen("..\\Debug\\B-large.out", "w", stdout);
	int num;
	double farm, speed, goal, time;
	cin >> num;
	for(int i=0; i<num; i++)
	{
		cin >> farm >> speed >> goal;
		time = calc_time(farm, speed, goal);
		printf("Case #%d: %.7lf\n", i+1, time);
	}
	return 0;
}