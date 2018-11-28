#include<stdio.h>
#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int t,T;
	scanf("%d",&t);
	T=t;
	double c,f,x,time,init;
	while(t--)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		long long int n=x;
		double arr[n],ti[n];
		time=x/2.0;
		init=2.0;
		for(int i=0;i<x;i++)
		{
			
		
			if(i==0)
				arr[i]=0;
			else
			{
				arr[i]=arr[i-1]+c/init;
				init+=f;
			}
			ti[i]=x/init;
			if(time>ti[i]+arr[i])
				time=ti[i]+arr[i];
		}
		printf("Case #%d: ",T-t);
		cout<<fixed<<setprecision(7)<<time<<endl;
		/*delete []arr;
		delete []ti*/
		
	}
	return 0;
}
