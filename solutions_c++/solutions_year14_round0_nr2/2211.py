#include<bits/stdc++.h>
using namespace std;int main()
{
    freopen ("B-large.in","r",stdin);
    freopen ("output1.txt","w",stdout);
    int t,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        double c,f,x,t=0,r=2;
        scanf("%lf%lf%lf",&c,&f,&x);
        double t1=x/r;
        double t2=c/r;
        double t3=x/(r+f);
        while(t1>t2+t3)
        {
            t+=t2;
            r+=f;
            t1=x/r;
            t2=c/r;
            t3=x/(r+f);
        }
        t+=x/r;
        printf("Case #%d: ",k);
        printf("%.7f\n",t);
        //cout<<t;


    }
    fclose (stdout);
    fclose (stdin);
    return 0;
}
