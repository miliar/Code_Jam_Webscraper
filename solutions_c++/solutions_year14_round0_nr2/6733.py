#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	int tc,q=0;
	double c,f,x,r,timex,timex1,timex2;
	scanf("%d",&tc);
	
	
	
	while(tc--)
	{
		q++;
		scanf("%lf%lf%lf",&c,&f,&x);
		r=2.0;
		timex=0.0;
		timex1=0.0;
		timex2=0.0;
		while(1)
		{
			timex1=timex+x/r;
			timex2=timex+(c/r)+(x/(f+r));
			if(timex1>timex2)
			{
			timex+=c/r;
			r+=f;
			}
			else
			{
			timex+=x/r;
			break;
			}
		}
		
		
		printf("Case #%d: %0.7lf\n",q,timex);
		
	}
	
	return 0;
}
