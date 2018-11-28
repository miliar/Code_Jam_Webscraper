#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    freopen("qns.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    int t;
    double C,F,X,answer,low,high;
    double rate;
    int val,cnt;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
       scanf("%lf %lf %lf",&C,&F,&X);
       answer=0.0;
       rate=2.0;
       low=0.0;
       high=0.1;
       while(low<high)
       {
          high=(X/rate);
          low=(C/rate)+(X/(rate+F));
          if(low<high)
          {
            answer+=(C/rate);
            rate+=F;
          }
       }
       answer+=(X/rate);
       printf("Case #%d: %0.7lf\n",test,answer);
    }
    return 0;
}
