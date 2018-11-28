#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main() 
{
	double c,f,x,currRate=2.0,currTime=0.0;
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		//cout<<"Case #"<<k<<endl;
		currRate=2.0;
		currTime=0.0;
		cin>>c>>f>>x;
		double tmp1=currTime+((x*1.0)/currRate);
		double tmp2=currTime+((c*1.0)/currRate)+((x*1.0)/(currRate+f));
		while(tmp1>tmp2)
		{
			
			currTime+=((c*1.0)/currRate);
			currRate+=f;
			tmp1=currTime+((x*1.0)/currRate);
			tmp2=currTime+((c*1.0)/currRate)+((x*1.0)/(currRate+f));
		}
		if(tmp1<tmp2)
		printf("Case #%d: %0.7lf \n",k,tmp1);
		else
		printf("Case #%d: %0.7lf \n",k,tmp2);
	}
	
	return 0;
}