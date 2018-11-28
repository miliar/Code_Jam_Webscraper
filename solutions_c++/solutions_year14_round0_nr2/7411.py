#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include<cmath>
using namespace std;

int main()
{
     freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,tt=1;
    double c,f,x,small_x,n,time,v;
    scanf("%d",&t);
    while(t--)
    {
        v=2;
        time=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        n=ceil((x*f-c*f-2*c)/c/f);
        //printf("%lf\n",n);
        if(n<0)n=0;
        for(i=1;i<=n;i++)
        {
            time+=c/v;
            v+=f;
        }
        printf("Case #%d: %.7lf\n",tt++,time+x/v);
    }
    return 0;
}
