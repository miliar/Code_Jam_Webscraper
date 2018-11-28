//COOKIE CLIKER

#include<cstdio>
#include<iostream>

int main()
{
	int t;
	scanf("%d",&t);
	int i=1;
	while(t--)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		 double num1,num2,inc=2.0,onefarm,sum=0.0,nextfarm;
		 while(1)
		 {
				onefarm=c/inc;
				nextfarm=onefarm+(c/(inc+f))*(x/c);
			//	printf("onefarm   %f   next   %f\n",onefarm,nextfarm);
				if(onefarm*(x/c)>nextfarm)
				{
					inc=inc+f;
					sum=sum+onefarm;
		//			printf("sum  is   %f  %f\n",sum,inc);
				}
				else
				break;
		}sum+=(c/(inc))*(x/c);
	//	printf("last  %f\n",(c/(inc))*4);
			printf("Case #%d: %.7f\n",i,sum);
			i++;
	}
  //system("pause");
	return 0;
}
				
