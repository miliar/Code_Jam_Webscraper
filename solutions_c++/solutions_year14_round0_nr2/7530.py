#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
	int T,t=1;
	cin>>T;
	while(T--)
	{
	    double C,F,X,cr=2,tl=0;
	    cin>>C>>F>>X;
	    if(X<=C)
	    tl=X/cr;
	    else
	    {
	    tl=C/2;
	    cr=cr+F;
	    while(F*X>cr*C)
	    {
	    	tl=tl+C/cr;
	    	cr+=F;
	    }
	    tl=tl+(X-C)/(cr-F);
	    }
	    printf("Case #%d: %.7lf\n",t,tl);
	    t=t+1;
	}
	// your code goes here
	return 0;
}
