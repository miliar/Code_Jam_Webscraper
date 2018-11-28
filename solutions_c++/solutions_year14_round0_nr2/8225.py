#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int T,i;
	double C,F,X,k,time,temp,count;	
	scanf("%d", &T);
	for(i=1;i<=T;i++)
	{
		k=2;count=0;
		scanf("%lf%lf%lf",&C,&F,&X);
		time=X/k;
		while(1)
		{
			count+=C/k;
			k+=F;
			temp=count+X/k;
			if(temp<time)
				time=temp;
			else
				break;
		}
		printf("Case #%d: %.7lf\n",i,time);
	}
	return 0;
}