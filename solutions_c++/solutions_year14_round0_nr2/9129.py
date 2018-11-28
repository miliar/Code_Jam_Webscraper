#include<stdio.h>
int main()
{
	FILE *op = fopen("Output4.TXT", "w");
	FILE *ip = fopen("B-large.in", "r");
	int test_case=1, T;
	double C, F, X, time1, time2, total_time, adder;
	fscanf(ip, "%d", &T);
	while(test_case<=T)
	{
		fscanf(ip, "%lf %lf %lf", &C, &F, &X);
		total_time=0.0;
		adder=2.0;
		while(1)
		{
			time1 = X/adder;
			time2 = C/adder + X/(F+adder);
			if(time1>=time2)
			{
				total_time = total_time + C/adder;
				adder = adder + F; 
			}
			else
			{
				total_time = total_time + X/adder;
				break; 
			}
		}

		fprintf(op,"Case #%d: %lf\n",test_case, total_time);
		test_case++;
	}
	fclose(ip);
	fclose(op);
	return 0;
}
