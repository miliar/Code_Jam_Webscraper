#include<stdio.h>
#include<iostream>
#include<iomanip>
using namespace std;
main()
{
	int test,n;
	scanf("%d",&n);
	for(test=1;test<=n;test++)
	{
		double c,f,x,sum=0,t=0,r=2;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(1)
		{
			if(((c/r)+(x/(r+f)))<(x/r))
			{
				sum=sum+c/r;
				r=r+f;
			}
			else
			{
				sum=sum+x/r;
				cout<<"Case #"<<test<<": ";
				cout<<fixed<<setprecision(7)<<sum<<endl;
				break;
			}
		}
		
	}
}
