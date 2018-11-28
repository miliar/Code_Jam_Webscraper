#include <set>
#include <map>
#include <queue>
#include <stack>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <limits.h>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
       // freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    int T;
    double C,F,X,v;
    double result;
    int ca = 1;
    scanf("%d",&T);
    while(T--)
    {
        double x = 0,t1,t2;
        result = 0;
        v = 2;
        scanf("%lf%lf%lf",&C,&F,&X);
        while(x < X)
        {
            t1 = (X - x)/v;
            if(X - x <= C){
                result +=t1;
                break;
            }
            t2 = C/v + X/(v + F);
            if(t1 > t2)
            {
                result +=(C/v);
                v+=F;
                x = 0;
            }else{
                result +=t1;
                break;
            }


        }
        printf("Case #%d: %.7lf\n",ca++,result);

    }
}
