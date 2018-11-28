#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{

	int t,tc=1;;
	double second=0.0,predict_second=0.0,farm_second=0.0,actual_second=0;
	scanf("%d",&t);
	double inc=2.0;
	double C,F,X;


	for(tc=1; tc<=t; tc++)
	{
		cin>>C>>F>>X;
		farm_second=C/inc;
		predict_second=X/(inc+F);
		actual_second=X/inc;
		while(1)
		{
			if((second+farm_second+predict_second)<(actual_second))
			{
			    actual_second=second+farm_second+predict_second;
				second+=farm_second;

				inc+=F;
				farm_second=C/inc;
				predict_second=X/(inc+F);


			}
			else
			{
				printf("Case #%d: %.7f\n",tc,actual_second);
				break;

			}
		}
		inc=2;
		second=0.0,predict_second=0.0,farm_second=0.0,actual_second=0.0;
	}


}
