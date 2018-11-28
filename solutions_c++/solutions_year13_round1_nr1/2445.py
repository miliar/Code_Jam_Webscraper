#include<math.h>
#include<Windows.h>
#include <iostream>
#include<conio.h>
void main()
{int T;
scanf("%d",&T);
	for(int counter=0;counter<T;counter++)
	{
	
	unsigned long long int t,r;
	scanf("%llu",&r);
	scanf("%llu",&t);
	
	double t2=sqrt((2*r-1)*(2*r-1)+8*t)/4;
	double t1= 0.25-((double)r/2);
	unsigned  long int result= t1+t2;
	unsigned long int temp=(sqrt(((2*r-1))*((2*r-1))+  t*8)/4)+(1-(2*r))/4;

	printf("Case #%d: %lu\n",counter+1, result);

	}


}
