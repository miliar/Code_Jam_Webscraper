#include<cstdio>
#include<cmath>
using namespace std;
int main(void)
{
  int tc,cs;
  double r,t,a1,tmp;
  scanf("%d",&tc);
  for(cs=1;cs<=tc;cs++)
  {
    scanf("%lf%lf",&r,&t);
    a1=2*r+1;
    tmp=(int)floor((-(a1-2)+sqrt((a1-2)*(a1-2)+8*t))/4);
    if((2*a1+(tmp-1)*4)*tmp/2>t) tmp--;
    printf("Case #%d: %.0lf\n",cs,tmp);
  }
  return 0;
}
