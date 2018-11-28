#include<iostream>

using namespace std;

int main()
{
	long int n;
	long double sum,T_sum,time;
	double C,F,X;
	double time_cookie;
	FILE *fp1,*fp2;

	fp1 = fopen("B-large.in","r");
	fp2 = fopen("B-large.out","w+");

	fscanf(fp1,"%ld",&n);

	for(int i=1;i<=n;i++)
	{
		T_sum = time = 0;
		sum = 200000000;
		time_cookie = 2;
		fscanf(fp1,"%lf %lf %lf",&C,&F,&X);
		while(1)
		{
			T_sum = (X/time_cookie) +time;
			time += (C/time_cookie);
			if( sum >= T_sum )
				sum = T_sum;
			else break;
			time_cookie += F;
		}
		fprintf(fp2,"Case #%d: %.7llf\n",i,sum);
	}

	fclose(fp1);
	fclose(fp2);

	return 0;
}