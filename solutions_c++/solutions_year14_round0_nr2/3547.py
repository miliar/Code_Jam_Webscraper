#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	int i,t;
	double c,f,x,tm,fac,min;
	cin>>t;
	for(i=0;i<t;i++)
	{
		tm=0;
		fac=2;
		cin>>c>>f>>x;
		min=1000000;
		while(1)
		{
			if((tm+x/fac)<min)
				min=tm+x/fac;
			else
				break;
			tm=tm+c/fac;
			fac=fac+f;
		}
		printf("Case #%d: %.7lf\n",i+1,min);
	}
	return 0;
}
