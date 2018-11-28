#include <stdio.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	int t;
	double c,f,x;
	scanf("%d",&t);
	for(int h=0;h<t;h++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);double rate=2.0;double time=0.0;
		while(c/rate+x/(rate+f)<x/rate)
		{
			time+=c/rate;
			rate+=f;
		}
		time+=x/rate;
		printf("Case #%d: %lf\n",(h+1),time);
	}
	return 0;
}
