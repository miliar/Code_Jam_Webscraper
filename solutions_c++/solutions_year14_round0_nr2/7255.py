#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
using namespace std;

  int a[10][10];
  int b[20];


  int main()
  {
      freopen("B.in","r",stdin);
      freopen("out.txt","w",stdout);
      int t,tt;
      double c,f,x;
      double tmin,v,tnow,tnext;

      cin>>t;

      for (tt=1;tt<=t;tt++)
      {
          cin>>c>>f>>x;
          tmin=x/2;
          tnow=0;
          v=2.0;
          while (tnow<tmin)
          {
              tnext=tnow+x/v;
              tmin=min(tmin,tnext);
              tnow+=c/v;
              v+=f;
          }
          printf("Case #%d: %.7f\n",tt,tmin);


      }




      return 0;
  }
