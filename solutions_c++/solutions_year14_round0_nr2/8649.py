#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
const int N = 10+10;
double C,F,X;
int main()
{
	int T;
	scanf("%d", &T);
	int p=1;//case #
	
	while(T--)
	{
		double rate = 2.0;
		double cur_tottime=0.0;
		double ansTime = 0.0;
		scanf("%lf%lf%lf",&C,&F,&X);
		double t1 = X/rate;
		double t2 = C/rate + X/(rate+F);
		while(t1 > t2)
		{
			cur_tottime += C/rate;
			rate += F;
			t1 = X/rate;
			t2 = C/rate + X/(rate+F);
		}
		// t1 = X/rate;
		cur_tottime += t1;
		printf("Case #%d: %.7lf\n",p++,cur_tottime);

	}
	return 0;
}
