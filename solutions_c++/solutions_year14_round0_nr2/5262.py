#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	int T, t;
	long double C, F, X, erate, prate, total_time ;
	cin>>T;
	for(t=1; t<=T; t++)
	{
		cin>>C>>F>>X;
		prate = 2.0;
		erate = 0.0;
		total_time = 0.0;
        total_time += C/prate;

		while(1)
		{
		    erate = prate + F;

            if ( X/erate >= ((X - C)/prate) )
			{
			    total_time  += (X - C)/prate;
			    break;
			}
			else
            {
                prate = erate;
                total_time += C/prate;
            }
        }
        //cout<<total_time<<endl;
        printf("Case #%d: %.7llf \n", t, total_time);
	}
	return 0;
}
