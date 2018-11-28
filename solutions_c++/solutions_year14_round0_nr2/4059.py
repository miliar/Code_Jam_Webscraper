#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
using namespace std;
double 

c,f,x,ans1,ans2,r=2.0,k3=0;
double calc()
{
    long double k1=0;
	k3+=c/r;
	r+=f;
	k1=k3+x/r;
	return k1;
}
int 

main()
{
int t,T;
scanf("%d",&t);
T=t;
	while(t--)
	{
	scanf("%lf %lf %lf",&c,&f,&x);
	k3=0;r=2;ans1=1;ans2=0;
		

double ans3=x/r;
		ans1=calc();
		if(ans3>ans1)
		{
		while(1)
		{
	

		
			ans2=calc();
			if(ans1>ans2)
				ans1=ans2;
	

		else
				break;
		}
		}
		else
			

ans1=ans3;
			printf("%s%d%s%.10g\n","Case #",T-t,": ",ans1);
	}
}
