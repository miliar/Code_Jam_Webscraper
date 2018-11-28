#include <cstdio>

double memo[9999999];
double get_machine_time(double c, double f, int machine)
{
	if(memo[machine]>0 or machine==0) return memo[machine];
	return memo[machine] = get_machine_time(c,f,machine-1)+c/( ((machine-1)*f)+2 );
}
double get_time(double c, double f, double x, int machine)
{
	double re = get_machine_time(c,f,machine);
	re += x/(2+(machine*f));
	return re;
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
		for (int i = 0; i <= machine; ++i)
		{
			memo[i] = 0;
		}
	}
	return 0;
}