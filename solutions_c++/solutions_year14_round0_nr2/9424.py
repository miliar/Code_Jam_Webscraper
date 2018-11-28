#include <cstdio>

using namespace std;


double get_time(double c, double f, double x, int machine)
{
	double times = 0;
	double power = 2;
	while(machine--)
	{
		times += c/power;
		power += f;
	}
	return times + (x/power);
}

int main()
{
	int testcase;
	scanf("%d",&testcase);

	double c,f,x;
	double current_time;
	double prev_time;
	int machine;

	for(int testcase_run=1; testcase_run<=testcase; testcase_run++)
	{
		scanf("%lf %lf %lf",&c ,&f ,&x);
		machine = 0;
		prev_time = get_time(c,f,x,machine++);
		current_time = get_time(c,f,x,machine++);
		while(current_time<prev_time)
		{
			prev_time = current_time;
			current_time = get_time(c,f,x,machine++);
		}
		printf("Case #%d: %.7lf\n", testcase_run, prev_time );
	}
	return 0;
}