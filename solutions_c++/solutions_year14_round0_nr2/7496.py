#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cerr<<#x<<":"<<x<<"\n"
int cs,caseno,i;
double s,c,f,x,res;
int main()
{
  scanf("%d",&cs);
  for(caseno=1;caseno<=cs;caseno++)
  {
    scanf("%lf%lf%lf",&c,&f,&x);
    res=x/2;
    s=0;
    for(i=1;;i++)
    {
      s=s+c/(2+f*(i-1));
      if(s>res)
        break;
      res=min(res,s+x/(2+f*i));
    }
    printf("Case #%d: %.10lf\n",caseno,res);
  }
	return 0;
}
