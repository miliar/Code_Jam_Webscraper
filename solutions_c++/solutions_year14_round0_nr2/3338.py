#include <iostream>
#include <cstdio>
using namespace std;
double DP(double Farm$,double Extra,double Win)
{
	double Time=0,Cps=2,Cookie=0;
	while(1)
	{
		Time+=Farm$/Cps;
		Cookie+=Farm$;
		if( ((Win-Cookie)/Cps) > ((Win)/(Cps+Extra)) )
			Cookie=0,Cps+=Extra;
		else
			return Time+((Win-Cookie)/Cps);
	}
}
int main()
{
	freopen("Bin.in","r",stdin);
	freopen("Bout.txt","w",stdout);
	int T;
	double C,F,X;
	cin>>T;
	for(int tms=1;tms<=T;tms++)
	{
		cin>>C>>F>>X;
		printf("Case #%d: %.7lf\n",tms,DP(C,F,X));
	}
	return 0;
}
