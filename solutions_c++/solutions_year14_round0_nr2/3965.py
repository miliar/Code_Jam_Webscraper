#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int t;
	double c,f,x,r;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>c>>f>>x;
		double r=2.0,sum=0.0;
		while(1)
		{
			double v1=c/r,v2=x/r,v3=x/(r+f);
			if(v1+v3>v2)
			{
				sum+=v2;
				break;
			}
			else
			{
				sum+=v1;
				r+=f;
			}
		}
		printf("Case #%d: %.7f\n",k,sum);
	}
}