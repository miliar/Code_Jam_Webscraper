#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<climits>
#include<cstring>
#include<algorithm>
#include<stack>
#include<vector>
#include <fstream>

using namespace std;

double strategy(double C, double F, double X)
{
	double curr_time, next_time, total_time = 0.0, rate = 2.0;

	while(1)
	{
		curr_time = total_time + (X/rate);

		double buy_time = C/rate;
		rate = rate + F;
		next_time = total_time + buy_time + (X/rate);

		if(curr_time < next_time)
			return curr_time;

		total_time += buy_time;
	}
}

int main()
{
	double C, F, X;

	int num, count = 1;

    ifstream infile("B-large.in");
    infile >> num;

	FILE *f = fopen("output.txt", "w");

	while(num--)
	{
		infile >> C >> F >> X;
		double time = strategy(C, F, X);
		fprintf(f, "Case #%d: %.7lf\n", count, time);
		count = count + 1;
	}

	fclose(f);
	infile.close();
}
