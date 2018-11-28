#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <vector>
using namespace std;
int map[5][5];
vector<int> vec;
double time[100010];
int main()
{
    freopen("dd.in","r",stdin);
    freopen("out.txt","w+",stdout);
    int ncase,T=0;
    scanf("%d",&ncase);
    double C,F,X;
    while(ncase--)
    {
        printf("Case #%d: ",++T);
        scanf("%lf%lf%lf",&C,&F,&X);
        int num=floor(X/C)+1;
        double t=2.0;
        double ans=X/2;
        double tt=0;
        for(int i=1;i<=num;i++)
        {
            tt+=C/t;
            t+=F;
            if(ans>=tt+X/t)
            {
                ans=tt+X/t;
            }
            else
            break;
        }
        printf("%.7lf\n",ans);

    }
    return 0;
}
