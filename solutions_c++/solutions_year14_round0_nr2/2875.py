#include<iostream>
#include<cstdio>



double func(double C, double F, double X, double rate)
{
	double current = X/rate;
	double next =  C/rate;
	rate += F;
	double temp = X/rate;
	next += temp;
	
	while(next < current)
	{
		current = next;
		next -= temp;
		next += C/rate;
		rate += F;
		temp = X/rate;
		next += temp;	
	}
	
	return current;
}


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int t, counter = 1;
	double C, F, X, rate = 2.0;
	
	scanf("%d", &t);
	
	while(t--)
	{
		
		scanf("%lf%lf%lf", &C, &F, &X);
		
		double res = func(C, F, X, rate);
		
		printf("Case #%d: ", counter++);
		printf("%.7lf\n", res);			
	}
	
	
	return 0;
}
