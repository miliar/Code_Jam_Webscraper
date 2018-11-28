#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
vector <int> vc;
void run()
{  int t,cnt=1;
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
  double c,f,x;
  scanf("%d",&t);
  while(t--)
  {
      scanf("%lf%lf%lf",&c,&f,&x);
      double time=x/2.0;
      double tt=c/2.0+x/(2.0+f);
      int num=1;
      while(tt<time)
      {
       time=tt;
       num++;
       tt=tt-x/(2.0+(num-1)*f)+c/(2.0+(num-1)*f)+x/(2.0+(num)*f);
      }


      printf("Case #%d: %.7lf\n",cnt++,time);
  }

}
int main()
{

   run();
    return 0;
}
