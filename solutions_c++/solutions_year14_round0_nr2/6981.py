#include <iostream>
#include <iomanip>
#include <cstdio>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w+",stdout);
  int test,t;
  double C,F,X,R,tottime;
  cin >> test;
  t=test;
  while(test--)
  {
  	scanf("%lf%lf%lf",&C,&F,&X);
  	R = 2;
  	if(X<C)
  		tottime = X/R;
  	else
  	{
	  	tottime=C/R;
	  	while(1)
	  	{
	  		if( (X-C)/R < X/(R+F) )
	  		{
	  			tottime += (X-C)/R;
	  			break;
	  		}
	  		else
	  		{
	  			R += F;
	  			tottime += C/R;
	  		}
	  	}
  	}
  	printf("Case #%d: %.7lf\n",t-test,tottime);
  }
}
