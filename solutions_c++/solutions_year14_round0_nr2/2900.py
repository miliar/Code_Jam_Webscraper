#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
long double C,F,X;

int main()
{
     freopen("in.txt","r",stdin);
     freopen("out.txt","w",stdout);
     int T,cas=0;
     cin>>T;
     while (T--)
     {
         cin>>C>>F>>X;
         long double ans=999999999999;
         long double per=2.0;
         long double time=0;
         while (true)
         {
             long double t1=(X)/per;
             long double t2=(C/per)+X/(per+F);
             if (ans<(min(t1+time,t2+time))) break;
             ans=min(t1+time,ans);
             ans=min(t2+time,ans);
             time+=C/per;
             per+=F;
         }
         double ou=ans;
         printf("Case #%d: %.7f\n",++cas,ou);

     }

}
