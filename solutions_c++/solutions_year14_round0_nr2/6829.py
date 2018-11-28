#include <stdio.h>
#include <stdlib.h>

double calc_best_strategy(double c, double f, double x,int case_num)
{

	double time_took = x/2.0;
	double curr_time_took = 0;
	int fix_time_flag = 0;
	int num_farms = 1;
	int i;
	double curr_cookie_per_second;
	do
	{
		curr_cookie_per_second = 2;
		fix_time_flag = 0;
		curr_time_took = 0;

		for (i = 0; i < num_farms; i++)
		{
			curr_time_took += c / curr_cookie_per_second;
			curr_cookie_per_second += f;

		}

		curr_time_took += x / curr_cookie_per_second;


		if (curr_time_took < time_took)
		{
			time_took = curr_time_took;
			fix_time_flag = 1;
		}

		num_farms++;
		//printf("it took %lf time\n", curr_time_took);
	} while (fix_time_flag == 1);

	//printf("it'll take %lf time\n", time_took);
	printf("Case #%d: %lf\n", case_num, time_took);
	return time_took;
}

int main(void)
{
	FILE * fd = fopen("D:\\B-large.in", "r");
	if (fd == NULL)
	{
		perror("fopen");
		return 1;
	}

	int num_cases, i;
	double c, f, x;

	fscanf(fd,"%d", &num_cases);
	//printf("num_cases is : %d \n", num_cases);
	
	for (i = 0; i < num_cases; i++)
	{
		fscanf(fd, "%lf %lf %lf", &c, &f, &x);
		//printf("c,f,x : %lf,%lf,%lf \n", c, f, x);

		calc_best_strategy(c, f, x,i+1);

	}

	return 0;
}