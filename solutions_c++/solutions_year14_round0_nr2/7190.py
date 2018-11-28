#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      double C,F,X,time=0.0,curF=2.0,best;
      cin>>C>>F>>X;
      best = X/curF;
      do
	{
	  time+=C/curF;
	  curF+=F;
	  best = min(best,time+X/curF);
	}while(time<best);
      
      printf("Case #%d: %.7lf\n",t,best);
    }
  return 0;
}
