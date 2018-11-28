#include <stdio.h>
//#include <algorithm>

//void sort( int *seq, int size);
double Time(double time, double gain, double Cprice);

int main()
{
	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("output.txt", "w");
	double Cprice, Fextra,
		Xneed, gain = 2.0;
	int t;
	double curTime;
	fscanf(in, "%d", &t);
	for(int i = 0; i < t; i++)
	{
		fscanf(in,"%lf %lf %lf", &Cprice, &Fextra, &Xneed);
		gain = 2;
		double T_time = Xneed / gain, time;
		//gain += Fextra;
		time = Time(0, 2, Cprice);
		gain += Fextra;
		curTime = time + Xneed / gain;
		while(T_time > curTime)
		{
			time = Time(time, gain, Cprice);
			gain += Fextra;
			T_time = curTime;
			curTime = time + Xneed / gain;
		}
		fprintf(out,"Case #%d: %lf\n", i + 1, T_time);
	}
	return 0;
}

double Time(double time, double gain, double Cprice)
{
	return time + Cprice / gain;
}