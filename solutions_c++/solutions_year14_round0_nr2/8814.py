#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int tt =1;tt<=t;tt++)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double n;
		n = x*f - 2.0*c;
		double temp = c*f;
		n = n / temp;
		int num = floor(n);
		if (num<0) num = 0;
		double sum = 0;
		//cout<<n <<"  "<<num<<endl;
		for(int i =0 ;i<=(num-1);i++)
		{
			sum = sum + (c/(2+i*f));
		}
		sum = sum + (x/(2+num*f));
		printf("Case #%d: %.7lf\n",tt,sum);
	}
}
