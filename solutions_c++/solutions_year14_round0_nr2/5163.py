#include <stdio.h>
#include <iostream>
#include <cmath>
#include <fstream>
#include <iomanip>
#define lldd long long int
using namespace std;
int main()
{
int t;
scanf("%d",&t);
ofstream fout;
	fout.open("question1.txt");
for(int i=1;i<=t;i++)
{
	double c,f,x,ans=0;
	double rate=2;
	scanf("%lf%lf%lf",&c,&f,&x);
	while(1)
	{
		if(x<c)
		{
			ans=x/rate;
			break;
		}
		double time=c/rate;
		ans+=time;
		cout<<" "<<time<<" ";
		if(((x-c)/rate)<(x/(rate+f)))
		{
			time=(x-c)/rate;
			ans+=time;
			break;
		}
		else
		{
			rate+=f;
		}
	}
	fout<<fixed;
		fout<<setprecision(7)<<"Case #"<<i<<": "<<ans<<endl;
}
return 0;	
}