#include<bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int iter=1;iter<=T;iter++)
	{
		double C,F,X,res=0,rate;
		scanf("%lf %lf %lf",&C,&F,&X);
		double x=((double)(F*X)/(double)C) - F;
		//cout<<x<<endl;
		for(rate=2.0;rate<=x;rate+=F)
		{
			res+=C/rate;
		}
		res+=X/(rate);
		printf("Case #%d: %.7lf\n",iter,res);
	}
	return(0);
}

