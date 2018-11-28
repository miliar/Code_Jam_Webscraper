#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <stdio.h>
#include <iomanip>

using namespace std;

const double epsillon = 1e-6;

int main()
{
	cout.precision(7);
	long long t,i=0;
	scanf("%lld",&t);
	//cin>>t;
	for(i=1;i<=t;i++)
	{
		double C,F,X,res=0;
		scanf("%lf %lf %lf",&C,&F,&X);
		//cin>>C>>F>>X;
		double rate=2.0;
		double currentRate=rate;
		double timeToTargetcur = X/currentRate ;
		double timeToFarm = (C/currentRate);
		double timeToTargetfarm = timeToFarm+(X/(currentRate+F));
		double diff = timeToTargetcur - timeToTargetfarm;
		while(diff > 0)
		{
			res+=timeToFarm;
			currentRate+=F;
			timeToTargetcur = X/currentRate ;
			timeToFarm = (C/currentRate);
			timeToTargetfarm = timeToFarm+(X/(currentRate+F));
			diff = timeToTargetcur - timeToTargetfarm;
		}
		res+=timeToTargetcur;
		printf("Case #%lld: %.7lf\n",i,res);
		//cout<<"Case #"<<i<<": "<<res<<endl;
	}
}
