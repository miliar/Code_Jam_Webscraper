#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

FILE *in, *out;
int time;
double c, f, x;
double v,max;
double cost;
int solve()
{
	v = 2;
	cost = 0;
	max = (x / c - 1)*f;
	while (v < max)
	{
		cost += c / v;
		v += f;
	}
	cost += x / v;
	return 0;
}
int print(int i)
{
	fprintf(out,"Case #%d: ",i);
	fprintf(out,"%.7lf\n",cost);
	return 0;
}
int main()
{
	in = fopen("B-large.in","r");
	out = fopen("result.txt","w");
	int i;
	fscanf(in,"%d",&time);
	for (i = 1; i <= time; i++)
	{
		fscanf(in,"%lf%lf%lf",&c,&f,&x);
		solve();
		print(i);
	}
	return 0;
}