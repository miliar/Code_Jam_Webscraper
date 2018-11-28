#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<string>
#include<cstdlib>
#include<cmath>
#include<set>
#include<cstring>
#include <iomanip>
using namespace std;
main()
{
  long long int t;scanf("%lld",&t);
  for(int k=1;k<=t;k++)
  {
      double c,f,x;
      scanf("%lf%lf%lf",&c,&f,&x);
      double t=0,d=2;
	     while(1)
	      {	
	      	if((((x/d))<((c/(d))+(x/(d+f)))))
	      	{
	      		t+=(x/d);
	      		break;
	      	}
	      	else
	      	{
	      		t+=(c/d);
	      		d+=f;
	      	}
	      }
      printf("Case #%d: ",k);
      printf("%.7f\n",t);
  }
}