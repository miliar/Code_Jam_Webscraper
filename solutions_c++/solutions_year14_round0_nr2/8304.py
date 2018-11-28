#include <iostream>
#include <algorithm>
#include<cstdio>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	double c,f,x,time,add;
	for(int ind=1;ind<=t;ind++)
	{
		time=0,add=2;
		scanf("%lf %lf %lf",&c,&f,&x);
		while((c/add)+x/(add+f)<x/add)
		{
			time+=c/add;
			add+=f;
		}
		time+=x/add;
		printf("Case #%d:%.7f\n",ind,time);
	}
	return 0;
}
