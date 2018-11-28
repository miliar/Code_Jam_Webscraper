#include<math.h>
#include<stdio.h>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    int t;
    double C,F,X;
    //freopen("e:\\b.txt","r",stdin);
    //freopen("e:\\f.txt","w",stdout);
    scanf("%d",&t);
    //freopen("e:\\f.txt","w",stdout);
    for(int i=1;i<=t;i++)
    {
        scanf("%lf %lf %lf",&C,&F,&X);
        double ans=0.0;
        double val=2.0;
        double temp=0.0;
        double t=C/val;
        ans=X/val;
        while((temp+t+X/(F+val))<(X/val+temp))
        {
            //printf("%.7lf %.7lf\n",t+X/(F+val),X/val+temp);
            ans=temp+t+X/(F+val);
            temp+=t;
            val+=F;
            t=C/val;
        }
        printf("Case #%d: %.7lf\n",i,ans);
    }
    //freopen("e:\\f.txt","w",stdout);
    return 0;
}
