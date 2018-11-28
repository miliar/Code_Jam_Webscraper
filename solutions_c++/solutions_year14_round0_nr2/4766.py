#include <iostream>
#include <stdio.h>
#include <set>
#include <string.h>
#include <algorithm>
using namespace std;
set<int> g;
const double eps=1e-10;
double c,ad,aim;
double cal(int ti)
{
	double ba=2;
	double ret=0;
	while(ti--)
	{
		ret+=c/ba;
		ba+=ad;
	}
	return ret+aim/ba;
}
int main()
{
	int ca;
	cin>>ca;
	//cout<<c<<endl;
	int cc=1;
	while(ca--)
	{
		printf("Case #%d: ",cc++);
		
		scanf("%lf%lf%lf",&c,&ad,&aim);
		int s=0,t=1e5;
		
		double ans;
		while(s<=t)
		{
		
			int l=(s*2+t)/3;
			int r=(s+2*t)/3;
			
			if(cal(l)>cal(r)) 
			{
				s=l+1;
				ans=cal(r);	
			}
			else 
			{
				t=r-1;
				ans=cal(l);
			}
		}
		printf("%.7f\n",ans);
		
	}
	return 0;
}