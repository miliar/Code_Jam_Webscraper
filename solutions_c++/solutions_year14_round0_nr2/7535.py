#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

void Init(void)
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
}


int main(void)
{
	Init();
	int i,cases,tt;
	double C,F,X;
	scanf("%d",&cases);
	for(tt=1; tt<=cases; ++tt)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		double time = 0.0;
		double rate = 2.0;
		while(true)
		{
			double t1 = X/rate;
			double t2 = C/rate + X/(rate+F);
			if(t1 < t2)
			{
				time += t1;
				break;
			}
			else
			{
				time += C/rate;
				rate += F;
			}
		}
		printf("Case #%d: %.7lf\n", tt, time);
	}
	return 0;
}