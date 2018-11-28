#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	double C, F, X;
	scanf("%d", &T);
	for(int Case = 1; Case <= T; Case++)
	{
		scanf("%lf%lf%lf", &C, &F, &X);
		double time = 0.0;
		double rate = 2.0;
		while(X / rate > C / rate + X / (rate + F))
		{
			time += C / rate;
			rate += F;
		}
		printf("Case #%d: %.7lf\n", Case, time + X / rate);
	}
	return 0;
}
