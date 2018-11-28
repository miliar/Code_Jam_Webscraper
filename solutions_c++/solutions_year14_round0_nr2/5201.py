//siddharth prasad

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
double c,f,x,r=2.0;
using namespace std;
int main()
{
 int t,T;
 cin>>t;
 for(T=1;T<=t;T++)
 {
  cin>>c>>f>>x;
  c*=1.0000000;
  f*=1.0000000;
  x*=1.0000000;
  double time,time1,ans=0;
  r=2.0;
  while(1)
  {
      time=x/r;
      time1=((c/r)+(x/(r+f)));
      if(time1<time)
      {
          ans+=c/r;
          r+=f;
      }
      else
      {
          ans+=x/r;
          break;
      }
  }
  printf("Case #%d: %0.7f\n",T,ans);
 }
 return 0;
}
