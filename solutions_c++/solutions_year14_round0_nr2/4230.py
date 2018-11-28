
#include <iostream>
#include <stdio.h>
#include <cstring>
#include <algorithm>
#include <cstdlib>

using namespace std;
int main()
{
   	freopen("2l.in","r",stdin);
    freopen("2Lres.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int c = 1;c<=T;c++)
	{
		double C,F,X;
		// cerr<<c<<endl;
		scanf("%lf %lf %lf",&C,&F,&X);
		double res = X / 2;
		double acc= 0;
		for(int i = 1 ;i<= 100000 ;i++)
		{
			acc +=C/(2 + F * (i-1));
			double t = X/( 2 + F *i) +acc;
			// cerr<<i<<" "<<t<<endl;
			if(t < res)
				res= t;
		}



		printf("Case #%d: %.7f\n",c, res);
	}

	return 0;
}