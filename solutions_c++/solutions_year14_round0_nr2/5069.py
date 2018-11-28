#include <iostream>
#include<cstdio>
using namespace std;
int main()
{	
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{		
		double c,f,x;
		double time=0.0000;
		cin>>c>>f>>x;
		double lhs=(c/2.0)+(x/(2.0+f));
		double rhs=x/2.0;
		int i=0;
		//cout<<lhs<<"\t"<<rhs<<endl;
		while(lhs<rhs)
		{
			time = time + c/(2.0+i*f);i++;
			//cout<<time<<"\t"<<lhs<<"\t"<<rhs<<endl;
			lhs = c/(2.0+i*f)+x/(2.0+(i+1)*f);
			rhs = x/(2.0+i*f);
		}
		//cout<<"this is after loop "<<x/(2.0+(i+1)*f) <<endl;
		time = time + x/(2.0+(i)*f);
		cout<<"Case #"<<k+1<<": ";
		printf("%.7f\n",time);
	}
}

