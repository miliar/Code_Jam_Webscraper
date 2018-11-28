#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
using namespace std;

int main()
{
    int cas,ca=1;
    double c,f,x,ans,cur;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&cas);
    while(cas--)
    {
        ans=0.0;
        cur=2.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        while(1)
        {
            ans+=c/cur;
            double t1=x/(cur+f);
            double t2=(x-c)/cur;
            if(t1<t2)
               cur+=f;
            else
            {
                ans+=t2;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",ca++,ans);
    }

    return 0;
}
