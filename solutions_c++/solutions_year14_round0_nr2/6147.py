#include <iostream>
#include <stdio.h>
using namespace std;
int main() {
	int tc;
	scanf("%d",&tc);
	for(int i=1;i<=tc;i++)
	{
		double ans,c,x,f,currtime=0.0,temp=0.0;
		double factor=2.0;
		cin>>c>>f>>x;
		currtime=x/factor;
		
		while(true)
		{
			//printf("%lf %lf %lf ",currtime,temp,factor);
			temp=temp+(c/factor);
			factor=factor+f;
			double now=temp+(x/(factor));
			//printf("%lf\n",now);
			if(now>currtime)
				break;
			currtime=now;	
		}
		printf("Case #%d: %.7lf\n",i,currtime);
	}
	return 0;
}
