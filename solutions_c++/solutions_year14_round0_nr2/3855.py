#include "stdio.h"
#include "stdlib.h"

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d",&t);
	for (int cas = 1; cas <= t; ++cas)
	{
		printf("Case #%d: ",cas );
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		// printf("%0.7lf %0.7lf %0.7lf\n",c,f,x );
		double currRate=2.0,currCookie=0;
		double tim=0.0;
		int count=0;
		//printf("%0.7lf",tim );
		while(((x-c)/(currRate))>(x/((currRate+f))))
		{
				 //printf("%f %f\n",(x-c)/(currRate), (x/((currRate+f))));
				tim+=c/(currRate);
		//		printf("%.7lf %.7lf\n",c/(currRate),tim );
				currRate+=f;
				count++;
				//if(count>20) break;
			
		}
		tim+=(x)/(currRate);
		//printf("%0.7lf\n",x/currRate	 );
		printf("%0.7lf\n",tim );
	}
}