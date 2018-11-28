#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,count=0;
	double c,f,x,time,rate=2;
	cin>>t;
	while(t>0)
	{ count++;
		cin>>c>>f>>x;
		rate=2;
		time=0;
		while(true)
		{
			if(x/rate>(c/rate+x/(rate+f)))
			{
				
				time=time+c/rate;
				rate=rate+f;
				
			}
			else
			break;
		}
		time=time+x/rate;
		printf("case #%d: %.7f\n",count,time);  //plaease check d code and convert it into euivalent printf with 7 decimal precision...
		t--;
	}
}
