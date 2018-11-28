#include <iostream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#include<fstream>
using namespace std;
int main()
{
    int t=0,flag=0,cc=1;
    double x=0.0,f=0.0,c=0.0,r1=2.0,r2=0.0,t1=0.0,t2=0.0,nof=1.0,noc=0.0,tof=0.0;
    scanf("%d",&t);
    while(t--)
    {
        tof=0.0;
        r2=0.0;
        flag=0;
        t2=0.0;
        scanf("%lf %lf %lf",&c,&f,&x);
        t1=x/r1;
        tof=c/r1;
        r2=r1+f;
        while(flag==0)
        {
            t2=(x/r2)+(tof);
            tof=tof+(c/r2);
            nof=nof+1;
            r2=r2+f;
            if(t2>t1)
            {
                flag=1;
                break;
            }
            t1=t2;
        }
        printf("Case #%d: %0.7lf\n",cc,t1);
        cc++;
    }
    return 0;
}
