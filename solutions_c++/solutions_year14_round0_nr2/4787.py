#include<iostream>
#include<cstdlib>
#include<string.h>
#include<string>
#include<vector>
#include<math.h>
#include<ctype.h>
#include<iomanip>
using namespace std;
double C,F,X;
double tot1=0,tot2=0,inc;
double cookiet=0;
double caltot()
{
	double tot;
	while(1)
	{
		tot1=cookiet+(X/inc);
		tot2=cookiet+(C/inc)+(X/(inc+F));
//		cout<<tot1<<" "<<tot2<<endl;
		if(tot2<tot1)
		{
			cookiet=cookiet+(C/inc);
			inc+=F;
			return caltot();
		}
		else
		{
			return tot1;
		}
	}
}
int main()
{
	int T;
	cin>>T;
	for(int p=0;p<T;p++)
	{
		cookiet=0;
		inc=2;
		cin>>C>>F>>X;
//		cout<<C;
		cout<<"Case #"<<p+1<<": ";
		double ans=caltot();
		cout<<std::fixed;
		cout<<setprecision(7)<<ans<<endl;
	}
	return 0;
}
