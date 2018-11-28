#include<iostream>
#include<iomanip>
//#define epsilon 1e-6
using namespace std;

//bool precision()

int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("cookie.txt","w",stdout);
	int t;
	scanf("%d",&t);
	//cin>>t;
	for(int tt=1;tt<=t;++tt)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		//cin>>c>>f>>x;
		double cookies=0,rate=2,time=0;
		while(cookies<x)
		{
			if((x/rate)<((c/rate)+(x/(rate+f))))
			{
				cookies=x;
				time+=(x/rate);
			}
			else
			{
				time+=(c/rate);
				rate+=f;
			}
		}
		printf("Case #%d: ",tt);
		//cout<<"Case #"<<tt<<": ";
		printf("%.7lf\n",time);
	}
}
